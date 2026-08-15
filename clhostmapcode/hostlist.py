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
                     ".is-a.software", ".thedev.id", ".dedyn.io", ".eu.org", ".ngrok-free.app", ".loca.lt"]
country_tlds = [".ac", ".ad", ".ae", ".af", ".ag", ".ai", ".al", ".am", ".ao", ".aq",
                ".ar", ".as", ".at", ".au", ".aw", ".ax", ".az", ".ba", ".bb", ".bd",
                ".be", ".bf", ".bg", ".bh", ".bi", ".bj", ".bl", ".bm", ".bn", ".bo",
                ".bq", ".br", ".bs", ".bt", ".bv", ".bw", ".by", ".bz", ".ca", ".cc",
                ".cd", ".cf", ".cg", ".ch", ".ci", ".ck", ".cl", ".cm", ".cn", ".co",
                ".cr", ".cu", ".cv", ".cw", ".cx", ".cy", ".cz", ".de", ".dj", ".dk",
                ".dm", ".do", ".dz", ".ec", ".ee", ".eg", ".eh", ".er", ".es", ".et",
                ".eu", ".fi", ".fj", ".fk", ".fm", ".fo", ".fr", ".ga", ".gd", ".ge",
                ".gf", ".gg", ".gh", ".gi", ".gl", ".gm", ".gn", ".gp", ".gq", ".gr",
                ".gs", ".gt", ".gu", ".gw", ".gy", ".hk", ".hm", ".hn", ".hr", ".ht",
                ".hu", ".id", ".ie", ".il", ".im", ".in", ".io", ".iq", ".ir", ".is",
                ".it", ".je", ".jm", ".jo", ".jp", ".ke", ".kh", ".ki", ".km", ".kn",
                ".kp", ".kr", ".kw", ".ky", ".kz", ".la", ".lb", ".lc", ".li", ".lk",
                ".lr", ".ls", ".lt", ".lu", ".lv", ".ly", ".ma", ".mc", ".md", ".me",
                ".mf", ".mg", ".mh", ".mk", ".ml", ".mm", ".mn", ".mo", ".mp", ".mq",
                ".mr", ".ms", ".mt", ".mu", ".mv", ".mw", ".mx", ".my", ".mz", ".na",
                ".nc", ".ne", ".nf", ".ng", ".ni", ".nl", ".no", ".np", ".nr", ".nu",
                ".nz", ".om", ".pa", ".pe", ".pf", ".pg", ".ph", ".pk", ".pl", ".pm",
                ".pn", ".pr", ".ps", ".pt", ".pw", ".py", ".qa", ".re", ".ro", ".rs",
                ".ru", ".rw", ".sa", ".sb", ".sc", ".sd", ".se", ".sg", ".sh", ".si",
                ".sj", ".sk", ".sl", ".sm", ".sn", ".so", ".sr", ".ss", ".st", ".su",
                ".sv", ".sx", ".sy", ".sz", ".tc", ".td", ".tf", ".tg", ".th", ".tj",
                ".tk", ".tl", ".tm", ".tn", ".to", ".tr", ".tt", ".tv", ".tw", ".tz",
                ".ua", ".ug", ".uk", ".us", ".uy", ".uz", ".va", ".vc", ".ve", ".vg",
                ".vi", ".vn", ".vu", ".wf", ".ws", ".ye", ".yt", ".za", ".zm", ".zw"
            ]

generic_tlds_part1 = [
    ".com", ".org", ".net", ".info", ".biz", ".name", ".xyz", ".top", ".club", ".online",
    ".site", ".tech", ".store", ".app", ".dev", ".link", ".website", ".live", ".space", ".shop",
    ".work", ".click", ".vip", ".loan", ".win", ".men", ".bid", ".stream", ".download", ".accountant",
    ".trade", ".science", ".cricket", ".party", ".faith", ".webcam", ".gdn", ".date", ".racing", ".review",
    ".web", ".cloud", ".digital", ".agency", ".marketing", ".studio", ".design", ".photography", ".media", ".news",
    ".today", ".world", ".global", ".international", ".expert", ".guru", ".solutions", ".systems", ".services", ".support",
    ".network", ".company", ".business", ".enterprise", ".ltd", ".inc", ".pro", ".mobi", ".tel", ".asia",
    ".cat", ".jobs", ".travel", ".museum", ".coop", ".aero", ".icu", ".cyou", ".monster", ".fun",
    ".buzz", ".lol", ".wtf", ".fail", ".rocks", ".cool", ".best", ".money", ".gold", ".finance",
    ".capital", ".investments", ".exchange", ".market", ".trading", ".bank", ".credit", ".cards", ".cash", ".tax",
    ".pay", ".secure", ".safe", ".protection", ".security", ".legal", ".law", ".court", ".health", ".clinic",
    ".doctor", ".hospital", ".care", ".life", ".fit", ".games", ".play", ".casino", ".bet", ".poker",
    ".bingo", ".lotto", ".run", ".walk", ".ride", ".family", ".mom", ".dad", ".kids", ".baby",
    ".pet", ".dog", ".home", ".house", ".rent", ".buy", ".sale", ".discount", ".coupons", ".deals",
    ".cheap", ".free", ".bargain", ".save", ".academy", ".accountants", ".actor", ".ads", ".adult", ".affiliate",
    ".apartments", ".arch", ".architect", ".army", ".art", ".associates", ".attorney", ".auction", ".audio", ".auto",
    ".autos", ".band", ".bar", ".bargains", ".baseball", ".basketball", ".beauty", ".beer", ".bible", ".bike",
    ".bio", ".black", ".blackfriday", ".blog", ".blue", ".boats", ".bonds", ".boo", ".book", ".boutique",
    ".box", ".broadway", ".broker", ".builders", ".build", ".cab", ".cafe", ".cam", ".camera", ".camp"
]

