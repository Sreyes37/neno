# -*- coding: utf-8 -*-
"""
Kodi Add-on: neno_pc IPTV Latino & Mundial, Zona TNT Sports HD, Cine en Español Latino 1080p & Servidores Open Source
Autor: neno_pc
Versión: 1.4.0
Compatible con Kodi 19 Matrix, 20 Nexus y 21 Omega.
Diseño y arquitectura mejorada (v1.4.0):
- Zona Especial TNT Sports & Deportes HD con Multi-Mirror y Failover Automático Inteligente (check_stream_health)
- Televisión en Español Latino de los 20 Países de Latinoamérica + Repositorios Open Source (IPTV-Org LatAm, M3U.CL, Free-TV/IPTV, TDTChannels)
- Catálogo Ampliado de Películas 1080p Full HD y 720p HD en Español Latino con enlaces directos + Explorador en Vivo (Archive.org & PeerTube)
- Selector de Servidores / Calidades funcional para TV y Películas, Verificador Multi-Mirror, Favoritos e Historial
"""

import os
import sys
import shutil
import urllib.parse
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon

from resources.lib import chile_channels
from resources.lib import premium_channels
from resources.lib import vod_and_247
from resources.lib import world_channels
from resources.lib import latam_channels
from resources.lib import open_movies
from resources.lib import favorites_manager
from resources.lib import history_manager
from resources.lib import m3u_cinema
from resources.lib import scrapers
from resources.lib import resolvers
from resources.lib import network_helper
from resources.lib import ui_helper

ADDON = xbmcaddon.Addon()
BASE_URL = sys.argv[0]
HANDLE = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else -1


def build_url(query):
    return f"{BASE_URL}?{urllib.parse.urlencode(query)}"


def add_menu_entry(label, query_params, plot, icon_file=None, is_folder=True, genre="Menú"):
    """Helper estandarizado para crear entradas de menú con diseño visual completo."""
    item = xbmcgui.ListItem(label=label)
    ui_helper.set_video_info(item, {
        "title": label,
        "plot": plot,
        "genre": genre,
        "mediatype": "video"
    })
    icon_path = ui_helper.get_media_icon(icon_file) if icon_file else ui_helper.DEFAULT_ICON
    ui_helper.set_item_art(item, icon=icon_path, thumb=icon_path, poster=icon_path)
    xbmcplugin.addDirectoryItem(
        handle=HANDLE,
        url=build_url(query_params),
        listitem=item,
        isFolder=is_folder
    )


# ==========================================
# MENÚ PRINCIPAL (ROOT)
# ==========================================
def list_root_menu():
    """Menú principal rediseñado con Zona TNT Sports HD, TV LatAm (20 países), Cine 1080p Español Latino y Servidores Open Source."""
    xbmcplugin.setPluginCategory(HANDLE, "neno_pc TV LatAm, TNT Sports & Cine 1080p")
    xbmcplugin.setContent(HANDLE, "videos")

    favs_count = len(favorites_manager.load_favorites())
    hist_count = len(history_manager.load_history())
    chile_count = len(chile_channels.get_chile_channels())
    tnt_sports_count = len(premium_channels.get_tnt_and_sports_channels())
    movies_count = len(open_movies.OPEN_MOVIES_CATALOG)
    latam_countries_count = len(latam_channels.LATAM_COUNTRIES)

    # Si el usuario activó Lista M3U Personalizada en Ajustes, mostrar acceso directo arriba
    source_mode = ADDON.getSetting("source_mode")
    if source_mode in ("1", "2"):
        add_menu_entry(
            label="[COLOR springgreen][B]📡 MI LISTA M3U ACTIVA (DESDE AJUSTES)[/B][/COLOR]",
            query_params={"mode": "load_settings_m3u"},
            plot="Reproduce directamente la lista M3U remota o archivo local que configuraste en los ajustes del add-on.",
            icon_file="icon_m3u_vod.png",
            is_folder=True
        )

    # 1. ZONA ESPECIAL: TNT SPORTS & DEPORTES EN VIVO (MULTI-SERVIDOR ESTABLE)
    add_menu_entry(
        label=f"[COLOR lime][B]⚽ ZONA TNT SPORTS & FÚTBOL EN VIVO (MULTI-MIRROR HD)[/B][/COLOR] [COLOR gray]({tnt_sports_count} señales + feed)[/COLOR]",
        query_params={"mode": "menu_tnt_sports"},
        plot="Señales estables con múltiples servidores en failover automático: TNT Sports Chile HD, TNT Sports / Pack Fútbol Argentina 1080p, TNT Sur/Andina, ESPN (1 al 7), TyC Sports, Fox Sports, Win+ Fútbol, L1 Max y FIFA+ Español.",
        icon_file="icon_categories.png"
    )

    # 2. TV LATINOAMÉRICA DE TODOS LOS PAÍSES (20 PAÍSES EN ESPAÑOL LATINO)
    add_menu_entry(
        label=f"[COLOR springgreen][B]🌎 TV LATINOAMÉRICA POR PAÍSES (ESPAÑOL LATINO)[/B][/COLOR] [COLOR gray]({latam_countries_count} países)[/COLOR]",
        query_params={"mode": "menu_latam_countries"},
        plot="Televisión en vivo en español latino de todos los países: Chile, Argentina, México, Colombia, Perú, Uruguay, Paraguay, Bolivia, Ecuador, Venezuela, Centroamérica, Caribe y señales panregionales.",
        icon_file="icon_latam.png"
    )

    # 3. TELEVISIÓN DE CHILE EN VIVO (+200 SEÑALES)
    add_menu_entry(
        label=f"[COLOR crimson][B]🇨🇱 TELEVISIÓN DE CHILE EN VIVO[/B][/COLOR] [COLOR gray]({chile_count} señales verificadas)[/COLOR]",
        query_params={"mode": "menu_chile"},
        plot="Colección completa de canales nacionales, TNT Sports Chile, deportivos, noticias, cultura y regionales de Chile con filtros por categoría y servidores de respaldo.",
        icon_file="icon_chile.png"
    )

    # 4. CANALES DESTACADOS LATAM & PANREGIONALES (HD)
    add_menu_entry(
        label="[COLOR gold][B]🔥 CANALES DESTACADOS LATAM & PANREGIONALES (HD)[/B][/COLOR]",
        query_params={"mode": "menu_premium"},
        plot="Selección rápida de canales premium en Español Latino con failover: TNT Sports, Cinecanal, TNT, Cartoon Network, Discovery Kids, Disney, ESPN, Fox Sports y Noticias 24/7.",
        icon_file="icon_latam.png"
    )

    # 5. TV LATINA POR CATEGORÍAS TEMÁTICAS
    add_menu_entry(
        label="[COLOR deepskyblue][B]📺 TV LATINA POR CATEGORÍAS (DEPORTES, CINE, NOTICIAS, KIDS)[/B][/COLOR]",
        query_params={"mode": "menu_latam_genres"},
        plot="Explora los canales de toda Latinoamérica organizados por temática: Deportes en Vivo, Cine y Series, Infantil en Español Latino, Noticias, Música y Cultura.",
        icon_file="icon_categories.png"
    )

    # 6. CINE & PELÍCULAS HD EN ESPAÑOL LATINO (1080P / 720P + COLECCIONES)
    add_menu_entry(
        label=f"[COLOR cyan][B]🎬 CINE & PELÍCULAS HD EN ESPAÑOL LATINO (1080P / 720P)[/B][/COLOR] [COLOR gray]({movies_count} títulos)[/COLOR]",
        query_params={"mode": "menu_movies"},
        plot="Películas completas dobladas al Español Latino en 1080p Full HD y 720p HD con enlace directo instantáneo, Cine Latinoamericano, Anime en Español Latino y selector de servidor.",
        icon_file="icon_movies_latino.png"
    )

    # 7. EXPLORADOR EN VIVO DE SERVIDORES OPEN SOURCE (ARCHIVE.ORG & PEERTUBE LATINO)
    add_menu_entry(
        label="[COLOR orange][B]🏛️ SERVIDORES OPEN SOURCE EN VIVO (ARCHIVE.ORG 1080P & PEERTUBE)[/B][/COLOR]",
        query_params={"mode": "menu_open_servers"},
        plot="Conecta en tiempo real con la API de servidores Open Source (Internet Archive y PeerTube Fediverse) para explorar y buscar miles de películas completas en Español Latino y Full HD.",
        icon_file="icon_archive_live.png"
    )

    # 8. REPOSITORIOS OPEN SOURCE M3U & VOD (IPTV-ORG LATAM, M3U.CL, FREE-TV, TDTCHANNELS)
    add_menu_entry(
        label="[COLOR violet][B]🍿 REPOSITORIOS OPEN SOURCE M3U & LISTAS VOD[/B][/COLOR]",
        query_params={"mode": "menu_m3u_cinema"},
        plot="Carga repositorios Open Source verificados (IPTV-Org Región LatAm, M3U.CL Chile/Argentina, Free-TV/IPTV GitHub, TDTChannels) o importa tus propias listas M3U.",
        icon_file="icon_m3u_vod.png"
    )

    # 9. CANALES 24/7 CONTINUOS
    add_menu_entry(
        label="[COLOR yellow][B]⏰ CANALES TEMÁTICOS 24/7 SIN PAUSAS[/B][/COLOR]",
        query_params={"mode": "menu_247"},
        plot="Emisiones continuas las 24 horas de dibujos animados, comedia, series, cultura y festivales.",
        icon_file="icon_247.png"
    )

    # 10. MIS FAVORITOS GUARDADOS
    add_menu_entry(
        label=f"[COLOR gold][B]⭐ MIS FAVORITOS GUARDADOS[/B][/COLOR] [COLOR gray]({favs_count} elementos)[/COLOR]",
        query_params={"mode": "menu_favorites"},
        plot="Acceso inmediato a tus canales de TV y películas guardadas con clic derecho / menú contextual.",
        icon_file="icon_favorites.png"
    )

    # 11. HISTORIAL DE REPRODUCCIÓN (VISTOS RECIENTEMENTE)
    add_menu_entry(
        label=f"[COLOR lightblue][B]🕒 HISTORIAL: VISTOS RECIENTEMENTE[/B][/COLOR] [COLOR gray]({hist_count} recientes)[/COLOR]",
        query_params={"mode": "menu_history"},
        plot="Retoma rápidamente los últimos canales en vivo y películas que has reproducido.",
        icon_file="icon_history.png"
    )

    # 12. BUSCADOR GLOBAL UNIFICADO
    add_menu_entry(
        label="[COLOR lime][B]🔍 BUSCADOR GLOBAL (TNT SPORTS + TV LATAM + CINE 1080P + ARCHIVE)[/B][/COLOR]",
        query_params={"mode": "search"},
        plot="Busca simultáneamente señales de TNT Sports/Deportes, canales de los 20 países de Latinoamérica, películas 1080p del catálogo y servidores de Internet Archive.",
        icon_file="icon_search.png"
    )

    # 13. AJUSTES Y HERRAMIENTAS
    add_menu_entry(
        label="[COLOR silver][B]⚙️ AJUSTES, LISTAS M3U & HERRAMIENTAS[/B][/COLOR]",
        query_params={"mode": "menu_tools"},
        plot="Configura listas M3U, modo de selección de servidor, limpia la caché de canales o administra tu historial.",
        icon_file="icon_settings.png"
    )

    xbmcplugin.endOfDirectory(HANDLE)


