# Code used to write TLDs to alltlds.txt from IANA.

from curl_cffi import requests

def get_iana_tld_list():
    url = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt"
    try:
        response = requests.get(url, impersonate="chrome120")
        if response.status_code == 200:
            lines = response.text.splitlines()
            return [line.strip().lower() for line in lines if not line.startswith("#") and line.strip()]
    except Exception as e:
        print(f"Failed: {e}")
    return []

alltlds = get_iana_tld_list()
print(f"number of tlds: {len(alltlds)}\n")

with open("alltlds.txt", "w") as f:
    for tld in alltlds:
        f.write(tld)
        f.write(" | ")