generic_tlds_part2 = [
    ".capital", ".car", ".cards", ".care", ".careers", ".cars", ".casa", ".case", ".cash", ".casino",
    ".catering", ".center", ".ceo", ".charity", ".chat", ".cheap", ".chinas", ".chloe", ".christmas", ".church",
    ".cie", ".cisco", ".citadel", ".citi", ".city", ".claims", ".cleaning", ".clinic", ".clothing", ".cloud",
    ".club", ".coach", ".codes", ".coffee", ".college", ".cologne", ".community", ".company", ".compare", ".computer",
    ".comsec", ".condos", ".construction", ".consulting", ".contact", ".contractors", ".cooking", ".cool", ".coop", ".corsica",
    ".country", ".coupon", ".coupons", ".courses", ".credit", ".creditcard", ".creditunion", ".cricket", ".crown", ".cruise",
    ".cruises", ".cuisinella", ".cyou", ".dabur", ".dad", ".dance", ".data", ".date", ".dating", ".datsun",
    ".day", ".daze", ".deal", ".deals", ".degree", ".delivery", ".dell", ".deloitte", ".democrat", ".dental",
    ".dentist", ".desi", ".design", ".dev", ".dhl", ".diamonds", ".diet", ".digital", ".direct", ".directory",
    ".discount", ".discover", ".dish", ".diy", ".dnp", ".docs", ".doctor", ".dodge", ".dog", ".domains",
    ".dot", ".download", ".drive", ".dtv", ".dubai", ".duck", ".dunlop", ".dupont", ".durban", ".dvag",
    ".dvr", ".earth", ".eat", ".eco", ".edeka", ".education", ".email", ".emerck", ".energy", ".engineer",
    ".engineering", ".enterprises", ".epson", ".equipment", ".ericsson", ".erni", ".esurance", ".estate", ".etisalat", ".eurovision",
    ".eus", ".events", ".exchange", ".expert", ".exposed", ".express", ".extraspace", ".fage", ".fail", ".fairwinds",
    ".faith", ".family", ".fan", ".fans", ".farm", ".farmers", ".fashion", ".fast", ".fedex", ".feedback",
    ".ferrari", ".ferrero", ".fiat", ".fidelity", ".fido", ".film", ".final", ".finance", ".financial", ".fire",
    ".firestone", ".firmdale", ".fish", ".fishing", ".fit", ".fitness", ".flickr", ".flights", ".flir", ".florist",
    ".flowers", ".fly", ".foo", ".food", ".football", ".ford", ".forex", ".forsale", ".forum", ".foundation",
    ".fox", ".free", ".fresenius", ".frl", ".frogans", ".frontier", ".ftr", ".fujitsu", ".fun", ".fund",
    ".furniture", ".futbol", ".fyi", ".gal", ".gallery", ".gallo", ".gallup", ".game", ".games", ".garena"
]