# ==========================================
# RENDERIZADOR ESTÁNDAR DE CANALES DE TV
# ==========================================
def render_channel_list(channels_list, category_title="Canales en Vivo", show_country_tag=False):
    xbmcplugin.setPluginCategory(HANDLE, category_title)
    xbmcplugin.setContent(HANDLE, "videos")
    ui_helper.apply_sort_methods(HANDLE, is_movies=False)

    fav_ids = {f.get("id") or f.get("url") for f in favorites_manager.load_favorites()}

    for ch in channels_list:
        name = ch.get("name", "Canal TV")
        cat_es = ch.get("category_es") or latam_channels.translate_category(ch.get("category", "General"))
        country = ch.get("country", "")
        is_verified = ch.get("verified", True)
        ch_id = ch.get("id", "")
        url_str = ch.get("url", "")
        backups = ch.get("backup_urls", [])

        badges = []
        if show_country_tag and country:
            flag = ch.get("flag", "")
            badges.append(f"[COLOR deepskyblue][{flag} {country}][/COLOR]".replace("[ ", "["))
        if is_verified:
            badges.append("[COLOR lime]●[/COLOR]")
        if backups:
            badges.append(f"[COLOR gold][+{len(backups)} Mirror][/COLOR]")

        prefix = " ".join(badges)
        label = f"{prefix} [COLOR white][B]{name}[/B][/COLOR] [COLOR gray]· {cat_es}[/COLOR]".strip()

        item = xbmcgui.ListItem(label=label)
        plot = ch.get("info") or ch.get("plot") or (
            f"Señal de televisión en vivo ({country or 'Latinoamérica'}).\n"
            f"Categoría: {cat_es} | Servidores de respaldo: {len(backups) + 1}\n"
            f"Idioma: Español Latino"
        )
        ui_helper.set_video_info(item, {
            "title": name,
            "genre": cat_es,
            "country": country,
            "plot": plot,
            "mediatype": "video"
        })

        logo = ch.get("logo") or ui_helper.get_media_icon("icon_latam.png")
        ui_helper.set_item_art(item, icon=logo, thumb=logo, poster=logo)

        is_fav = (ch_id and ch_id in fav_ids) or (url_str and url_str in fav_ids)
        item.addContextMenuItems(
            ui_helper.build_context_menu(BASE_URL, {
                "id": ch_id,
                "name": name,
                "url": url_str,
                "logo": ch.get("logo", ""),
                "genre": cat_es,
                "plot": plot,
                "type": "tv"
            }, is_fav=is_fav, allow_server_select=True)
        )

        item.setProperty("IsPlayable", "true")
        play_url = build_url({
            "mode": "play",
            "stream_url": url_str,
            "channel_name": name,
            "item_id": ch_id,
            "logo": ch.get("logo", "")
        })
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=play_url, listitem=item, isFolder=False)

    xbmcplugin.endOfDirectory(HANDLE)


