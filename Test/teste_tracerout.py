sites_conhecidos = [
    # --- Américas ---
    # EUA
    "google.com",
    "youtube.com",
    "facebook.com",
    "amazon.com",
    "wikipedia.org",
    "twitter.com",
    "instagram.com",
    "linkedin.com",
    "netflix.com",
    "microsoft.com",
    "apple.com",
    "ebay.com",
    "reddit.com",
    "pinterest.com",
    "nytimes.com",
    "cnn.com",
    "weather.com",
    "salesforce.com",
    "adobe.com",
    # Canadá
    "cbc.ca",
    "ctvnews.ca",
    "shopify.com",
    "canada.ca",
    # Brasil
    "uol.com.br",
    "globo.com",
    "mercadolivre.com.br",
    "g1.globo.com",
    "itau.com.br",
    # Argentina
    "clarin.com",
    "lanacion.com.ar",
    # México
    "unam.mx",
    "gob.mx",
    "eltiempo.es",

    # --- Europa ---
    # Reino Unido
    "bbc.com",
    "theguardian.com",
    "dailymail.co.uk",
    # Alemanha
    "spiegel.de",
    "bild.de",
    "t-online.de",
    "sap.com",
    # França
    "lemonde.fr",
    "lefigaro.fr",
    "radiofrance.fr",
    "orange.fr",
    # Espanha
    "elpais.com",
    "marca.com",
    "rtve.es",
    # Itália
    "corriere.it",
    "repubblica.it",
    "rai.it",
    # Holanda
    "marktplaats.nl",
    "nu.nl",
    # Suécia
    "ikea.com",
    "aftonbladet.se",
    # Suíça
    "sbb.ch",
    "admin.ch",
    # Rússia
    "yandex.ru",
    "vk.com",
    "mail.ru",

    # --- Ásia ---
    # China
    "baidu.com",
    "qq.com",
    "taobao.com",
    "jd.com",
    "weibo.com",
    "alibaba.com",
    "xinhuanet.com",
    # Japão
    "yahoo.co.jp",
    "rakuten.co.jp",
    "goo.ne.jp",
    "sony.com",
    "toyota.com",
    # Índia
    "google.co.in",
    "timesofindia.indiatimes.com",
    "flipkart.com",
    "hotstar.com",
    # Coreia do Sul
    "naver.com",
    "samsung.com",
    "daum.net",
    # Indonésia
    "kompas.com",
    "tokopedia.com",
    # Turquia
    "hurriyet.com.tr",
    "sahibinden.com",
    # Arábia Saudita
    "arabnews.com",
    # Emirados Árabes Unidos
    "khaleejtimes.com",
    "emirates.com",

    # --- Oceania ---
    # Austrália
    "abc.net.au",
    "news.com.au",
    "smh.com.au",
    "seek.com.au",
    # Nova Zelândia
    "stuff.co.nz",
    "nzherald.co.nz",

    # --- África ---
    # África do Sul
    "news24.com",
    "iol.co.za",
    # Nigéria
    "punchng.com",
    "vanguardngr.com",
    "jumia.com.ng",
    # Quênia
    "nation.africa",
    "standardmedia.co.ke",
    # Egito
    "ahram.org.eg",
    "youm7.com"
]

# Para verificar a quantidade:
print(f"Total de sites na lista: {len(sites_conhecidos)}")

# traceroute ->      tracert {endereço obtido do vetor}
# dns ->             nslookup {endereço obtido do vetor}
# dns_reverso ->     nslookup {endereco_ip obtido acima}
# ip geo location -> Invoke-RestMethod -Uri "http://ip-api.com/json/{endereco_ip obtido acima}"