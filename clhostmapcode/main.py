from .hostlist import host_suffixes, tldlist
import argparse
from colorama import init, Fore, Style
from curl_cffi.requests import AsyncSession, errors
import asyncio
import sys
import os 
import hmac
import secrets

HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.9",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "If-None-Match": "",
    "If-Modified-Since": ""
}

def gen_hash() -> str:
    hexone = secrets.token_hex(32)
    hextwo = secrets.token_hex(32)
    h1bytes = bytes.fromhex(hexone)
    h2bytes = bytes.fromhex(hextwo)
    hmachash = hmac.new(h1bytes, msg=h2bytes, digestmod='sha3-512')
    finalhash = hmachash.hexdigest()
    return finalhash

def extract_brand_name(user_input):
    user_input = user_input.lower()
    if "://" in user_input:
        user_input = user_input.split("://")[1]
    domain = user_input.split('/')[0]
    if domain.startswith('www.'):
        domain = domain[4:]
    if user_input.isalpha():
        brand = user_input
    else:
        brand = domain.split('.')[0]
    return brand

async def testhashes(session, sem):
    baselines = {}
    all_extensions = list(host_suffixes) + list(tldlist)
    shared_hash = gen_hash()[:16]   
    baseline_tasks = []
    extension_map = []
    async def bound_get(url):
        async with sem:
            try:
                return await session.get(url, headers=HEADER, timeout=3, impersonate="chrome120")
            except Exception as e:
                return e
    
    for ext in all_extensions:
        clean_ext = ext if ext.startswith('.') else f".{ext}"
        if ext in host_suffixes:
            fake_url = f"https://{shared_hash}{clean_ext}"
        else:
            fake_url = f"https://{shared_hash}{clean_ext}"
            
        baseline_tasks.append(bound_get(fake_url))
        extension_map.append((ext, shared_hash, fake_url))
    try:
        results = await asyncio.gather(*baseline_tasks, return_exceptions=True)
    except (KeyboardInterrupt, SystemExit):
        print("Scan stopped.")
        sys.exit(0)
    for (ext, current_hash, fake_url), res in zip(extension_map, results):
        if isinstance(res, Exception):
            continue
            
        if 200 <= res.status_code < 400 or res.status_code in [401, 403, 405, 429]:
            parsed_host = fake_url.replace("https://", "").replace("http://", "").split('/')[0]
            baselines[ext] = {
                "raw_bytes": res.content,
                "hash_str": current_hash,
                "fake_host": parsed_host
            }
    return baselines


async def test_single_url(session, url, show_unregistered, show_status, ignored_domains, baseline_signatures, target, sem, print_lock, counter_data):
    async with sem:
        current_domain = url.replace("https://", "").replace("http://", "").split('/')[0]
        try:
            res = await session.get(url, headers=HEADER, timeout=5, impersonate="chrome120")
            status = res.status_code

            if 200 <= status < 400 or status in [401, 403, 405, 429]:
                is_false_positive = False
                
                for ext, base_data in baseline_signatures.items():
                    if url.split('?')[0].split('#')[0].endswith(ext):
                        real_text = res.text
                        fake_hash = base_data["hash_str"]
                        fake_host = base_data["fake_host"]
                        
                        normalized_text = real_text.replace(current_domain, fake_host)
                        normalized_text = normalized_text.replace(target, fake_hash)
                        normalized_text = normalized_text.replace(target.upper(), fake_hash.upper())
                        normalized_text = normalized_text.replace(target.capitalize(), fake_hash.capitalize())
                        
                        normalized_bytes = normalized_text.encode('utf-8', errors='ignore')
                        
                        if normalized_bytes == base_data["raw_bytes"]:
                            is_false_positive = True
                            break

                if is_false_positive:
                    if show_unregistered:
                        async with print_lock:
                            if show_status:
                                print(f"[{Fore.GREEN}NOT REGISTERED{Fore.RESET}] {url} (Status: {status} [Fake 200])")
                            else:
                                print(f"[{Fore.GREEN}NOT REGISTERED{Fore.RESET}] {url}")
                    return

                if current_domain in ignored_domains:
                    if show_status:
                        async with print_lock:
                            print(f"[{Fore.LIGHTBLACK_EX}IGNORED{Fore.RESET}] {url} (Status: {status})")
                    return

                async with print_lock:
                    counter_data["threats"] += 1
                    if show_status:
                        print(f"[{Fore.RED}REGISTERED{Fore.RESET}] {url} (Status: {status})")
                    else:
                        print(f"[{Fore.RED}REGISTERED{Fore.RESET}] {url}")
                    
            elif show_unregistered:
                async with print_lock:
                    if current_domain in ignored_domains:
                        print(f"[{Fore.LIGHTBLACK_EX}IGNORED{Fore.RESET}] {url}")
                    elif show_status:
                        print(f"[{Fore.GREEN}NOT REGISTERED{Fore.RESET}] {url} (Status: {status})")
                    else:
                        print(f"[{Fore.GREEN}NOT REGISTERED{Fore.RESET}] {url}")

        except errors.RequestsError as e:
            if show_unregistered:
                if current_domain in ignored_domains:
                    return
                async with print_lock:
                    if show_status:
                        err_msg = str(e).lower()
                        if "dns" in err_msg or "resolve" in err_msg:
                            print(f"[{Fore.GREEN}NOT REGISTERED{Fore.RESET}] {url} ({Fore.LIGHTBLACK_EX}DNS Error{Fore.RESET})")
                        else:
                            print(f"[{Fore.GREEN}NOT REGISTERED{Fore.RESET}] {url} ({Fore.LIGHTBLACK_EX}Conn Error{Fore.RESET})")
                    else:
                        print(f"[{Fore.GREEN}NOT REGISTERED{Fore.RESET}] {url}")
                    
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception:
            if show_unregistered and current_domain not in ignored_domains:
                async with print_lock:
                    if show_status:
                        print(f"[{Fore.GREEN}NOT REGISTERED{Fore.RESET}] {url} ({Fore.LIGHTBLACK_EX}Error{Fore.RESET})")
                    else:
                        print(f"[{Fore.GREEN}NOT REGISTERED{Fore.RESET}] {url}")



