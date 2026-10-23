# -*- coding: utf-8 -*-
"""
neno_pc Global Feed Manager - Motor de Carga Dinámica de Canales Mundiales y Regionales Open Source
Descarga y cachea listas M3U por país, región y categoría (IPTV-Org, M3U.CL, Free-TV/IPTV y TDTChannels)
con soporte automático de directivas #EXTVLCOPT (User-Agent y Referer) para máxima estabilidad en Kodi.
"""

import os
import re
import time
import urllib.request
import urllib.parse
from resources.lib import network_helper

CACHE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
if not os.path.exists(CACHE_DIR):
    try:
        os.makedirs(CACHE_DIR)
    except Exception:
        pass

CACHE_TTL_SECONDS = 3600 * 12  # 12 Horas de caché local para velocidad instantánea

WORLD_COUNTRIES = [
    {"code": "cl", "name": "Chile", "flag": "🇨🇱"},
    {"code": "ar", "name": "Argentina", "flag": "🇦🇷"},
    {"code": "mx", "name": "México", "flag": "🇲🇽"},
    {"code": "co", "name": "Colombia", "flag": "🇨🇴"},
    {"code": "pe", "name": "Perú", "flag": "🇵🇪"},
    {"code": "es", "name": "España", "flag": "🇪🇸"},
    {"code": "us", "name": "Estados Unidos", "flag": "🇺🇸"},
    {"code": "br", "name": "Brasil", "flag": "🇧🇷"},
    {"code": "uy", "name": "Uruguay", "flag": "🇺🇾"},
    {"code": "ve", "name": "Venezuela", "flag": "🇻🇪"},
    {"code": "ec", "name": "Ecuador", "flag": "🇪🇨"},
    {"code": "bo", "name": "Bolivia", "flag": "🇧🇴"},
    {"code": "py", "name": "Paraguay", "flag": "🇵🇾"},
    {"code": "fr", "name": "Francia", "flag": "🇫🇷"},
    {"code": "it", "name": "Italia", "flag": "🇮🇹"},
    {"code": "de", "name": "Alemania", "flag": "🇩🇪"},
    {"code": "gb", "name": "Reino Unido", "flag": "🇬🇧"},
    {"code": "jp", "name": "Japón", "flag": "🇯🇵"}
]

WORLD_CATEGORIES = [
    {"id": "sports", "name": "Deportes Mundiales & Eventos en Vivo", "icon": "⚽", "url": "https://iptv-org.github.io/iptv/categories/sports.m3u"},
    {"id": "movies", "name": "Cine & Películas 24/7", "icon": "🎬", "url": "https://iptv-org.github.io/iptv/categories/movies.m3u"},
    {"id": "animation", "name": "Animación, Dibujos & Anime", "icon": "🧸", "url": "https://iptv-org.github.io/iptv/categories/animation.m3u"},
    {"id": "comedy", "name": "Comedia & Humor", "icon": "😂", "url": "https://iptv-org.github.io/iptv/categories/comedy.m3u"},
    {"id": "documentary", "name": "Documentales & Naturaleza", "icon": "🌍", "url": "https://iptv-org.github.io/iptv/categories/documentary.m3u"},
    {"id": "music", "name": "Música & Conciertos", "icon": "🎵", "url": "https://iptv-org.github.io/iptv/categories/music.m3u"},
    {"id": "news", "name": "Noticias Internacionales", "icon": "📡", "url": "https://iptv-org.github.io/iptv/categories/news.m3u"},
    {"id": "entertainment", "name": "Entretenimiento & Series", "icon": "🌟", "url": "https://iptv-org.github.io/iptv/categories/entertainment.m3u"},
    {"id": "kids", "name": "Infantil & Familia", "icon": "👶", "url": "https://iptv-org.github.io/iptv/categories/kids.m3u"}
]