# ==========================================
# ZONA ESPECIAL: TNT SPORTS & DEPORTES EN VIVO (MULTI-MIRROR)
# ==========================================
def list_tnt_sports_menu():
    xbmcplugin.setPluginCategory(HANDLE, "Zona TNT Sports & Deportes en Vivo HD")
    xbmcplugin.setContent(HANDLE, "videos")

    # Acceso directo al Feed Global de Deportes Open Source (IPTV-Org sports.m3u)
    add_menu_entry(
        label="[COLOR gold][B]🌐 FEED EN VIVO: TODOS LOS CANALES DEPORTIVOS OPEN SOURCE (+450 SEÑALES)[/B][/COLOR]",
        query_params={"mode": "world_cat_items", "cat_id": "sports", "name": "Deportes Open Source en Vivo"},
        plot="Explora el feed deportivo global actualizado de IPTV-Org (sports.m3u) con más de 450 señales abiertas.",
        icon_file="icon_categories.png"
    )

    # Acceso a todos los canales deportivos de los 20 países de Latinoamérica
    all_latam_sports = latam_channels.get_latam_by_genre("deportes")
    add_menu_entry(
        label=f"[COLOR deepskyblue][B]🌎 TODOS LOS CANALES DEPORTIVOS DE LATINOAMÉRICA[/B][/COLOR] [COLOR gray]({len(all_latam_sports)} señales)[/COLOR]",
        query_params={"mode": "latam_genre_items", "genre_id": "deportes", "name": "Deportes Latinoamérica"},
        plot="Listado completo de canales deportivos verificados de Chile, Argentina, México, Colombia, Perú, Paraguay y más.",
        icon_file="icon_latam.png"
    )

    # Renderizar debajo directamente las señales Multi-Mirror de TNT Sports, TNT, ESPN 1-7, TyC, Fox, Win+, L1 Max y FIFA+
    render_channel_list(
        premium_channels.get_tnt_and_sports_channels(),
        category_title="Zona TNT Sports & Deportes Multi-Servidor",
        show_country_tag=True
    )


# ==========================================
# TV LATINOAMÉRICA DE TODOS LOS PAÍSES (20 PAÍSES)
# ==========================================
def list_latam_countries_menu():
    xbmcplugin.setPluginCategory(HANDLE, "TV Latinoamérica por Países")
    xbmcplugin.setContent(HANDLE, "videos")

    # Acceso rápido a Todas las Señales Verificadas de Latinoamérica
    all_ver_count = len(latam_channels.get_all_verified_latam_channels())
    add_menu_entry(
        label=f"[COLOR gold][B]⚡ TODOS LOS CANALES VERIFICADOS DE LATINOAMÉRICA[/B][/COLOR] [COLOR gray]({all_ver_count} señales)[/COLOR]",
        query_params={"mode": "latam_all_verified"},
        plot="Listado unificado con todas las señales pre-verificadas de alta velocidad de los 20 países de Latinoamérica.",
        icon_file="icon_latam.png"
    )

    # Feed Regional Latinoamérica de IPTV-Org (regions/latam.m3u)
    add_menu_entry(
        label="[COLOR lime][B]🌎 FEED REGIONAL OPEN SOURCE LATINOAMÉRICA (IPTV-ORG LATAM.M3U)[/B][/COLOR] [COLOR gray](350+ canales)[/COLOR]",
        query_params={"mode": "latam_region_feed"},
        plot="Carga directamente el repositorio regional de Latinoamérica de IPTV-Org (regions/latam.m3u).",
        icon_file="icon_latam.png"
    )

    # Feed Global en idioma Español (IPTV-Org languages/spa.m3u)
    add_menu_entry(
        label="[COLOR cyan][B]🗣️ FEED GLOBAL: TODOS LOS CANALES EN IDIOMA ESPAÑOL[/B][/COLOR] [COLOR gray](350+ canales)[/COLOR]",
        query_params={"mode": "latam_global_spanish"},
        plot="Carga todos los canales de televisión del mundo que transmiten íntegramente en idioma español.",
        icon_file="icon_latam.png"
    )

    # Lista de los 20 países de Latinoamérica y habla hispana
    for c in latam_channels.LATAM_COUNTRIES:
        code = c["code"]
        name = c["name"]
        flag = c["flag"]
        region = c.get("region", "Latinoamérica")
        ver_count = len(latam_channels.get_verified_for_country(code))

        label = f"{flag} [COLOR white][B]{name}[/B][/COLOR] [COLOR lime]({ver_count} verificados + feed en vivo)[/COLOR] [COLOR gray][{region}][/COLOR]"
        add_menu_entry(
            label=label,
            query_params={"mode": "latam_country", "code": code, "name": name},
            plot=f"Televisión en vivo de {name} en español.\nIncluye {ver_count} señales verificadas de carga rápida más el catálogo completo actualizado del país.",
            icon_file="icon_latam.png"
        )

    # También permitir ver otros países no hispanos del mundo abajo
    add_menu_entry(
        label="[COLOR silver][B]🌐 OTROS PAÍSES DEL MUNDO (EE.UU., BRASIL, EUROPA, ASIA)[/B][/COLOR]",
        query_params={"mode": "menu_world_countries"},
        plot="Explora canales internacionales de Estados Unidos, Brasil, Francia, Italia, Alemania, Reino Unido y Japón.",
        icon_file="icon_categories.png"
    )

    xbmcplugin.endOfDirectory(HANDLE)


def list_latam_country_channels(country_code, country_name):
    if country_code == "cl":
        list_chile_menu()
        return

    include_dyn = ADDON.getSetting("include_dynamic_feeds") != "false"
    channels = latam_channels.get_country_channels_full(country_code, include_live_feed=include_dyn)
    render_channel_list(channels, category_title=f"TV en Vivo: {country_name}", show_country_tag=False)


def list_latam_genres_menu():
    xbmcplugin.setPluginCategory(HANDLE, "TV Latina por Categorías")
    xbmcplugin.setContent(HANDLE, "videos")

    for g in latam_channels.LATAM_GENRE_GROUPS:
        count = len(latam_channels.get_latam_by_genre(g["id"]))
        add_menu_entry(
            label=f"[COLOR deepskyblue][B]{g['name']}[/B][/COLOR] [COLOR gray]({count} canales latinos)[/COLOR]",
            query_params={"mode": "latam_genre_items", "genre_id": g["id"], "name": g["name"]},
            plot=f"Canales verificados de toda Latinoamérica en la categoría {g['name']}.",
            icon_file="icon_categories.png"
        )

    # Categorías globales adicionales de IPTV-Org
    for wcat in world_channels.WORLD_CATEGORIES:
        add_menu_entry(
            label=f"{wcat['icon']} [COLOR silver][B]{wcat['name']} (Feed Internacional)[/B][/COLOR]",
            query_params={"mode": "world_cat_items", "cat_id": wcat["id"], "name": wcat["name"]},
            plot=f"Catálogo internacional de canales de {wcat['name']}.",
            icon_file="icon_categories.png"
        )

    xbmcplugin.endOfDirectory(HANDLE)


