# -*- coding: utf-8 -*-
"""
neno_pc UI & Kodi Skin Helper (Kodi 19 Matrix / 20 Nexus / 21 Omega)
Motor de diseño visual para Kodi:
- Soporte nativo para InfoTagVideo (Kodi 20/21) con fallback automático a setInfo (Kodi 19)
- Propagación de Fanart HD, Posters, Banners e Iconos personalizados
- Construcción de etiquetas enriquecidas con insignias de idioma, calidad y servidor
- Menús contextuales avanzados (Favoritos, Selector de Servidor, Test de Señal, Ficha Técnica)
"""

import os
import urllib.parse
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon

ADDON = xbmcaddon.Addon()
ADDON_PATH = ADDON.getAddonInfo("path")
DEFAULT_ICON = os.path.join(ADDON_PATH, "icon.png")
DEFAULT_FANART = os.path.join(ADDON_PATH, "fanart.jpg")
MEDIA_DIR = os.path.join(ADDON_PATH, "resources", "media")


def get_media_icon(filename):
    """Devuelve la ruta absoluta de un icono temático en resources/media/ o el icono principal."""
    if not filename:
        return DEFAULT_ICON
    candidate = os.path.join(MEDIA_DIR, filename)
    if os.path.exists(candidate):
        return candidate
    return DEFAULT_ICON


def set_video_info(listitem, info_dict):
    """
    Aplica metadatos de video usando la API moderna InfoTagVideo (Kodi 20/21)
    con respaldo compatible para Kodi 19.
    """
    title = str(info_dict.get("title") or "")
    plot = str(info_dict.get("plot") or "")
    genre = info_dict.get("genre") or "General"
    year = info_dict.get("year")
    rating = info_dict.get("rating")
    country = info_dict.get("country") or ""
    studio = info_dict.get("studio") or "neno_pc Open Stream"
    mediatype = info_dict.get("mediatype") or "video"

    year_int = 0
    if year and str(year).isdigit():
        year_int = int(year)

    rating_float = 0.0
    if rating:
        try:
            rating_float = float(rating)
        except Exception:
            rating_float = 0.0

    try:
        vtag = listitem.getVideoInfoTag()
        if title:
            vtag.setTitle(title)
        if plot:
            vtag.setPlot(plot)
            vtag.setPlotOutline(plot[:160])
        if genre:
            genres = [g.strip() for g in str(genre).replace(";", "/").split("/") if g.strip()]
            vtag.setGenres(genres)
        if year_int > 0:
            vtag.setYear(year_int)
        if rating_float > 0:
            vtag.setRating(rating_float)
        if country:
            vtag.setCountries([country])
        if studio:
            vtag.setStudios([studio])
        if mediatype:
            vtag.setMediaType(mediatype)
    except AttributeError:
        legacy_info = {
            "title": title,
            "plot": plot,
            "genre": str(genre),
            "studio": studio,
            "mediatype": mediatype
        }
        if year_int > 0:
            legacy_info["year"] = year_int
        if rating_float > 0:
            legacy_info["rating"] = rating_float
        if country:
            legacy_info["country"] = country
        listitem.setInfo("video", legacy_info)


def set_item_art(listitem, icon=None, thumb=None, poster=None, fanart=None, banner=None):
    """Configura el arte visual completo para vistas de Póster, Muro, Fanart y Lista en Kodi."""
    resolved_icon = icon or poster or thumb or DEFAULT_ICON
    resolved_thumb = thumb or poster or icon or DEFAULT_ICON
    resolved_poster = poster or thumb or icon or DEFAULT_ICON
    resolved_fanart = fanart or DEFAULT_FANART

    art = {
        "icon": resolved_icon,
        "thumb": resolved_thumb,
        "poster": resolved_poster,
        "fanart": resolved_fanart,
        "landscape": resolved_fanart
    }
    if banner:
        art["banner"] = banner
    listitem.setArt(art)


def apply_sort_methods(handle, is_movies=False):
    """Agrega métodos de ordenación en la interfaz de Kodi."""
    if handle < 0:
        return
    xbmcplugin.addSortMethod(handle, xbmcplugin.SORT_METHOD_UNSORTED)
    xbmcplugin.addSortMethod(handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    if is_movies:
        xbmcplugin.addSortMethod(handle, xbmcplugin.SORT_METHOD_VIDEO_YEAR)
        xbmcplugin.addSortMethod(handle, xbmcplugin.SORT_METHOD_VIDEO_RATING)
        xbmcplugin.addSortMethod(handle, xbmcplugin.SORT_METHOD_GENRE)


def build_context_menu(base_url, item_data, is_fav=False, allow_server_select=True):
    """Construye un menú contextual enriquecido (clic derecho / tecla C / pulsación larga)."""
    def _url(q):
        return f"{base_url}?{urllib.parse.urlencode(q)}"

    ctx = []
    item_id = item_data.get("id", "")
    name = item_data.get("name") or item_data.get("title") or "Elemento"
    stream_url = item_data.get("url", "")
    logo = item_data.get("logo") or item_data.get("poster") or ""
    item_type = item_data.get("type", "video")

    fav_label = "❌ Quitar de Mis Favoritos" if is_fav else "⭐ Guardar en Mis Favoritos"
    fav_cmd = f"RunPlugin({_url({'mode': 'toggle_fav', 'id': item_id, 'name': name, 'url': stream_url, 'logo': logo, 'type': item_type})})"
    ctx.append((fav_label, fav_cmd))

    if allow_server_select and (stream_url or item_id):
        sel_cmd = f"RunPlugin({_url({'mode': 'select_server', 'item_id': item_id, 'stream_url': stream_url, 'channel_name': name})})"
        ctx.append(("🔄 Elegir Servidor / Fuente", sel_cmd))

        ping_cmd = f"RunPlugin({_url({'mode': 'check_signal', 'stream_url': stream_url, 'channel_name': name, 'item_id': item_id})})"
        ctx.append(("🩺 Verificar Estado de Señal", ping_cmd))

    info_cmd = f"RunPlugin({_url({'mode': 'show_item_info', 'title': name, 'genre': item_data.get('genre') or item_data.get('category', ''), 'plot': (item_data.get('plot') or '')[:350], 'url': stream_url})})"
    ctx.append(("ℹ️ Ver Ficha Técnica", info_cmd))

    return ctx
