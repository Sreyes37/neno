# -*- coding: utf-8 -*-
"""
neno_pc IPTV - Canales Abiertos y Señales Oficiales Verificadas LatAm
Streams 100% operativos alojados en CDNs estables.
"""

DEFAULT_CHANNELS = [
    # CHILE
    {
        "id": "cl_13c",
        "name": "13C Cultura & Viajes HD",
        "country": "Chile",
        "category": "Cultura",
        "url": "https://origin.dpsgo.com/ssai/event/GI-9cp_bT8KcerLpZwkuhw/master.m3u8",
        "logo": "https://i.imgur.com/Zfe2f5j.png",
        "info": "Señal cultural de Canal 13 Chile"
    },
    {
        "id": "cl_13humor",
        "name": "13 Humor & Comedia HD",
        "country": "Chile",
        "category": "Entretenimiento",
        "url": "https://origin.dpsgo.com/ssai/event/cKWySXKgSK-SzlJmESkOWw/master.m3u8",
        "logo": "https://i.imgur.com/KvMuTzN.png",
        "info": "Humor nacional y sketches clásicos de Canal 13"
    },
    {
        "id": "cl_13kids",
        "name": "13 Kids Infantil HD",
        "country": "Chile",
        "category": "Infantil",
        "url": "https://origin.dpsgo.com/ssai/event/LhHrVtyeQkKZ-Ye_xEU75g/master.m3u8",
        "logo": "https://i.imgur.com/8WJUbSD.png",
        "info": "Programación familiar y dibujos infantiles"
    },
    {
        "id": "cl_13e",
        "name": "13 Entretenimiento HD",
        "country": "Chile",
        "category": "Entretenimiento",
        "url": "https://origin.dpsgo.com/ssai/event/BBp0VeP6QtOOlH8nu3bWTg/master.m3u8",
        "logo": "https://i.imgur.com/utI1tJV.png",
        "info": "Espacios de espectáculo y entretención"
    },
    {
        "id": "cl_13festival",
        "name": "13 Festival de Viña & Música",
        "country": "Chile",
        "category": "Música",
        "url": "https://origin.dpsgo.com/ssai/event/Nftd0fM2SXasfDlRphvUsg/master.m3u8",
        "logo": "https://i.imgur.com/Ymk6j5o.png",
        "info": "Conciertos, festivales y música en vivo"
    },
    {
        "id": "cl_13t",
        "name": "13T Telenovelas & Series HD",
        "country": "Chile",
        "category": "Series",
        "url": "https://origin.dpsgo.com/ssai/event/f4TrySe8SoiGF8Lu3EIq1g/master.m3u8",
        "logo": "https://i.imgur.com/csBNi2L.png",
        "info": "Grandes producciones y series dramáticas de Canal 13"
    },
    {
        "id": "cl_13realities",
        "name": "13 Realities HD",
        "country": "Chile",
        "category": "Entretenimiento",
        "url": "https://origin.dpsgo.com/ssai/event/g7_JOM0ORki9SR5RKHe-Kw/master.m3u8",
        "logo": "https://i.imgur.com/m0SuwMU.png",
        "info": "Maratones continuas de reality shows"
    },
    # INTERNACIONAL & NOTICIAS
    {
        "id": "dw_espanol",
        "name": "Deutsche Welle (DW Español HD)",
        "country": "Internacional LatAm",
        "category": "Noticias",
        "url": "https://dwamdstream104.akamaized.net/hls/live/2015530/dwstream104/index.m3u8",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Deutsche_Welle_symbol_2012.svg/300px-Deutsche_Welle_symbol_2012.svg.png",
        "info": "Noticias mundiales en español las 24 horas"
    },
    {
        "id": "rt_doc",
        "name": "RT Documentales Español HD",
        "country": "Internacional LatAm",
        "category": "Documentales",
        "url": "https://rt-esp.rttv.com/live/rtd_es/playlist.m3u8",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/RT_logo.svg/300px-RT_logo.svg.png",
        "info": "Canal de documentales internacionales de alta producción"
    },
    {
        "id": "telefe_noticias",
        "name": "Telefe Noticias HD",
        "country": "Argentina",
        "category": "Noticias",
        "url": "https://telefe-live.cdn.vustreams.com/live/smil:telefe_noticias.smil/playlist.m3u8",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Telefe_logo_2018.png/240px-Telefe_logo_2018.png",
        "info": "Señal informativa de Telefe Argentina"
    }
]


def get_all_channels():
    return DEFAULT_CHANNELS


def get_countries(channel_list=None):
    chs = channel_list if channel_list is not None else DEFAULT_CHANNELS
    countries = list(set(ch.get("country", "Otros") for ch in chs))
    countries.sort()
    return countries


def get_channels_by_country(country_name, channel_list=None):
    chs = channel_list if channel_list is not None else DEFAULT_CHANNELS
    return [ch for ch in chs if ch.get("country") == country_name]


def get_channel_by_id(channel_id, channel_list=None):
    chs = channel_list if channel_list is not None else DEFAULT_CHANNELS
    for ch in chs:
        if ch.get("id") == channel_id:
            return ch
    return None