# ==========================================
# CANALES DE CHILE CON FILTRO POR CATEGORÍAS
# ==========================================
def list_chile_menu(category_filter=None):
    all_chile = chile_channels.get_chile_channels()
    for ch in all_chile:
        ch["category_es"] = latam_channels.translate_category(ch.get("category", "General"))
        ch["country"] = "Chile"

    if category_filter:
        filtered = [c for c in all_chile if c.get("category_es") == category_filter]
        render_channel_list(filtered, category_title=f"Chile: {category_filter}", show_country_tag=False)
        return

    xbmcplugin.setPluginCategory(HANDLE, "Televisión de Chile en Vivo")
    xbmcplugin.setContent(HANDLE, "videos")

    # Acceso rápido arriba a Zona TNT Sports & Deportes Chile
    add_menu_entry(
        label="[COLOR lime][B]⚽ ZONA TNT SPORTS CHILE & DEPORTES EN VIVO (MULTI-MIRROR)[/B][/COLOR]",
        query_params={"mode": "menu_tnt_sports"},
        plot="Acceso directo a TNT Sports Chile HD, TNT Sports Premium, TNT Sports 2 y señales deportivas con servidores de respaldo.",
        icon_file="icon_chile.png"
    )

    # Carpetas de filtro rápido por categoría arriba
    cats = sorted(list(set(c["category_es"] for c in all_chile)))
    for cat in cats:
        c_count = sum(1 for c in all_chile if c["category_es"] == cat)
        add_menu_entry(
            label=f"📁 [COLOR gold][B]Chile - {cat}[/B][/COLOR] [COLOR gray]({c_count} canales)[/COLOR]",
            query_params={"mode": "menu_chile", "cat": cat},
            plot=f"Filtrar canales chilenos de la categoría {cat}.",
            icon_file="icon_chile.png"
        )

    render_channel_list(all_chile, category_title="Televisión de Chile", show_country_tag=False)


# ==========================================
# CINE & PELÍCULAS EN ESPAÑOL LATINO (1080P / 720P HD) + OPEN SOURCE
# ==========================================
def list_movies_menu():
    xbmcplugin.setPluginCategory(HANDLE, "Cine en Español Latino HD & Open Source")
    xbmcplugin.setContent(HANDLE, "videos")

    hd_movs = open_movies.get_hd_1080p_movies()
    latino_movs = open_movies.get_latino_only_movies()
    all_movs = open_movies.get_all_movies()

    add_menu_entry(
        label=f"[COLOR gold][B]🔥 PELÍCULAS EN 1080P & 720P FULL HD (ESPAÑOL LATINO)[/B][/COLOR] [COLOR gray]({len(hd_movs)} títulos HD)[/COLOR]",
        query_params={"mode": "movies_hd_1080p"},
        plot="Selección especial de películas en 1080p Full HD y 720p HD dobladas al Español Latino con enlace directo de alta velocidad.",
        icon_file="icon_movies_latino.png"
    )

    add_menu_entry(
        label=f"[COLOR lime][B]🇲🇽 TODAS LAS PELÍCULAS Y COLECCIONES EN ESPAÑOL LATINO[/B][/COLOR] [COLOR gray]({len(latino_movs)} títulos)[/COLOR]",
        query_params={"mode": "movies_latino_only"},
        plot="Películas completas dobladas al Español Latino, cine mexicano y series/anime en español latino listas para reproducir.",
        icon_file="icon_movies_latino.png"
    )

    add_menu_entry(
        label=f"[COLOR deepskyblue][B]🍿 CATÁLOGO COMPLETO CURADO ({len(all_movs)} TÍTULOS HD)[/B][/COLOR]",
        query_params={"mode": "movies_all"},
        plot="Todas las películas del catálogo curado en Español Latino y clásicos Open Source restaurados.",
        icon_file="icon_movies_latino.png"
    )

    add_menu_entry(
        label="[COLOR orange][B]🏛️ EXPLORAR SERVIDORES OPEN SOURCE EN VIVO (MILES DE PELÍCULAS HD)[/B][/COLOR]",
        query_params={"mode": "menu_open_servers"},
        plot="Busca y reproduce directamente desde los servidores de Internet Archive (con filtro 1080p/720p) y PeerTube en Español Latino.",
        icon_file="icon_archive_live.png"
    )

    genres = open_movies.get_movie_genres()
    for g in genres:
        movs = open_movies.get_movies_by_genre(g)
        add_menu_entry(
            label=f"🎬 [COLOR white][B]{g}[/B][/COLOR] [COLOR gray]({len(movs)} títulos)[/COLOR]",
            query_params={"mode": "movies_genre", "genre": g},
            plot=f"Explorar películas del género {g}.",
            icon_file="icon_movies_latino.png"
        )

    xbmcplugin.endOfDirectory(HANDLE)


def render_movie_items(movie_list, category_title="Películas", next_page_params=None):
    xbmcplugin.setPluginCategory(HANDLE, category_title)
    xbmcplugin.setContent(HANDLE, "movies")
    ui_helper.apply_sort_methods(HANDLE, is_movies=True)

    fav_ids = {f.get("id") or f.get("url") for f in favorites_manager.load_favorites()}

    for mov in movie_list:
        title = mov.get("title", "Película")
        year = mov.get("year", "2020")
        lang = mov.get("language", "Español Latino")
        quality = mov.get("quality", "")
        is_collection = mov.get("is_collection", False)
        mov_id = mov.get("id", "")
        url_str = mov.get("url", "")
        archive_id = mov.get("archive_id") or resolvers.ArchiveOrgResolver.extract_identifier(url_str)

        lang_badge = f"[COLOR lime][{lang}][/COLOR]" if "Latino" in lang else f"[COLOR cyan][{lang}][/COLOR]"
        q_badge = f" [COLOR gold][{quality}][/COLOR]" if quality and quality.split()[0] not in lang else ""
        label = f"{lang_badge}{q_badge} [COLOR white][B]{title}[/B][/COLOR] [COLOR gray]({year})[/COLOR]"

        item = xbmcgui.ListItem(label=label)
        plot = mov.get("plot", "Película en servidor Open Source.")
        ui_helper.set_video_info(item, {
            "title": title,
            "genre": mov.get("genre", "Cine"),
            "year": year,
            "rating": mov.get("rating", "7.5"),
            "plot": f"Idioma: {lang} | Calidad: {quality or 'HD'}\n{plot}",
            "mediatype": "movie"
        })

        poster = mov.get("poster") or ui_helper.get_media_icon("icon_movies_latino.png")
        fanart = mov.get("fanart") or ui_helper.DEFAULT_FANART
        ui_helper.set_item_art(item, icon=poster, thumb=poster, poster=poster, fanart=fanart)

        is_fav = (mov_id and mov_id in fav_ids) or (url_str and url_str in fav_ids)
        ctx = ui_helper.build_context_menu(BASE_URL, {
            "id": mov_id,
            "title": title,
            "url": url_str,
            "poster": poster,
            "genre": mov.get("genre", "Cine"),
            "plot": plot,
            "type": "movie"
        }, is_fav=is_fav, allow_server_select=True)

        if archive_id:
            explore_cmd = f"Container.Update({build_url({'mode': 'explore_archive_item', 'archive_id': archive_id, 'title': title, 'poster': poster})})"
            ctx.insert(1, ("📂 Ver Todos los Archivos / Episodios / Calidades", explore_cmd))

        item.addContextMenuItems(ctx)

        if is_collection and archive_id:
            target_url = build_url({
                "mode": "explore_archive_item",
                "archive_id": archive_id,
                "title": title,
                "poster": poster
            })
            xbmcplugin.addDirectoryItem(handle=HANDLE, url=target_url, listitem=item, isFolder=True)
        else:
            item.setProperty("IsPlayable", "true")
            target_url = build_url({
                "mode": "play",
                "item_id": mov_id,
                "stream_url": url_str,
                "channel_name": title,
                "logo": poster
            })
            xbmcplugin.addDirectoryItem(handle=HANDLE, url=target_url, listitem=item, isFolder=False)

    if next_page_params:
        next_item = xbmcgui.ListItem(label=f"[COLOR gold][B]⏩ SIGUIENTE PÁGINA (PÁGINA {next_page_params.get('page')})[/B][/COLOR]")
        ui_helper.set_item_art(next_item, icon=ui_helper.get_media_icon("icon_archive_live.png"))
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=build_url(next_page_params), listitem=next_item, isFolder=True)

    xbmcplugin.endOfDirectory(HANDLE)