async def testalldomains(target, show_unregistered, show_status, ignored_domains, only_results, sem):
    all_domains = []
    
    for suffix in host_suffixes:
        all_domains.append(f"https://{target}{suffix}")
        
    for tld in tldlist:
        tld = tld if tld.startswith('.') else f".{tld}"
        all_domains.append(f"https://{target}{tld}")

    if not only_results:
        print(f"Loaded {len(all_domains)} total hosts to test.\n")
    async with AsyncSession() as session:
        if not only_results:
            print(f"Testing fake domain for all hosts...")
        baseline_signatures = await testhashes(session, sem)
        if not only_results:
            print("Fake domain test complete")
            print(f"\n{Style.BRIGHT}Scanning...\n")
        print_lock = asyncio.Lock() #prevent race condition
        counter_data = {"threats": 0}
        tasks = [
            test_single_url(session, url, show_unregistered, show_status, ignored_domains, baseline_signatures, target, sem, print_lock, counter_data) 
            for url in all_domains
        ]
        try:
            await asyncio.gather(*tasks)
        except (KeyboardInterrupt, SystemExit):
            print(f"\nScan stopped.")
            sys.exit(0)

def chtrack():
    parser = argparse.ArgumentParser(description="Tool to check if other people have tried impersonating your company/website.")
    parser.add_argument("site", nargs='?', help="URL or brand name to verify.")
    parser.add_argument("-su", "--show-unregistered", action="store_true", help="Display unregistered domains as well.")
    parser.add_argument("-ss", "--show_status", action="store_true", help="Provide status codes/errors for every domain checked (forces -su).")
    parser.add_argument("-sr", "--self-registered", help="Domains that you yourself have registered, so that those domains will be ignored. Use comma-seperated values or path to a text file.")
    parser.add_argument("-or", "--only-results", action='store_true', help="Only print the result")
    parser.add_argument("-ccr", "--concurrent-req", type=int, default=100, help="Maximum number of async requests, default 100.")
    args = parser.parse_args()

    MAX_CC_REQ = args.concurrent_req
    sem = asyncio.Semaphore(MAX_CC_REQ)
    show_unregistered = args.show_unregistered
    show_status = args.show_status
    only_results = args.only_results
    if not args.only_results:
        init(autoreset=True)
        print()
        print("-" * 65)
        print(f"{Style.BRIGHT}ClHostMap {Fore.LIGHTMAGENTA_EX}v1.1.0")
        print()
        print(f"Made by: {Fore.LIGHTMAGENTA_EX}SphericalFlower52811")
        print()
        print(f"{Fore.LIGHTBLUE_EX}GitHub: {Fore.RESET}{Style.BRIGHT}https://github.com/SphericalFlower52811/clhostmap")
        print("-" * 65)
        print()

    site = args.site if args.site else input("Website to test not found.\nEnter website (e.g. https://example.com): ").lower().strip()
    target = extract_brand_name(site)
    if not only_results:
        print(f"Target: {Style.BRIGHT}{Fore.CYAN}{target}")
    ignored_domains = set()
    init_domain = site.replace("https://", "").replace("http://", "").split('/')[0]
    if init_domain.startswith("www."):
        init_domain = init_domain[4:]
    if '.' in init_domain:
        ignored_domains.add(init_domain)
    if args.self_registered:
        if os.path.isfile(args.self_registered):
            try:
                with open(args.self_registered, "r") as f:
                    for line in f:
                        item = line.strip().lower()
                        if "://" in item:
                            item = item.split("://")[1]
                        item = item.split('/')[0]
                        if item.startswith("www."):
                            item = item[4:]
                        if item and not item.isalpha() and '.' in item:
                            ignored_domains.add(item)
            except Exception:
                pass
        else:
            for piece in args.self_registered.split(","):
                item = piece.strip().lower()
                if "://" in item:
                    item = item.split("://")[1]
                item = item.split('/')[0]
                if item.startswith("www."):
                    item = item[4:]
                if '.' in item:
                    ignored_domains.add(item)

    if ignored_domains and not only_results:
        print(f"{Fore.LIGHTBLACK_EX}Domains to be ignored: {Fore.RESET}{', '.join(sorted(ignored_domains))}")
    print()
    
    try:
        asyncio.run(testalldomains(target, show_unregistered, show_status, ignored_domains, only_results, sem))
    except KeyboardInterrupt:
        print(f"\nScan stopped.")

if __name__ == '__main__':
    chtrack()
