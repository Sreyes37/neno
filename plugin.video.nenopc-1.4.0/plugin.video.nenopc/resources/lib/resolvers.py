# -*- coding: utf-8 -*-
"""
neno_pc Core - Resolvedor Modular Multi-Servidor Open Source & IPTV (Kodi 19/20/21)
Soporta:
- Internet Archive API (archive://ID, /details/ID y /download/ directo con detección real de resolución 1080p/720p)
- PeerTube Open Source Instances (API /api/v1/videos/ para HLS adaptativo y WebVideo MP4 1080p/720p)
- Wikimedia Commons Open Media Server
- StreamWish / FileLions / WishFast / VidGuard (con desempaquetador JS Dean Edwards)
- Doodstream / Ok.ru / Voe / Direct HLS (.m3u8) y MPEG-DASH (.mpd)
"""

import re
import json
import urllib.request
import urllib.parse
from resources.lib import network_helper
from resources.lib import streamwish_resolver


class BaseServerResolver:
    """Clase base para resolutores de servidores."""
    name = "Servidor Directo / Universal"

    @classmethod
    def can_resolve(cls, url):
        return True

    @classmethod
    def resolve(cls, url):
        return network_helper.prepare_kodi_stream_url(url)


class ArchiveOrgResolver(BaseServerResolver):
    name = "Internet Archive Open Server"

    @classmethod
    def can_resolve(cls, url):
        if not url:
            return False
        u = url.lower()
        return u.startswith("archive://") or "archive.org/" in u

    @classmethod
    def extract_identifier(cls, url):
        if not url:
            return None
        if url.startswith("archive://"):
            return url.replace("archive://", "").strip("/")
        m = re.search(r"archive\.org/(?:details|metadata|download)/([^/?#]+)", url)
        if m:
            return m.group(1)
        return None

    @classmethod
    def get_item_video_files(cls, identifier):
        """
        Consulta la API abierta de Internet Archive (https://archive.org/metadata/<id>)
        y devuelve todos los archivos de video disponibles ordenados por resolución HD real.
        """
        if not identifier:
            return []
        api_url = f"https://archive.org/metadata/{urllib.parse.quote(identifier)}"
        try:
            req = urllib.request.Request(
                api_url,
                headers={"User-Agent": network_helper.DEFAULT_USER_AGENT}
            )
            with urllib.request.urlopen(req, timeout=8, context=network_helper.UNVERIFIED_SSL_CONTEXT) as r:
                meta = json.loads(r.read().decode("utf-8", errors="ignore"))

            files = meta.get("files", [])
            videos = []
            for f in files:
                fname = f.get("name", "")
                lower_name = fname.lower()
                if not lower_name.endswith((".mp4", ".mkv", ".webm", ".ogv", ".avi")):
                    continue
                if "sample" in lower_name or lower_name.endswith(".thumbs.mp4"):
                    continue

                size_bytes = int(f.get("size", 0) or 0)
                size_mb = round(size_bytes / (1024 * 1024), 1) if size_bytes else 0
                height_raw = str(f.get("height", "") or "")
                height = int(height_raw) if height_raw.isdigit() else 0

                is_derivative = (
                    lower_name.endswith(".ia.mp4")
                    or "512kb" in lower_name
                    or f.get("source") == "derivative"
                )
                ext = fname.rsplit(".", 1)[-1].upper()

                if height >= 1000 or "1080" in lower_name or size_mb > 1100:
                    quality_badge = f"1080p Full HD ({height}p)" if height else "1080p Full HD"
                    res_rank = 3
                elif height >= 700 or "720" in lower_name or size_mb > 400:
                    quality_badge = f"720p HD ({height}p)" if height else "720p HD"
                    res_rank = 2
                elif not is_derivative:
                    quality_badge = f"HD Original ({height}p)" if height else "HD / Original"
                    res_rank = 1
                else:
                    quality_badge = "SD / Ligero (Carga Rápida)"
                    res_rank = 0

                clean_label = fname.rsplit(".", 1)[0].replace("_", " ").replace(".", " ").strip()
                dl_url = f"https://archive.org/download/{identifier}/{urllib.parse.quote(fname)}"

                videos.append({
                    "name": clean_label or fname,
                    "filename": fname,
                    "url": dl_url,
                    "size_mb": size_mb,
                    "ext": ext,
                    "height": height,
                    "quality": quality_badge,
                    "priority": (0 if is_derivative else 1, res_rank, size_bytes)
                })

            videos.sort(key=lambda x: x["priority"], reverse=True)
            return videos
        except Exception:
            return []

    @classmethod
    def resolve(cls, url):
        if not url:
            return None
        # Si ya es un enlace directo a /download/...
        if "/download/" in url and not url.startswith("archive://"):
            return network_helper.prepare_kodi_stream_url(url)

        ident = cls.extract_identifier(url)
        if ident:
            videos = cls.get_item_video_files(ident)
            if videos:
                return network_helper.prepare_kodi_stream_url(videos[0]["url"])
        return network_helper.prepare_kodi_stream_url(url)