generic_tlds_part3 = [
    ".gallo", ".gallup", ".garden", ".gayi", ".gbiz", ".gdn", ".gea", ".gent", ".genting", ".george",
    ".ggee", ".gift", ".gifts", ".gives", ".giving", ".glass", ".gle", ".global", ".globo", ".gmail",
    ".gmo", ".gmx", ".godaddy", ".gold", ".goldpoint", ".golf", ".goo", ".goodyear", ".goog", ".google",
    ".gop", ".got", ".grainger", ".graphics", ".gratis", ".green", ".gripe", ".grocery", ".group", ".guardian",
    ".gucci", ".guge", ".guide", ".guitars", ".guru", ".hair", ".hamburg", ".hangout", ".haus", ".hbo",
    ".hdfc", ".hdfcbank", ".health", ".healthcare", ".help", ".helsinki", ".here", ".hermes", ".hiphop", ".hisamitsu",
    ".hitachi", ".hiv", ".hkt", ".hockey", ".holdings", ".holiday", ".homedepot", ".homegoods", ".homes", ".homesense",
    ".honda", ".horse", ".hospital", ".host", ".hosting", ".hot", ".hotels", ".hotmail", ".house", ".how",
    ".hsbc", ".htc", ".hughes", ".hyundai", ".ibm", ".icbc", ".ice", ".icu", ".ieee", ".ifm",
    ".ikano", ".imamat", ".imdb", ".immo", ".immobilien", ".inc", ".industries", ".infiniti", ".info", ".ing",
    ".ink", ".institute", ".insurance", ".insure", ".intel", ".international", ".intuit", ".investments", ".ipiranga", ".irish",
    ".intel", ".intuit", ".investments", ".ipiranga", ".irish", ".iselect", ".ismaili", ".ist", ".istanbul", ".itau",
    ".itv", ".iveco", ".jaguar", ".java", ".jcb", ".jcp", ".jeep", ".jio", ".jll", ".jmp",
    ".jnj", ".jobs", ".joburg", ".jot", ".joy", ".jpmorgan", ".jprs", ".juegos", ".juniper", ".kaufen",
    ".kddi", ".kerryhotels", ".kerryproperties", ".kerrylogistics", ".kfh", ".kia", ".kids", ".kim", ".kinder", ".kindle",
    ".kitchen", ".kiwi", ".koeln", ".komatsu", ".kosher", ".kpmg", ".kpn", ".krd", ".kred", ".kuwait",
    ".kyoto", ".lacaixa", ".lamborghini", ".lamer", ".lancaster", ".lancia", ".land", ".landrover", ".lanxess", ".lasalle",
    ".lat", ".latrobe", ".law", ".lawyer", ".lds", ".lease", ".leclerc", ".lefrak", ".legal", ".lego",
    ".lexus", ".lgbt", ".lidl", ".life", ".lifeinsurance", ".lifestyle", ".lighting", ".like", ".lilly", ".limited",
    ".limo", ".lincoln", ".linde", ".link", ".lipsy", ".live", ".livenet", ".lixil", ".loan", ".loans"
]

generic_tlds_part4 = [
    ".locker", ".locus", ".lol", ".london", ".lotte", ".lotto", ".love", ".lpl", ".lplfinancial", ".ltd",
    ".ltda", ".lucerne", ".lupin", ".luxe", ".luxury", ".macys", ".madrid", ".maif", ".maison", ".makeup",
    ".management", ".mango", ".map", ".market", ".marketing", ".markets", ".marriott", ".marshall", ".maserati", ".mattel",
    ".mba", ".mcd", ".mcdonalds", ".mckinsey", ".med", ".media", ".meet", ".melbourne", ".meme", ".memorial",
    ".mens", ".menu", ".merckmsd", ".metlife", ".miami", ".microsoft", ".mini", ".mint", ".mit", ".mitsubishi",
    ".mlb", ".mls", ".mma", ".mobi", ".mobile", ".moda", ".moe", ".moi", ".mom", ".monash",
    ".money", ".monster", ".mormon", ".mortgage", ".moscow", ".moto", ".motorcycles", ".mov", ".movie", ".msd",
    ".mtn", ".mtr", ".museum", ".mutual", ".nab", ".nagoya", ".navy", ".nba", ".nec", ".netbank",
    ".new", ".news", ".next", ".nextdirect", ".nexus", ".nfl", ".ngo", ".nhk", ".nico", ".nike",
    ".nikon", ".ninja", ".nissan", ".nissay", ".nokia", ".northwesternmutual", ".norton", ".now", ".nowtv", ".nowruz",
    ".nra", ".nrw", ".ntt", ".nyc", ".obi", ".observer", ".off", ".office", ".okinawa", ".olayan",
    ".olayangroup", ".oldnavy", ".ollo", ".om", ".omega", ".one", ".ong", ".onl", ".online", ".onyourside",
    ".ooo", ".open", ".oracle", ".orange", ".org", ".organic", ".origins", ".osaka", ".otsuka", ".ovh",
    ".page", ".panasonic", ".paris", ".pars", ".partners", ".parts", ".party", ".passagens", ".pay", ".pccw",
    ".pet", ".pfizer", ".pharmacy", ".phd", ".philips", ".phone", ".photo", ".photography", ".photos", ".physio",
    ".pics", ".pictet", ".pictures", ".pid", ".pin", ".ping", ".pink", ".pioneer", ".pizza", ".place",
    ".play", ".playstation", ".plumbing", ".plus", ".pnc", ".pohl", ".poker", ".politie", ".porno", ".post",
    ".pramerica", ".praxi", ".press", ".prime", ".pro", ".prod", ".productions", ".prof", ".progressive", ".promo",
    ".properties", ".property", ".protection", ".pru", ".prudential", ".pub", ".pwc", ".qpon", ".quebec", ".quest",
    ".racing", ".radio", ".read", ".realestate", ".realtor", ".realty", ".recipes", ".red", ".redstone", ".redumbrella"
]

generic_tlds_1 = set((
    generic_tlds_part1 + 
    generic_tlds_part2
))

wd_generic_tlds_2 = set(( 
    generic_tlds_part3 + 
    generic_tlds_part4
))

generic_tlds_2 = list(wd_generic_tlds_2 - generic_tlds_1)
generic_tlds_1 = list(generic_tlds_1)