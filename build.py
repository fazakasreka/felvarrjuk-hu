import json
import os
from datetime import date

SITE = "http://www.felvarrjuk.hu"
MAPS = "https://www.google.hu/maps/place/Mikl%C3%B3s+u.+9,+Budapest,+1033/@47.5434651,19.0432522,17z"
EMBED = "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2693.2498854607456!2d19.0432522!3d47.543465100000006!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4741d96721e4fc93%3A0x20fdfc344be69625!2sMikl%C3%B3s+u.+9%2C+Budapest%2C+1033!5e0!3m2!1shu!2shu!4v1430750934724"
FONTS = "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Outfit:wght@300;400;500;600&display=swap"

# Set by build(); t() returns only the text of the language being built.
LANG = "hu"


def t(hu, en):
    return hu if LANG == "hu" else en


NAV = [
    ("#fooldal", "Főoldal", "Home"),
    ("#szolgaltatasok", "Szolgáltatások", "Services"),
    ("#arak", "Árak", "Prices"),
    ("#kapcsolat", "Kapcsolat", "Contact"),
    ("#allas", "Állás", "Jobs"),
]

PAGES = {
    "hu": {
        "path": "/",
        "file": "index.html",
        "prefix": "",
        "title": "III. kerületi óbudai varrónő | Felvarrjuk",
        "desc": "III. kerületi óbudai varrónő: ruhajavítás, ruhaigazítás, ruhaalakítás. Miklós utca 9.",
        "keywords": "III. kerületi óbudai varrónő, varrás, ruhajavítás, ruhaigazítás, III. kerület, Óbuda, Miklós utca 9",
        "locale": "hu_HU",
        "ld_desc": "Varrónő Óbudán: ruhajavítás, ruhaigazítás, ruhaalakítás, függönyvarrás és színtanácsadás 2000 óta.",
    },
    "en": {
        "path": "/en/",
        "file": "en/index.html",
        "prefix": "../",
        "title": "Clothing alterations and tailoring in Óbuda, Budapest | Felvarrjuk",
        "desc": "Seamstress in Óbuda, Budapest III: clothing alterations, repairs, tailoring and curtain making at Miklós utca 9. Open Mon–Fri.",
        "keywords": "tailor Óbuda, seamstress Budapest, clothing alterations, clothing repair, tailoring, curtain making, Budapest III district, Miklós utca 9",
        "locale": "en_US",
        "ld_desc": "Seamstress in Óbuda, Budapest: clothing alterations, repairs, tailoring, curtain making and colour consultation since 2000.",
    },
}


def jsonld(p):
    return json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "TailorShop",
            "name": "Felvarrjuk",
            "description": p["ld_desc"],
            "url": SITE + p["path"],
            "telephone": "+36203755366",
            "email": "felvarrjuk@gmail.com",
            "foundingDate": "2000",
            "hasMap": MAPS,
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Miklós utca 9.",
                "addressLocality": "Budapest",
                "addressRegion": "Budapest",
                "postalCode": "1033",
                "addressCountry": "HU",
            },
            "geo": {"@type": "GeoCoordinates", "latitude": 47.5434651, "longitude": 19.0432522},
            "openingHoursSpecification": [
                {
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                    "opens": "10:30",
                    "closes": "17:00",
                }
            ],
            "knowsLanguage": ["hu", "en"],
            "areaServed": "Budapest III. kerület, Óbuda",
        },
        ensure_ascii=False,
        indent=2,
    )