# ==========================================
# EXPLORADOR EN VIVO DE SERVIDORES OPEN SOURCE (ARCHIVE.ORG & PEERTUBE)
# ==========================================
def list_open_servers_menu():
    xbmcplugin.setPluginCategory(HANDLE, "Servidores Open Source en Vivo")
    xbmcplugin.setContent(HANDLE, "videos")

    add_menu_entry(
        label="[COLOR lime][B]🔍 BUSCAR PELÍCULA EN VIVO EN ARCHIVE.ORG (ESPAÑOL LATINO)[/B][/COLOR]",
        query_params={"mode": "archive_live_search"},
        plot="Busca cualquier película, serie o clásico directamente en los servidores de Internet Archive en español latino.",
        icon_file="icon_search.png"
    )

    add_menu_entry(
        label="[COLOR cyan][B]🌐 BUSCAR EN SERVIDORES FEDERADOS PEERTUBE (ESPAÑOL)[/B][/COLOR]",
        query_params={"mode": "peertube_live_search"},
        plot="Busca películas y documentales en español alojados en la red descentralizada Open Source PeerTube.",
        icon_file="icon_archive_live.png"
    )

    for cat in open_movies.ARCHIVE_LIVE_CATEGORIES:
        add_menu_entry(
            label=f"[COLOR gold][B]{cat['name']}[/B][/COLOR]",
            query_params={"mode": "archive_live_cat", "cat_id": cat["id"], "page": "1"},
            plot=f"Explora en tiempo real el servidor de Internet Archive: {cat['name']}.",
            icon_file="icon_archive_live.png"
        )

    xbmcplugin.endOfDirectory(HANDLE)


def list_archive_live_category(cat_id, page=1):
    cat = next((c for c in open_movies.ARCHIVE_LIVE_CATEGORIES if c["id"] == cat_id), None)
    if not cat:
        return
    movies = open_movies.fetch_archive_org_live(cat["query"], page=page, rows=30)
    next_params = {"mode": "archive_live_cat", "cat_id": cat_id, "page": str(int(page) + 1)} if len(movies) >= 20 else None
    render_movie_items(movies, category_title=f"{cat['name']} (Pág. {page})", next_page_params=next_params)


def do_archive_live_search():
    keyboard = xbmc.Keyboard("", "Buscar Película en Archive.org (ej. 1080p Latino, Dragon Ball, Terror):")
    keyboard.doModal()
    if not keyboard.isConfirmed():
        return
    query = keyboard.getText().strip()
    if not query:
        return
    movies = open_movies.search_archive_org_latino(query, page=1, rows=35)
    render_movie_items(movies, category_title=f"Archive.org: {query}")


def do_peertube_live_search():
    keyboard = xbmc.Keyboard("", "Buscar en PeerTube Open Servers (Español):")
    keyboard.doModal()
    if not keyboard.isConfirmed():
        return
    query = keyboard.getText().strip()
    if not query:
        return
    movies = open_movies.search_peertube_latino(query, count=25)
    render_movie_items(movies, category_title=f"PeerTube: {query}")


def explore_archive_collection(archive_id, title, poster=""):
    """Muestra todos los archivos de video dentro de un ítem de Archive.org (episodios, películas o calidades)."""
    xbmcplugin.setPluginCategory(HANDLE, f"Archivos: {title}")
    xbmcplugin.setContent(HANDLE, "movies")

    files = resolvers.ArchiveOrgResolver.get_item_video_files(archive_id)
    if not files:
        xbmcgui.Dialog().notification("neno_pc", "No se encontraron archivos MP4/MKV en este contenedor", xbmcgui.NOTIFICATION_WARNING)
        xbmcplugin.endOfDirectory(HANDLE)
        return

    img = poster or f"https://archive.org/services/img/{archive_id}"
    for idx, f in enumerate(files, 1):
        label = f"[COLOR lime][{f['ext']} · {f['size_mb']} MB][/COLOR] [COLOR white][B]{f['name']}[/B][/COLOR] [COLOR gold]({f['quality']})[/COLOR]"
        item = xbmcgui.ListItem(label=label)
        ui_helper.set_video_info(item, {
            "title": f["name"],
            "genre": "Open Source Direct Stream",
            "plot": f"Archivo directo del servidor Internet Archive ({archive_id}).\nFormato: {f['ext']} | Tamaño: {f['size_mb']} MB | Calidad: {f['quality']}",
            "mediatype": "movie"
        })
        ui_helper.set_item_art(item, icon=img, thumb=img, poster=img)
        item.setProperty("IsPlayable", "true")
        play_url = build_url({
            "mode": "play",
            "stream_url": f["url"],
            "channel_name": f"{title} - {f['name']}",
            "logo": img
        })
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=play_url, listitem=item, isFolder=False)

    xbmcplugin.endOfDirectory(HANDLE)


# ==========================================
# SECCIÓN MIS FAVORITOS & HISTORIAL
# ==========================================
def list_favorites_menu():
    xbmcplugin.setPluginCategory(HANDLE, "Mis Favoritos Guardados")
    xbmcplugin.setContent(HANDLE, "videos")

    favs = favorites_manager.load_favorites()
    if not favs:
        add_menu_entry(
            label="[COLOR gray](No tienes canales ni películas en Favoritos aún — Usa clic derecho para guardar)[/COLOR]",
            query_params={"mode": "root"},
            plot="Abre el menú contextual (clic derecho o pulsación larga) sobre cualquier canal o película y selecciona 'Guardar en Mis Favoritos'.",
            icon_file="icon_favorites.png"
        )
        xbmcplugin.endOfDirectory(HANDLE)
        return

    for f in favs:
        title = f.get("name") or f.get("title") or "Favorito"
        label = f"[COLOR gold]⭐[/COLOR] [COLOR white][B]{title}[/B][/COLOR]"
        item = xbmcgui.ListItem(label=label)
        ui_helper.set_video_info(item, {"title": title, "plot": "Guardado en Mis Favoritos."})
        logo = f.get("logo") or f.get("poster") or ui_helper.get_media_icon("icon_favorites.png")
        ui_helper.set_item_art(item, icon=logo, thumb=logo, poster=logo)

        item.addContextMenuItems(
            ui_helper.build_context_menu(BASE_URL, {
                "id": f.get("id", ""),
                "name": title,
                "url": f.get("url", ""),
                "logo": logo,
                "type": f.get("type", "video")
            }, is_fav=True, allow_server_select=True)
        )

        item.setProperty("IsPlayable", "true")
        play_url = build_url({"mode": "play", "stream_url": f.get("url", ""), "channel_name": title, "item_id": f.get("id", ""), "logo": logo})
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=play_url, listitem=item, isFolder=False)

    xbmcplugin.endOfDirectory(HANDLE)


