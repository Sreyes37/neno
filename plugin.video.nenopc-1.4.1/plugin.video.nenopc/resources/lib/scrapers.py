# -*- coding: utf-8 -*-
"""
neno_pc Scrapers, Multi-Mirror Lookup & Unified Search Engine (v1.4.0)
Permite buscar películas HD en Español Latino, servidores Open Source (Archive.org y PeerTube),
señales multi-servidor de TNT Sports / Deportes HD y canales de los 20 países de Latinoamérica,
además de construir la lista completa de servidores/calidades para failover y selección manual.
"""

from resources.lib import vod_and_247
from resources.lib import open_movies
from resources.lib import latam_channels
from resources.lib import premium_channels
from resources.lib import resolvers


def find_any_item_by_id(item_id):
    """
    Busca cualquier película, canal de TNT Sports/Deportes, canal de Chile o canal LatAm
    por su identificador para recuperar sus servidores de respaldo (backup_urls).
    """
    if not item_id:
        return None
    return (
        open_movies.find_movie_by_id(item_id)
        or premium_channels.find_premium_channel_by_id(item_id)
        or latam_channels.find_channel_by_id(item_id)
        or vod_and_247.find_stream_by_id(item_id)
    )


def search_content(query, include_online_servers=True):
    """
    Motor de búsqueda global unificada:
    - Películas Curadas en Español Latino & Open Source (1080p / 720p HD)
    - Zona TNT Sports & Deportes HD + Televisión de los 20 Países de Latinoamérica
    - Servidores en Vivo Archive.org (Español Latino)
    - Canales 24/7
    """
    q = (query or "").lower().strip()
    results = {
        "movies_curated": [],
        "movies_archive_live": [],
        "live_tv_latam": [],
        "channels_247": []
    }

    if not q:
        return results

    # 1. Películas del catálogo curado (Español Latino 1080p/720p & Open Source)
    for mov in open_movies.OPEN_MOVIES_CATALOG:
        haystack = f"{mov.get('title', '')} {mov.get('genre', '')} {mov.get('plot', '')} {mov.get('language', '')}".lower()
        if q in haystack:
            results["movies_curated"].append(mov)

    # 2. Señales Multi-Mirror de TNT Sports & Deportes HD + 20 países de Latinoamérica
    seen_tv_urls = set()
    for sch in premium_channels.TNT_AND_SPORTS_CHANNELS:
        haystack = f"{sch.get('name', '')} {sch.get('country', '')} {sch.get('category', '')} {sch.get('info', '')}".lower()
        if q in haystack:
            u = sch.get("url", "")
            if u not in seen_tv_urls:
                seen_tv_urls.add(u)
                results["live_tv_latam"].append(sch)

    for ch in latam_channels.get_all_verified_latam_channels():
        haystack = f"{ch.get('name', '')} {ch.get('country', '')} {ch.get('category', '')} {ch.get('category_es', '')}".lower()
        if q in haystack:
            u = ch.get("url", "")
            if u not in seen_tv_urls:
                seen_tv_urls.add(u)
                results["live_tv_latam"].append(ch)

    # 3. Canales 24/7
    for ch247 in vod_and_247.CHANNELS_247:
        haystack = f"{ch247.get('name', '')} {ch247.get('category', '')}".lower()
        if q in haystack:
            results["channels_247"].append(ch247)

    # 4. Servidores Open Source en vivo (Archive.org)
    if include_online_servers:
        results["movies_archive_live"] = open_movies.search_archive_org_latino(q, page=1, rows=20)

    return results


def get_stream_sources_for_item(item=None, stream_url="", item_id=""):
    """
    Retorna la lista de servidores y calidades disponibles para una película o canal de TV
    (incluyendo todos los mirrors de TNT Sports/Deportes y calidades de Archive.org).
    """
    sources = []
    seen = set()

    if not item and item_id:
        item = find_any_item_by_id(item_id)

    primary = stream_url or (item.get("url", "") if item else "")
    backups = list(item.get("backup_urls", [])) if item else []

    # Si es un identificador de Archive.org, extraer todas las calidades/archivos reales del servidor
    archive_id = None
    if item and item.get("archive_id"):
        archive_id = item.get("archive_id")
    elif primary.startswith("archive://"):
        archive_id = resolvers.ArchiveOrgResolver.extract_identifier(primary)
    else:
        for b in backups:
            if b.startswith("archive://"):
                archive_id = resolvers.ArchiveOrgResolver.extract_identifier(b)
                break

    if primary and not primary.startswith("archive://"):
        srv_name = resolvers.detect_server_name(primary)
        q_label = (item.get("quality") if item and item.get("quality") else "Principal HD")
        sources.append({
            "name": f"⚡ Servidor 1: {srv_name}",
            "url": primary,
            "quality": q_label
        })
        seen.add(primary)

    if archive_id:
        archive_files = resolvers.ArchiveOrgResolver.get_item_video_files(archive_id)
        for idx, af in enumerate(archive_files[:8], 1):
            f_url = af["url"]
            if f_url not in seen:
                seen.add(f_url)
                sources.append({
                    "name": f"🏛️ Archive.org Open Server #{idx} [{af['ext']} · {af['size_mb']} MB]",
                    "url": f_url,
                    "quality": af["quality"]
                })

    for idx, b_url in enumerate(backups, 2):
        if b_url and not b_url.startswith("archive://") and b_url not in seen:
            seen.add(b_url)
            srv_name = resolvers.detect_server_name(b_url)
            sources.append({
                "name": f"🔄 Servidor Mirror #{idx}: {srv_name}",
                "url": b_url,
                "quality": "Mirror Activo HD"
            })

    if not sources and primary:
        sources.append({
            "name": "⚡ Servidor Principal Directo",
            "url": primary,
            "quality": "Automático HD"
        })

    return sources