def page(body):
    p = PAGES[LANG]
    pre = p["prefix"]
    url = SITE + p["path"]
    other_locale = PAGES["en" if LANG == "hu" else "hu"]["locale"]
    links = "\n          ".join(
        f'<a href="{href}" data-section="{href[1:]}">{t(hu, en)}</a>'
        for href, hu, en in NAV
    )
    # Language switch: plain links between the two pages
    hu_href = "index.html" if LANG == "hu" else "../index.html"
    en_href = "en/index.html" if LANG == "hu" else "index.html"
    hu_cur = ' aria-current="true"' if LANG == "hu" else ""
    en_cur = ' aria-current="true"' if LANG == "en" else ""
    return f'''<!DOCTYPE html>
<html lang="{LANG}">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{p["title"]}</title>
    <meta name="description" content="{p["desc"]}">
    <meta name="keywords" content="{p["keywords"]}">
    <meta name="author" content="Szolnoki András">
    <link rel="canonical" href="{url}">
    <link rel="alternate" hreflang="hu" href="{SITE}/">
    <link rel="alternate" hreflang="en" href="{SITE}/en/">
    <link rel="alternate" hreflang="x-default" href="{SITE}/">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Felvarrjuk">
    <meta property="og:title" content="{p["title"]}">
    <meta property="og:description" content="{p["desc"]}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{SITE}/images/varro-uzlet.jpg">
    <meta property="og:locale" content="{p["locale"]}">
    <meta property="og:locale:alternate" content="{other_locale}">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="{FONTS}" rel="stylesheet">
    <link href="{pre}styles.css" rel="stylesheet">
    <script type="application/ld+json">
{jsonld(p)}
    </script>
  </head>
  <body>
    <a class="skip" href="#fooldal">{t("Ugrás a tartalomhoz", "Skip to content")}</a>
    <header class="site-header">
      <div class="header-inner">
        <a class="brand" href="#fooldal">
          <strong>Felvarrjuk</strong>
          <span>{t("Minden, ami öltés", "A stitch in time")}</span>
        </a>
        <nav class="nav" id="nav" aria-label="{t("Fő navigáció", "Main navigation")}">
          {links}
        </nav>
        <div class="header-tools">
          <div class="lang" role="group" aria-label="Nyelv / Language">
            <a href="{hu_href}" hreflang="hu" lang="hu"{hu_cur}>HU</a>
            <a href="{en_href}" hreflang="en" lang="en"{en_cur}>EN</a>
          </div>
          <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav" aria-label="{t("Menü", "Menu")}">
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path class="bars" d="M4 7h16M4 12h16M4 17h16"/><path class="close" d="M6 6l12 12M18 6L6 18"/></svg>
          </button>
        </div>
      </div>
    </header>
{body}
    <footer class="site-footer">
      <div class="wrap footer-grid">
        <div>
          <strong>Felvarrjuk</strong>
          <address>Budapest III. {t("kerület", "district")}, Óbuda<br>Miklós utca 9.</address>
          <a class="maplink" href="{MAPS}" target="_blank" rel="noopener">{t("Megnyitás a Google Térképen", "Open in Google Maps")}</a>
        </div>
        <div>
          <strong>{t("Nyitva", "Hours")}</strong>
          <p>{t("Hétfő–Péntek 10:30–17:00", "Mon–Fri 10:30–17:00")}</p>
          <p>{t("Egyeztetéssel 17:00–20:00", "By appointment 17:00–20:00")}</p>
        </div>
        <div>
          <strong>{t("Elérhetőség", "Contact")}</strong>
          <p><a href="tel:+36203755366">06-20-375-5366</a></p>
        </div>
      </div>
    </footer>
    <script>
      (() => {{
        const root = document.documentElement;
        const footer = document.querySelector(".site-footer");
        const updateFooterHeight = () => {{
          if (footer) root.style.setProperty("--footer-height", `${{footer.offsetHeight}}px`);
        }};
        updateFooterHeight();
        if ("ResizeObserver" in window && footer) new ResizeObserver(updateFooterHeight).observe(footer);
        window.addEventListener("resize", updateFooterHeight);
      }})();
    </script>
    <script src="{pre}script.js"></script>
  </body>
</html>
'''


def hero(h1_hu, h1_en, p_hu, p_en):
    return f'''        <div class="page-hero">
          <div class="wrap">
            <h1>{t(h1_hu, h1_en)}</h1>
            <p>{t(p_hu, p_en)}</p>
          </div>
        </div>'''


