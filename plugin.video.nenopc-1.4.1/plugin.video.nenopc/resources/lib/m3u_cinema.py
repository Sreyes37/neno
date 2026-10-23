# -*- coding: utf-8 -*-
"""
neno_pc M3U Cinema & Open Source Playlist Importer
Permite cargar películas, deportes y televisión directamente a través de repositorios Open Source
(IPTV-Org LatAm, Free-TV/IPTV GitHub, M3U.CL, TDTChannels) o listas M3U remotas/locales del usuario,
con soporte nativo de cabeceras #EXTVLCOPT (User-Agent y Referer).
"""

import os
import re
import json
import urllib.request
import xbmc
import xbmcgui
import xbmcaddon
import xbmcvfs
from resources.lib import network_helper

ADDON = xbmcaddon.Addon()
try:
    PROFILE_DIR = xbmcvfs.translatePath(ADDON.getAddonInfo("profile"))
except AttributeError:
    PROFILE_DIR = xbmc.translatePath(ADDON.getAddonInfo("profile"))

if not os.path.exists(PROFILE_DIR):
    try:
        os.makedirs(PROFILE_DIR)
    except Exception:
        pass

CUSTOM_LISTS_FILE = os.path.join(PROFILE_DIR, "saved_m3u_lists.json")

# Repositorios Open Source M3U verificados en Internet
DEFAULT_CINEMA_M3U_LISTS = [
    {
        "name": "🌎 IPTV-Org Región Latinoamérica Completa (Open Source · +2500 Canales)",
        "url": "https://iptv-org.github.io/iptv/regions/latam.m3u"
    },
    {
        "name": "⚽ IPTV-Org Deportes & Fútbol en Vivo (Open Source · +450 Señales)",
        "url": "https://iptv-org.github.io/iptv/categories/sports.m3u"
    },
    {
        "name": "🇨🇱 M3U.CL Comunidad Open Source Chile (Canales Nacionales & Regionales)",
        "url": "https://www.m3u.cl/lista/CL.m3u"
    },
    {
        "name": "🇦🇷 M3U.CL Comunidad Open Source Argentina (Canales Nacionales & Interior)",
        "url": "https://www.m3u.cl/lista/AR.m3u"
    },
    {
        "name": "🌐 Free-TV/IPTV GitHub Open Source (Televisión Abierta Mundial HD)",
        "url": "https://raw.githubusercontent.com/Free-TV/IPTV/master/playlist.m3u8"
    },
    {
        "name": "🇪🇸 TDTChannels Open Source (TV Abierta en Español & Deportes)",
        "url": "https://www.tdtchannels.com/lists/tv.m3u8"
    },
    {
        "name": "🇲🇽 Televisión y Cine en Idioma Español (Feed Global Hispano)",
        "url": "https://iptv-org.github.io/iptv/languages/spa.m3u"
    },
    {
        "name": "🎬 Canales de Cine & Películas IPTV-Org (Mundial 24/7)",
        "url": "https://iptv-org.github.io/iptv/categories/movies.m3u"
    },
    {
        "name": "📺 Series & Entretenimiento Continuo",
        "url": "https://iptv-org.github.io/iptv/categories/series.m3u"
    },
    {
        "name": "🧸 Animación, Caricaturas & Cine Infantil",
        "url": "https://iptv-org.github.io/iptv/categories/animation.m3u"
    },
    {
        "name": "😂 Comedia, Humor & Películas Familiares",
        "url": "https://iptv-org.github.io/iptv/categories/comedy.m3u"
    },
    {
        "name": "🌍 Cine Documental, Ciencia & Naturaleza",
        "url": "https://iptv-org.github.io/iptv/categories/documentary.m3u"
    }
]


def load_saved_m3u_lists():
    if not os.path.exists(CUSTOM_LISTS_FILE):
        return []
    try:
        with open(CUSTOM_LISTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_custom_m3u_list(name, url):
    lists = load_saved_m3u_lists()
    for l in lists:
        if l.get("url") == url:
            return
    lists.insert(0, {"name": name, "url": url})
    try:
        with open(CUSTOM_LISTS_FILE, "w", encoding="utf-8") as f:
            json.dump(lists[:25], f, indent=2, ensure_ascii=False)
    except Exception:
        pass


def parse_m3u_content(content, max_items=500):
    """Parsea texto M3U extrayendo títulos, carátulas, géneros, cabeceras #EXTVLCOPT y enlaces."""
    movies = []
    if not content:
        return movies

    current_title = "Película / Canal"
    current_logo = ""
    current_group = "Cine / TV"
    current_ua = None
    current_ref = None

    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("#EXTINF"):
            logo_m = re.search(r'tvg-logo="([^"]+)"', line)
            current_logo = logo_m.group(1) if logo_m else ""
            group_m = re.search(r'group-title="([^"]+)"', line)
            current_group = group_m.group(1) if group_m else "Cine / TV"
            parts = line.split(",")
            current_title = parts[-1].strip() if len(parts) > 1 else "Película / Canal"
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
            movies.append({
                "title": current_title,
                "url": final_url,
                "poster": current_logo,
                "genre": current_group,
                "plot": f"Transmitido desde repositorio Open Source M3U ({current_group})"
            })
            if len(movies) >= max_items:
                break
            current_title = "Película / Canal"
            current_logo = ""
            current_group = "Cine / TV"
            current_ua = None
            current_ref = None

    return movies


def load_m3u_movies_from_url(url, max_items=500):
    """Descarga y procesa un archivo M3U remoto o local extrayendo películas y streams."""
    if not url:
        return []

    try:
        if os.path.exists(url):
            with open(url, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            return parse_m3u_content(content, max_items=max_items)

        req = urllib.request.Request(
            url,
            headers={"User-Agent": network_helper.DEFAULT_USER_AGENT}
        )
        with urllib.request.urlopen(req, timeout=10, context=network_helper.UNVERIFIED_SSL_CONTEXT) as response:
            content = response.read().decode("utf-8", errors="ignore")
        return parse_m3u_content(content, max_items=max_items)
    except Exception as e:
        xbmcgui.Dialog().notification(
            "neno_pc",
            f"Error cargando lista M3U: {str(e)[:30]}",
            xbmcgui.NOTIFICATION_ERROR
        )
        return []