class PeerTubeResolver(BaseServerResolver):
    name = "PeerTube Fediverse Open Server"

    @classmethod
    def can_resolve(cls, url):
        if not url:
            return False
        u = url.lower()
        return u.startswith("peertube://") or "/videos/watch/" in u or "/w/" in u

    @classmethod
    def resolve(cls, url):
        try:
            if url.startswith("peertube://"):
                parts = url.replace("peertube://", "").split("/", 1)
                host, video_id = parts[0], parts[1]
            else:
                parsed = urllib.parse.urlparse(url)
                host = parsed.netloc
                video_id = parsed.path.rstrip("/").split("/")[-1]

            api_url = f"https://{host}/api/v1/videos/{video_id}"
            req = urllib.request.Request(
                api_url,
                headers={"User-Agent": network_helper.DEFAULT_USER_AGENT}
            )
            with urllib.request.urlopen(req, timeout=7, context=network_helper.UNVERIFIED_SSL_CONTEXT) as r:
                data = json.loads(r.read().decode("utf-8", errors="ignore"))

            # Preferir HLS playlist si existe
            playlists = data.get("streamingPlaylists", [])
            if playlists and playlists[0].get("playlistUrl"):
                return network_helper.prepare_kodi_stream_url(playlists[0]["playlistUrl"])

            # Sino usar archivos directos MP4 (ordenados de mayor a menor resolución)
            files = data.get("files", [])
            if files:
                files_sorted = sorted(
                    files,
                    key=lambda f: int(f.get("resolution", {}).get("id", 0) or 0),
                    reverse=True
                )
                if files_sorted[0].get("fileDownloadUrl"):
                    return network_helper.prepare_kodi_stream_url(files_sorted[0]["fileDownloadUrl"])
        except Exception:
            pass
        return network_helper.prepare_kodi_stream_url(url)


class WikimediaCommonsResolver(BaseServerResolver):
    name = "Wikimedia Commons Open Server"

    @classmethod
    def can_resolve(cls, url):
        return "wikimedia.org" in (url or "").lower()

    @classmethod
    def resolve(cls, url):
        return network_helper.prepare_kodi_stream_url(url)


class StreamwishResolver(BaseServerResolver):
    name = "StreamWish / FileLions HD"

    @classmethod
    def can_resolve(cls, url):
        return streamwish_resolver.StreamWishResolver.can_resolve(url or "")

    @classmethod
    def resolve(cls, url):
        try:
            return streamwish_resolver.StreamWishResolver.resolve(url)
        except Exception:
            return network_helper.prepare_kodi_stream_url(url, referer=url)


class DoodstreamResolver(BaseServerResolver):
    name = "Doodstream"

    @classmethod
    def can_resolve(cls, url):
        u = (url or "").lower()
        return any(d in u for d in ["dood.", "doods.", "ds2play.", "d000d."])

    @classmethod
    def resolve(cls, url):
        return network_helper.prepare_kodi_stream_url(url, referer=url)


class HLSStreamResolver(BaseServerResolver):
    name = "HLS / CDN Adaptive Stream"

    @classmethod
    def can_resolve(cls, url):
        u = (url or "").lower()
        return ".m3u8" in u or "master" in u or "smil" in u or ".mpd" in u

    @classmethod
    def resolve(cls, url):
        return network_helper.prepare_kodi_stream_url(url)


RESOLVERS = [
    ArchiveOrgResolver,
    PeerTubeResolver,
    WikimediaCommonsResolver,
    HLSStreamResolver,
    DoodstreamResolver,
    StreamwishResolver,
    BaseServerResolver
]


def detect_server_name(url):
    """Devuelve el nombre amigable del servidor para mostrar en el selector."""
    if not url:
        return "Servidor Directo"
    u = url.lower()
    if "archive.org" in u or u.startswith("archive://"):
        if ".ia.mp4" in u or "512kb" in u:
            return "Archive.org Open CDN (Ligero / Rápido)"
        if u.endswith(".mkv"):
            return "Archive.org Open CDN (Matroska Full HD)"
        return "Archive.org Open CDN (Directo MP4 HD)"
    if "bantel-cdn" in u or "iptvperu" in u:
        return "CDN Sur Sudamérica (HLS 1080p)"
    if "boldmss.com" in u:
        return "CDN Panregional Sports (HLS 1080p)"
    if "amagi.tv" in u or "wurl.com" in u or "mediatailor" in u:
        return "CDN FAST Oficial (HLS 1080p)"
    if "dpsgo.com" in u or "dps.live" in u or "rudo.video" in u:
        return "CDN Oficial Chile (HLS HD)"
    if "wikimedia.org" in u:
        return "Wikimedia Commons Open Server"
    if "blender.org" in u or "unified-streaming.com" in u or "mux.dev" in u:
        return "Open Movie Foundation CDN (HLS 1080p)"
    if any(d in u for d in streamwish_resolver.STREAMWISH_DOMAINS):
        return "StreamWish High-Speed Mirror"
    if ".m3u8" in u:
        return "Servidor HLS Adaptativo (Directo HD)"
    return "Servidor Open Source Directo"


def resolve_media_url(url):
    """Detecta el tipo de servidor y resuelve la mejor URL con cabeceras para Kodi."""
    if not url:
        return None

    for resolver in RESOLVERS:
        if resolver.can_resolve(url):
            resolved = resolver.resolve(url)
            if resolved:
                return resolved

    return network_helper.prepare_kodi_stream_url(url)