def list_history_menu():
    xbmcplugin.setPluginCategory(HANDLE, "Historial: Vistos Recientemente")
    xbmcplugin.setContent(HANDLE, "videos")

    history = history_manager.load_history()
    if not history:
        add_menu_entry(
            label="[COLOR gray](Tu historial de reproducción está vacío)[/COLOR]",
            query_params={"mode": "root"},
            plot="Los canales y películas que reproduzcas aparecerán automáticamente aquí.",
            icon_file="icon_history.png"
        )
        xbmcplugin.endOfDirectory(HANDLE)
        return

    add_menu_entry(
        label="[COLOR tomato][B]🗑️ BORRAR HISTORIAL DE REPRODUCCIÓN[/B][/COLOR]",
        query_params={"mode": "clear_history"},
        plot="Elimina todas las entradas del historial de vistos recientemente.",
        icon_file="icon_history.png",
        is_folder=False
    )

    for h in history:
        title = h.get("name", "Reciente")
        ts = h.get("timestamp", "")
        label = f"[COLOR lightblue]🕒[/COLOR] [COLOR white][B]{title}[/B][/COLOR] [COLOR gray]({ts})[/COLOR]"
        item = xbmcgui.ListItem(label=label)
        ui_helper.set_video_info(item, {"title": title, "plot": f"Visto el: {ts}"})
        logo = h.get("logo") or ui_helper.get_media_icon("icon_history.png")
        ui_helper.set_item_art(item, icon=logo, thumb=logo, poster=logo)

        item.setProperty("IsPlayable", "true")
        play_url = build_url({"mode": "play", "stream_url": h.get("url", ""), "channel_name": title, "item_id": h.get("id", ""), "logo": logo})
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=play_url, listitem=item, isFolder=False)

    xbmcplugin.endOfDirectory(HANDLE)


# ==========================================
# REPOSITORIOS OPEN SOURCE M3U Y LISTAS PERSONALIZADAS
# ==========================================
def list_m3u_cinema_menu():
    xbmcplugin.setPluginCategory(HANDLE, "Repositorios Open Source M3U & VOD")
    xbmcplugin.setContent(HANDLE, "videos")

    add_menu_entry(
        label="[COLOR lime][B]➕ INTRODUCIR Y GUARDAR NUEVA URL M3U[/B][/COLOR]",
        query_params={"mode": "input_m3u_url"},
        plot="Pega un enlace web (.m3u / .m3u8) para reproducir y guardarlo automáticamente en tu colección.",
        icon_file="icon_m3u_vod.png"
    )

    add_menu_entry(
        label="[COLOR springgreen][B]📂 CARGAR LISTA M3U CONFIGURADA EN AJUSTES[/B][/COLOR]",
        query_params={"mode": "load_settings_m3u"},
        plot="Carga la URL remota o el archivo local .m3u que hayas seleccionado en Ajustes del Add-on.",
        icon_file="icon_m3u_vod.png"
    )

    for saved in m3u_cinema.load_saved_m3u_lists():
        add_menu_entry(
            label=f"[COLOR gold][B]⭐ [Mi Lista] {saved['name']}[/B][/COLOR]",
            query_params={"mode": "load_m3u_movies", "url": saved["url"], "name": saved["name"]},
            plot=f"Lista M3U guardada: {saved['url']}",
            icon_file="icon_m3u_vod.png"
        )

    for l in m3u_cinema.DEFAULT_CINEMA_M3U_LISTS:
        add_menu_entry(
            label=f"[COLOR yellow][B]{l['name']}[/B][/COLOR]",
            query_params={"mode": "load_m3u_movies", "url": l["url"], "name": l["name"]},
            plot=f"Cargar catálogo Open Source desde {l['name']} ({l['url']}).",
            icon_file="icon_m3u_vod.png"
        )

    xbmcplugin.endOfDirectory(HANDLE)


def load_m3u_movies(m3u_url, category_name):
    xbmcplugin.setPluginCategory(HANDLE, category_name)
    xbmcplugin.setContent(HANDLE, "movies")
    ui_helper.apply_sort_methods(HANDLE, is_movies=False)

    movies = m3u_cinema.load_m3u_movies_from_url(m3u_url)
    for mov in movies:
        title = mov.get("title", "Elemento M3U")
        genre = mov.get("genre", "Cine")
        label = f"[COLOR deepskyblue][B]{title}[/B][/COLOR] [COLOR gray][{genre}][/COLOR]"
        item = xbmcgui.ListItem(label=label)
        ui_helper.set_video_info(item, {
            "title": title,
            "genre": genre,
            "plot": mov.get("plot", "Stream desde lista M3U")
        })
        poster = mov.get("poster") or ui_helper.get_media_icon("icon_m3u_vod.png")
        ui_helper.set_item_art(item, icon=poster, thumb=poster, poster=poster)

        item.addContextMenuItems(
            ui_helper.build_context_menu(BASE_URL, {
                "title": title,
                "url": mov["url"],
                "poster": mov.get("poster", ""),
                "genre": genre,
                "type": "movie"
            })
        )

        item.setProperty("IsPlayable", "true")
        url = build_url({"mode": "play", "stream_url": mov["url"], "channel_name": title, "logo": poster})
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=url, listitem=item, isFolder=False)

    xbmcplugin.endOfDirectory(HANDLE)


def input_custom_m3u():
    keyboard = xbmc.Keyboard("", "Introduce la URL de tu lista M3U (.m3u / .m3u8):")
    keyboard.doModal()
    if keyboard.isConfirmed():
        url = keyboard.getText().strip()
        if url:
            m3u_cinema.save_custom_m3u_list(f"Lista Personalizada ({url[:28]}...)", url)
            load_m3u_movies(url, "Mi Lista M3U")


def load_settings_m3u():
    source_mode = ADDON.getSetting("source_mode")
    m3u_file = ADDON.getSetting("m3u_file")
    m3u_url = ADDON.getSetting("m3u_url")

    target = m3u_file if (source_mode == "2" and m3u_file) else m3u_url
    if not target:
        xbmcgui.Dialog().notification("neno_pc", "Configura primero tu URL o archivo M3U en Ajustes", xbmcgui.NOTIFICATION_WARNING)
        ADDON.openSettings()
        return
    load_m3u_movies(target, "Mi Lista M3U (Ajustes)")


# ==========================================
# OTROS PAÍSES DEL MUNDO Y 24/7
# ==========================================
def list_world_countries():
    xbmcplugin.setPluginCategory(HANDLE, "Otros Países del Mundo")
    xbmcplugin.setContent(HANDLE, "videos")

    for country in world_channels.WORLD_COUNTRIES:
        add_menu_entry(
            label=f"{country['flag']} [B]{country['name']}[/B]",
            query_params={"mode": "load_country", "code": country["code"], "name": country["name"]},
            plot=f"Canales internacionales de {country['name']}.",
            icon_file="icon_categories.png"
        )

    xbmcplugin.endOfDirectory(HANDLE)


def list_country_streams(country_code, country_name):
    chs = world_channels.get_country_channels(country_code)
    for c in chs:
        c["country"] = country_name
        c["verified"] = False
    render_channel_list(chs, category_title=f"Canales: {country_name}")


def list_247_menu():
    render_channel_list(vod_and_247.CHANNELS_247, category_title="Canales Temáticos 24/7")


def list_premium_menu():
    render_channel_list(premium_channels.get_premium_channels(), category_title="Canales Destacados LatAm & España", show_country_tag=True)


