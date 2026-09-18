host_suffixes = [".vercel.app", ".netlify.app", ".pages.dev", ".github.io", 
                     ".gitlab.io", ".stormkit.io", ".surge.sh", ".amplifyapp.com", 
                     ".herokuapp.com", ".railway.app", ".onrender.com", ".fly.dev", 
                     ".zeabur.app", ".koyeb.app", ".cleverapps.io", ".scw.cloud", 
                     ".up.railway.app", ".alwaysdata.net", ".qovery.app", ".northflank.app", 
                     ".porter.run", ".back4app.io", ".cyclic.app", ".choreoapps.dev", 
                     ".pythonanywhere.com", ".streamlit.app", ".hf.space", ".gradio.live", 
                     ".anvil.app", ".modal.run", ".wasmer.app", ".supabase.co", ".web.app", 
                     ".firebaseapp.com", ".supabase.com", ".appwriteapp.com", ".parseapp.com", 
                     ".wixsite.com", ".weebly.com", ".webflow.io", ".squarespace.com", 
                     ".wordpress.com", ".ghost.io", ".framer.app", ".framer.website", 
                     ".bubbleapps.io", ".carrd.co", ".pantheonsite.io", ".shopifypreview.com", 
                     ".myshopify.com", ".rhcloud.com", ".oraclecloud.com", ".fleek.co", ".ipfs.dweb.link", 
                     ".repl.co", ".replit.app", ".glitch.me", ".codeanywhere.com", ".js.org", ".is-a.dev", 
                     ".is-a.software", ".thedev.id", ".dedyn.io", ".eu.org", ".ngrok-free.app", ".loca.lt",
                     ".base44.app", ".lovable.app"]

from pathlib import Path

current_file = Path(__file__).resolve()
alltlds_path = current_file.parent / "alltlds.txt"

tldlist = []
with open(alltlds_path, "r") as tldfile:
    alltldsseparated = tldfile.read().strip().replace(" ", "").replace("\n", "")
    raw_tldlist = alltldsseparated.split("|")

    for ext in raw_tldlist:
            clean_ext = ext.strip().lower()
            if clean_ext:
                tldlist.append(clean_ext)
                
                # If it's a Punycode string, decode its native language characters 
                if clean_ext.startswith("xn--"):
                    try:
                        decoded_language = clean_ext.encode('ascii').decode('idna')
                        tldlist.append(decoded_language)
                    except Exception:
                        pass

if __name__ == '__main__':
    print(len(tldlist))
    print(len(host_suffixes))