def fetch_url(url, cache_filename):
    """Descarga con cache en disco para que Kodi no se quede esperando."""
    cache_path = os.path.join(CACHE_DIR, cache_filename)
    now = time.time()

    if os.path.exists(cache_path):
        if (now - os.path.getmtime(cache_path)) < CACHE_TTL_SECONDS:
            try:
                with open(cache_path, "r", encoding="utf-8", errors="ignore") as f:
                    return f.read()
            except Exception:
                pass

    headers = {"User-Agent": network_helper.DEFAULT_USER_AGENT}
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8, context=network_helper.UNVERIFIED_SSL_CONTEXT) as response:
            content = response.read().decode("utf-8", errors="ignore")
            with open(cache_path, "w", encoding="utf-8", errors="ignore") as f:
                f.write(content)
            return content
    except Exception:
        if os.path.exists(cache_path):
            with open(cache_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
        return ""


def parse_m3u_text(m3u_text, max_items=300):
    """
    Parsea el contenido M3U extrayendo nombres, logos, categorías y opciones #EXTVLCOPT
    (http-user-agent, http-referrer) para máxima estabilidad de reproducción en Kodi.
    """
    channels = []
    current_name = "Canal"
    current_logo = ""
    current_group = ""
    current_ua = None
    current_ref = None

    lines = m3u_text.splitlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("#EXTINF"):
            logo_m = re.search(r'tvg-logo="([^"]+)"', line)
            current_logo = logo_m.group(1) if logo_m else ""
            group_m = re.search(r'group-title="([^"]+)"', line)
            current_group = group_m.group(1) if group_m else ""
            parts = line.split(",")
            current_name = parts[-1].strip() if len(parts) > 1 else "Canal"
        elif line.startswith("#EXTVLCOPT:"):
            opt = line.split(":", 1)[1].strip()
            if opt.lower().startswith("http-user-agent="):
                current_ua = opt.split("=", 1)[1].strip()
            elif opt.lower().startswith("http-referrer=") or opt.lower().startswith("http-referer="):
                current_ref = opt.split("=", 1)[1].strip()
        elif line.startswith("http://") or line.startswith("https://"):
            final_url = line
            if (current_ua or current_ref) and "|" not in final_url:
                final_url = network_helper.prepare_kodi_stream_url(
                    final_url,
                    referer=current_ref,
                    user_agent=current_ua
                )
            channels.append({
                "name": current_name,
                "url": final_url,
                "logo": current_logo,
                "category": current_group or "General"
            })
            if len(channels) >= max_items:
                break
            current_name = "Canal"
            current_logo = ""
            current_group = ""
            current_ua = None
            current_ref = None

    return channels


def get_country_channels(country_code, max_items=250):
    url = f"https://iptv-org.github.io/iptv/countries/{country_code}.m3u"
    text = fetch_url(url, f"country_{country_code}.m3u")
    items = parse_m3u_text(text, max_items=max_items)
    # Complementar con M3U.CL para Chile y Argentina si aplica
    if country_code in ("cl", "ar") and len(items) < max_items:
        m3ucl_url = f"https://www.m3u.cl/lista/{country_code.upper()}.m3u"
        extra_text = fetch_url(m3ucl_url, f"m3ucl_{country_code}.m3u")
        extra_items = parse_m3u_text(extra_text, max_items=max_items - len(items))
        seen = {c["url"].split("|")[0] for c in items}
        for ex in extra_items:
            if ex["url"].split("|")[0] not in seen:
                items.append(ex)
    return items


def get_latam_region_channels(max_items=350):
    """Descarga el feed regional unificado de Latinoamérica de IPTV-Org (regions/latam.m3u)."""
    url = "https://iptv-org.github.io/iptv/regions/latam.m3u"
    text = fetch_url(url, "region_latam.m3u")
    return parse_m3u_text(text, max_items=max_items)


def get_category_channels(category_id, max_items=250):
    url = f"https://iptv-org.github.io/iptv/categories/{category_id}.m3u"
    text = fetch_url(url, f"cat_{category_id}.m3u")
    return parse_m3u_text(text, max_items=max_items)