# ==========================================
# BUSCADOR GLOBAL UNIFICADO
# ==========================================
def do_search():
    keyboard = xbmc.Keyboard("", "Buscar TNT Sports, Canal Latino o Película 1080p:")
    keyboard.doModal()
    if not keyboard.isConfirmed():
        return
    query = keyboard.getText().strip()
    if not query:
        return

    xbmcplugin.setPluginCategory(HANDLE, f"Resultados: {query}")
    xbmcplugin.setContent(HANDLE, "videos")

    res = scrapers.search_content(query, include_online_servers=True)

    # 1. Películas Curadas en Español Latino & Open Source
    for mov in res["movies_curated"]:
        title = mov["title"]
        lang = mov.get("language", "Español Latino")
        item = xbmcgui.ListItem(label=f"[COLOR cyan][🎬 Cine {lang}][/COLOR] [B]{title}[/B]")
        ui_helper.set_video_info(item, {"title": title, "plot": mov.get("plot", ""), "mediatype": "movie"})
        poster = mov.get("poster") or ui_helper.get_media_icon("icon_movies_latino.png")
        ui_helper.set_item_art(item, icon=poster, thumb=poster, poster=poster)
        item.setProperty("IsPlayable", "true")
        url = build_url({"mode": "play", "item_id": mov["id"], "stream_url": mov["url"], "channel_name": title, "logo": poster})
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=url, listitem=item, isFolder=False)

    # 2. Canales de TNT Sports / Deportes y 20 Países de Latinoamérica
    for ch in res["live_tv_latam"][:65]:
        country = ch.get("country", "LatAm")
        name = ch["name"]
        ch_id = ch.get("id", "")
        item = xbmcgui.ListItem(label=f"[COLOR springgreen][📺 TV {country}][/COLOR] [B]{name}[/B]")
        ui_helper.set_video_info(item, {"title": name, "genre": ch.get("category_es", "TV"), "country": country})
        logo = ch.get("logo") or ui_helper.get_media_icon("icon_latam.png")
        ui_helper.set_item_art(item, icon=logo, thumb=logo, poster=logo)
        item.setProperty("IsPlayable", "true")
        url = build_url({"mode": "play", "item_id": ch_id, "stream_url": ch["url"], "channel_name": name, "logo": logo})
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=url, listitem=item, isFolder=False)

    # 3. Resultados en vivo de Servidores Archive.org
    for amov in res["movies_archive_live"]:
        title = amov["title"]
        item = xbmcgui.ListItem(label=f"[COLOR orange][🏛️ Archive.org Open Server][/COLOR] [B]{title}[/B]")
        ui_helper.set_video_info(item, {"title": title, "plot": amov.get("plot", ""), "mediatype": "movie"})
        poster = amov.get("poster") or ui_helper.get_media_icon("icon_archive_live.png")
        ui_helper.set_item_art(item, icon=poster, thumb=poster, poster=poster)
        item.setProperty("IsPlayable", "true")
        url = build_url({"mode": "play", "stream_url": amov["url"], "channel_name": title, "logo": poster})
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=url, listitem=item, isFolder=False)

    xbmcplugin.endOfDirectory(HANDLE)


# ==========================================
# HERRAMIENTAS, DIAGNÓSTICO MULTI-MIRROR Y SELECTOR DE SERVIDOR
# ==========================================
def list_tools_menu():
    xbmcplugin.setPluginCategory(HANDLE, "Ajustes y Herramientas")
    xbmcplugin.setContent(HANDLE, "videos")

    add_menu_entry(
        label="[COLOR white][B]⚙️ ABRIR CONFIGURACIÓN DEL ADD-ON (LISTAS M3U & SERVIDORES)[/B][/COLOR]",
        query_params={"mode": "settings"},
        plot="Configura tu lista M3U remota o local, InputStream Adaptive y el comportamiento del selector de servidores.",
        icon_file="icon_settings.png",
        is_folder=False
    )

    add_menu_entry(
        label="[COLOR cyan][B]🧹 LIMPIAR CACHÉ DE CANALES Y SERVIDORES[/B][/COLOR]",
        query_params={"mode": "clear_cache"},
        plot="Borra los archivos temporales de listas M3U en caché para forzar una descarga fresca desde los servidores.",
        icon_file="icon_settings.png",
        is_folder=False
    )

    add_menu_entry(
        label="[COLOR tomato][B]🗑️ BORRAR HISTORIAL DE REPRODUCCIÓN[/B][/COLOR]",
        query_params={"mode": "clear_history"},
        plot="Limpia la lista de canales y películas vistas recientemente.",
        icon_file="icon_history.png",
        is_folder=False
    )

    xbmcplugin.endOfDirectory(HANDLE)


def clear_addon_cache():
    try:
        if os.path.exists(world_channels.CACHE_DIR):
            shutil.rmtree(world_channels.CACHE_DIR, ignore_errors=True)
            os.makedirs(world_channels.CACHE_DIR, exist_ok=True)
        xbmcgui.Dialog().notification("neno_pc", "Caché de canales actualizada correctamente", xbmcgui.NOTIFICATION_INFO)
    except Exception:
        xbmcgui.Dialog().notification("neno_pc", "Caché limpiada", xbmcgui.NOTIFICATION_INFO)


def check_signal_health(stream_url, channel_name, item_id=""):
    xbmcgui.Dialog().notification("neno_pc", f"Verificando servidores: {channel_name}...", xbmcgui.NOTIFICATION_INFO, 2000)
    sources = scrapers.get_stream_sources_for_item(stream_url=stream_url, item_id=item_id)
    if not sources:
        sources = [{"name": "Principal", "url": stream_url}]

    online_count = 0
    for s in sources[:4]:
        if network_helper.check_stream_health(s["url"], timeout=3.2):
            online_count += 1

    if online_count > 0:
        xbmcgui.Dialog().notification(
            "neno_pc",
            f"✅ ONLINE ({online_count}/{min(len(sources), 4)} servidores OK): {channel_name}",
            xbmcgui.NOTIFICATION_INFO,
            4000
        )
    else:
        xbmcgui.Dialog().notification(
            "neno_pc",
            f"⚠️ Servidor lento o requiere InputStream: {channel_name}",
            xbmcgui.NOTIFICATION_WARNING,
            4000
        )


def select_and_play_server(stream_url, channel_name, item_id=""):
    """Abre un selector interactivo con todos los servidores, mirrors y calidades disponibles."""
    target_obj = scrapers.find_any_item_by_id(item_id) if item_id else None
    sources = scrapers.get_stream_sources_for_item(item=target_obj, stream_url=stream_url, item_id=item_id)
    if not sources:
        xbmcgui.Dialog().notification("neno_pc", "No se encontraron servidores alternativos", xbmcgui.NOTIFICATION_WARNING)
        return

    labels = [f"{s['name']} — [{s['quality']}]" for s in sources]
    idx = xbmcgui.Dialog().select(f"Elegir Servidor / Mirror: {channel_name}", labels)
    if idx >= 0:
        chosen = sources[idx]
        final_url = resolvers.resolve_media_url(chosen["url"]) or chosen["url"]
        play_item = xbmcgui.ListItem(label=channel_name, path=final_url)
        ui_helper.set_video_info(play_item, {"title": channel_name, "plot": f"Reproduciendo desde {chosen['name']}"})
        xbmc.Player().play(final_url, play_item)