def build_body():
    pre = PAGES[LANG]["prefix"]

    # Home
    home = f'''
    <section class="hero" id="fooldal">
      <div class="hero-inner">
        <h1>Felvarrjuk.hu <small>{t("– varrónő és ruhajavítás Óbudán", "– tailoring and clothing alterations in Óbuda")}</small></h1>
        <p class="lede">{t("Nagyból kicsit – kicsiből nagyot alkotni, mi ez, ha nem művészet.", "Turning something big into something small, and small into something grand – if that isn’t art, what is?")}</p>
        <div class="hero-tags" aria-label="{t("Kapcsolati információk", "Contact information")}">
          <a class="hero-tag" href="{MAPS}" target="_blank" rel="noopener">
            {t("Óbuda","1033 Budapest")}, Miklós utca 9.
          </a>
          <span class="hero-tag">
            {t("H–P 10:30–17:00", "Mon–Fri 10:30–17:00")}
          </span>
          <a class="hero-tag" href="tel:+36203755366">06-20-375-5366</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap split">
        <blockquote class="quote">{t("Ötlettárunk majdnem kimeríthetetlen!", "Our supply of ideas is nearly endless!")}</blockquote>
        <div class="copy">
          <p>{t("Ha megtetszik egy új ruha, vagy a régi kedvenc ruhádat megváltoztatnád, jussunk eszedbe: kívánság szerint lehet hozzáadni, elvenni, alakra szabni, megjavítani.", "Fallen for a new piece, or want to give an old favourite a fresh look? Come and see us: we can add, take away, tailor to your shape or repair, whatever you wish.")}</p>
          <p>{t("Ha van elképzelésed, amihez tű, cérna és szaktudás kell, megtalálsz minket. A megvalósításra váró ötleted számunkra kihívás.", "Got an idea that calls for needle, thread and real expertise? You’ve found the right place. For us, an idea waiting to come to life is a welcome challenge.")}</p>
          <p>{t("2000 óta működő III. kerületi óbudai üzletünkben szeretettel várjuk leendő és új ügyfeleinket.", "We’ve been running our shop in Óbuda, District III, since 2000, and we warmly welcome both new and returning customers.")}</p>
          <p class="highlight">{t("Személyre szabott szolgáltatással, elégedettségi garanciával.", "Personal service, with a satisfaction guarantee.")}</p>
        </div>
      </div>
    </section>
'''

    # Services — one section, including colour consultation
    svc = [
        ("Női ruházat", "Women’s clothing", None),
        ("Férfiruházat", "Men’s clothing", None),
        ("Gyerekruházat", "Children’s clothing", None),
        ("Sportruházat", "Sportswear", ("elasztikus anyagból is", "including stretch fabrics")),
        ("Farmerruházat", "Denim", None),
        ("Bőrruházat", "Leather", None),
        ("Lakástextil", "Home textiles", None),
        ("Függönyvarrás", "Curtain making", None),
        ("Márkásruházat igény szerinti átalakítása, igazítása, a gyártó eredeti állapotára kivitelezve", "Designer and brand-name clothing altered or adjusted to your wishes, finished to the manufacturer’s original standard", None),
    ]
    lis = "".join(
        f'<li>{t(hu, en)}{(" <small>" + t(*extra) + "</small>") if extra else ""}</li>'
        for hu, en, extra in svc
    )
    seasons = [
        ("winter", "Tél", "Winter", "élénk–sötét", "bright–deep"),
        ("spring", "Tavasz", "Spring", "élénk–világos", "bright–light"),
        ("summer", "Nyár", "Summer", "tört–világos", "soft–light"),
        ("autumn", "Ősz", "Autumn", "tört–sötét", "soft–deep"),
    ]
    seas = "".join(
        f'<article class="season"><div class="swatch {cls}"></div><h3>{t(hu, en)}</h3><p>{t(a, b)}</p></article>'
        for cls, hu, en, a, b in seasons
    )
    services = f'''
    <section class="page-section section-alt" id="szolgaltatasok">
{hero("Szolgáltatások", "Services", "Fő profilunk a méretre igazítás, a ruhajavítás és az alakítás.", "Fitting, mending and altering are what we do best.")}
      <div class="section services-content">
        <div class="wrap">
          <ul class="list">{lis}</ul>
        </div>
      </div>
      <div class="section colour-consultation">
        <div class="wrap">
          <h2>{t("Színtanácsadás", "Colour consultation")}</h2>
          <p class="copy">{t("Bőrünk, szemünk és hajunk színe összhangban van. Ha a ruháinkat és a sminket ehhez igazítjuk, időt és pénzt spórolunk vásárláskor. Színes kendős színanalízissel meghatározzuk az évszaktípusodat:", "The colours of your skin, eyes and hair work together in natural harmony. Choosing clothes and make-up to match saves you time and money when shopping. Using coloured drapes, we analyse your colouring to find your seasonal type:")}</p>
          <div class="seasons slim">{seas}</div>
        </div>
      </div>
    </section>
'''

    # Prices
    pr = [
        ("Nadrág felhajtás", "Trouser hemming", "1950 Ft-tól", "from 1,950 HUF"),
        ("Nadrág cipzár csere", "Trouser zip replacement", "2500 Ft-tól", "from 2,500 HUF"),
        ("Szoknya cipzár csere", "Skirt zip replacement", "2700 Ft-tól", "from 2,700 HUF"),
        ("Fürdőruha átalakítás", "Swimwear alteration", "3500 Ft-tól", "from 3,500 HUF"),
        ("Karcsúsítás, szűkítés", "Taking in / slimming", "2500 Ft-tól", "from 2,500 HUF"),
        ("Függönyvarrás", "Curtain making", "550 Ft-tól / méter", "from 550 HUF per metre"),
    ]
    rows = "".join(f'<tr><th scope="row">{t(a,b)}</th><td>{t(c,d)}</td></tr>' for a,b,c,d in pr)
    prices = f'''
    <section class="page-section" id="arak">
{hero("Árak", "Prices", "Árainkból – a végső ár a munkától függ.", "A selection of our prices. The final cost depends on the work involved.")}
      <div class="section prices-content">
        <div class="wrap">
          <table class="price-table"><tbody>{rows}</tbody></table>
          <p class="note">{t("Kérdés esetén hívj:", "Any questions? Call us on")} <a href="tel:+36203755366">06-20-375-5366</a></p>
        </div>
      </div>
    </section>
'''

    # Contact
    contact = f'''
    <section class="page-section section-alt" id="kapcsolat">
{hero("Kapcsolat", "Contact", "Szeretettel várjuk üzletünkben.", "Drop by the shop – we’d love to meet you.")}
      <div class="section contact-content">
        <div class="wrap">
          <p><strong>{t("Címünk", "Address")}:</strong> <a href="{MAPS}" target="_blank" rel="noopener">Budapest III. {t("kerület", "district")}, Óbuda, Miklós utca 9.</a></p>
          <p><strong>{t("Nyitva", "Opening hours")}:</strong> {t("Hétfő–Péntek 10:30–17:00", "Mon–Fri 10:30–17:00")} | <i>{t("Egyeztetéssel 17:00–20:00", "By appointment 17:00–20:00")}</i></p>
          <p><strong>Tel:</strong> <a href="tel:+36203755366">06-20-375-5366</a></p>
          <div class="contact-grid">
            <iframe class="map" title="Google Maps" src="{EMBED}" allowfullscreen loading="lazy"></iframe>
            <figure class="shop"><img src="{pre}images/varro-uzlet.jpg" alt="{t("Felvarrjuk varróüzlet, Miklós utca 9, Óbuda", "Felvarrjuk tailoring shop, Miklós utca 9, Óbuda")}"></figure>
          </div>
        </div>
      </div>
    </section>
'''

    # Jobs
    jobs = f'''
    <section class="page-section jobs-section" id="allas">
{hero("Állás", "Jobs", "Munkatársat keresünk óbudai üzletünkbe.", "Join our team at our shop in Óbuda.")}
      <div class="section jobs-content">
        <div class="wrap">
          <p>{t("Kreatív szakmáját szerető varrónőt keresek változatos munkára.", "I’m looking for a seamstress who loves her creative craft, for varied and interesting work.")}</p>
          <p>{t("Fő profil ruhaigazítás Óbudán.", "The main focus is clothing alterations in Óbuda.")}</p>
          <p>{t("Jó kereseti lehetőséggel.", "Good earning potential.")}</p>
          <p>{t("Szakmai fényképes önéletrajzot:", "Please send your professional CV with a photo to:")} <a href="mailto:felvarrjuk@gmail.com">felvarrjuk@gmail.com</a></p>
        </div>
      </div>
    </section>
'''
    return home + services + prices + contact + jobs


def build(lang):
    global LANG
    LANG = lang
    out = PAGES[lang]["file"]
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(page(build_body()))


for lang in ("hu", "en"):
    build(lang)

# Sitemap with language alternates
alts = f'''    <xhtml:link rel="alternate" hreflang="hu" href="{SITE}/"/>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE}/en/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/"/>'''
today = date.today().isoformat()
with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>{SITE}/</loc>
    <lastmod>{today}</lastmod>
{alts}
  </url>
  <url>
    <loc>{SITE}/en/</loc>
    <lastmod>{today}</lastmod>
{alts}
  </url>
</urlset>
''')

with open("robots.txt", "w", encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")