# ==========================================
# REPRODUCTOR ROBUSTO CON FAILOVER AUTOMÁTICO REAL Y REGISTRO EN HISTORIAL
# ==========================================
def play_stream(stream_url, channel_name, item_id="", logo=""):
    if not stream_url and not item_id:
        xbmcgui.Dialog().notification("neno_pc", "Stream no disponible", xbmcgui.NOTIFICATION_ERROR)
        return

    # Buscar el objeto completo tanto en Películas como en TNT Sports, Premium, Chile y LatAm
    target_obj = scrapers.find_any_item_by_id(item_id) if item_id else None

    # Si el usuario configuró en Ajustes "Preguntar Servidor antes de reproducir"
    if ADDON.getSetting("server_select_mode") == "1":
        sources = scrapers.get_stream_sources_for_item(item=target_obj, stream_url=stream_url, item_id=item_id)
        if len(sources) > 1:
            labels = [f"{s['name']} — [{s['quality']}]" for s in sources]
            idx = xbmcgui.Dialog().select(f"Seleccionar Servidor: {channel_name}", labels)
            if idx >= 0:
                stream_url = sources[idx]["url"]
            else:
                xbmcplugin.setResolvedUrl(HANDLE, False, listitem=xbmcgui.ListItem())
                return

    backup_urls = target_obj.get("backup_urls", []) if target_obj else []

    # Failover Inteligente en Tiempo Real: si el stream tiene mirrors de respaldo y el principal no responde,
    # conmuta automáticamente al primer servidor activo (200 OK).
    best_candidate_url = stream_url
    if backup_urls and not str(stream_url).startswith(("archive://", "peertube://")):
        best_candidate_url = network_helper.get_best_stream_url(stream_url, backup_urls, timeout=2.5)

    resolved_url = resolvers.resolve_media_url(best_candidate_url)

    if not resolved_url and backup_urls:
        for b_url in backup_urls:
            resolved_url = resolvers.resolve_media_url(b_url)
            if resolved_url:
                break

    final_url = resolved_url or best_candidate_url or stream_url

    # Guardar en el Historial de Reproducción
    history_manager.add_to_history({
        "id": item_id,
        "name": channel_name or "Stream neno_pc",
        "url": stream_url or final_url,
        "logo": logo or (target_obj.get("poster") or target_obj.get("logo") if target_obj else "")
    })

    play_item = xbmcgui.ListItem(path=final_url)
    ui_helper.set_video_info(play_item, {
        "title": channel_name or "neno_pc Player",
        "plot": "Reproducción con Failover Multi-Servidor por neno_pc"
    })

    use_isa = ADDON.getSetting("use_inputstream") != "false"
    raw_lower = final_url.split("|")[0].lower()
    if use_isa and ".m3u8" in raw_lower:
        play_item.setProperty("inputstream", "inputstream.adaptive")
        play_item.setMimeType("application/vnd.apple.mpegurl")
    elif use_isa and ".mpd" in raw_lower:
        play_item.setProperty("inputstream", "inputstream.adaptive")
        play_item.setMimeType("application/dash+xml")

    xbmcplugin.setResolvedUrl(HANDLE, True, listitem=play_item)


# ==========================================
# ROUTER PRINCIPAL
# ==========================================
def router(paramstring):
    params = dict(urllib.parse.parse_qsl(paramstring))
    mode = params.get("mode")

    if not mode or mode == "root":
        list_root_menu()
    elif mode == "menu_tnt_sports":
        list_tnt_sports_menu()
    elif mode == "menu_latam_countries":
        list_latam_countries_menu()
    elif mode == "latam_country":
        list_latam_country_channels(params.get("code", "cl"), params.get("name", "Latinoamérica"))
    elif mode == "latam_all_verified":
        render_channel_list(latam_channels.get_all_verified_latam_channels(), "Todos los Canales Verificados LatAm", show_country_tag=True)
    elif mode == "latam_region_feed":
        render_channel_list(world_channels.get_latam_region_channels(), "Feed Regional Open Source LatAm", show_country_tag=False)
    elif mode == "latam_global_spanish":
        render_channel_list(latam_channels.get_global_spanish_feed(), "Feed Global en Español", show_country_tag=False)
    elif mode == "menu_latam_genres":
        list_latam_genres_menu()
    elif mode == "latam_genre_items":
        render_channel_list(latam_channels.get_latam_by_genre(params.get("genre_id", "")), params.get("name", "Categoría LatAm"), show_country_tag=True)
    elif mode == "world_cat_items":
        render_channel_list(world_channels.get_category_channels(params.get("cat_id", "movies")), params.get("name", "Categoría"))
    elif mode == "menu_chile":
        list_chile_menu(params.get("cat"))
    elif mode == "menu_premium":
        list_premium_menu()
    elif mode == "menu_favorites":
        list_favorites_menu()
    elif mode == "menu_history":
        list_history_menu()
    elif mode == "clear_history":
        history_manager.clear_history()
        xbmc.executebuiltin("Container.Refresh")
    elif mode == "toggle_fav":
        favorites_manager.toggle_favorite(params)
        xbmc.executebuiltin("Container.Refresh")
    elif mode == "menu_m3u_cinema":
        list_m3u_cinema_menu()
    elif mode == "load_m3u_movies":
        load_m3u_movies(params.get("url"), params.get("name", "Películas M3U"))
    elif mode == "input_m3u_url":
        input_custom_m3u()
    elif mode == "load_settings_m3u":
        load_settings_m3u()
    elif mode == "menu_movies":
        list_movies_menu()
    elif mode == "movies_hd_1080p":
        render_movie_items(open_movies.get_hd_1080p_movies(), "Películas 1080p & 720p Full HD (Español Latino)")
    elif mode == "movies_latino_only":
        render_movie_items(open_movies.get_latino_only_movies(), "Cine y Series en Español Latino")
    elif mode == "movies_all":
        render_movie_items(open_movies.OPEN_MOVIES_CATALOG, "Catálogo Completo de Películas")
    elif mode == "movies_genre":
        render_movie_items(open_movies.get_movies_by_genre(params.get("genre", "")), params.get("genre", "Género"))
    elif mode == "menu_open_servers":
        list_open_servers_menu()
    elif mode == "archive_live_cat":
        list_archive_live_category(params.get("cat_id", "latino_1080p_hd"), int(params.get("page", "1")))
    elif mode == "archive_live_search":
        do_archive_live_search()
    elif mode == "peertube_live_search":
        do_peertube_live_search()
    elif mode == "explore_archive_item":
        explore_archive_collection(params.get("archive_id", ""), params.get("title", "Colección"), params.get("poster", ""))
    elif mode == "menu_247":
        list_247_menu()
    elif mode == "menu_world_countries":
        list_world_countries()
    elif mode == "load_country":
        list_country_streams(params.get("code", "cl"), params.get("name", "País"))
    elif mode == "search":
        do_search()
    elif mode == "menu_tools":
        list_tools_menu()
    elif mode == "clear_cache":
        clear_addon_cache()
    elif mode == "settings":
        ADDON.openSettings()
    elif mode == "select_server":
        select_and_play_server(params.get("stream_url", ""), params.get("channel_name", "Stream"), params.get("item_id", ""))
    elif mode == "check_signal":
        check_signal_health(params.get("stream_url", ""), params.get("channel_name", "Canal"), params.get("item_id", ""))
    elif mode == "show_item_info":
        info_txt = f"Título: {params.get('title', '')}\nCategoría: {params.get('genre', '')}\nFuente: {params.get('url', '')}\n\nSinopsis / Detalles:\n{params.get('plot', '')}"
        xbmcgui.Dialog().textviewer("Ficha Técnica — neno_pc", info_txt)
    elif mode == "play":
        play_stream(
            params.get("stream_url", ""),
            params.get("channel_name", ""),
            item_id=params.get("item_id", ""),
            logo=params.get("logo", "")
        )


if __name__ == "__main__":
    if len(sys.argv) > 2:
        router(sys.argv[2][1:])
    else:
        router("")
