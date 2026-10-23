# -*- coding: utf-8 -*-
"""
neno_pc StreamWish Resolver Engine
Motor de resolución de enlaces y servidores StreamWish (y sus clones / dominios alternativos:
wishembed, streamwish.to, wishfast, swhls, flaswish, etc.)
Incluye desempaquetador Dean Edwards (jsunpack) en Python puro y extracción de .m3u8 maestro.
"""

import re
import urllib.request
import urllib.parse
from resources.lib import network_helper

STREAMWISH_DOMAINS = [
    "streamwish", "wishembed", "wishfast", "swwish", "streamwish.to",
    "swhls", "flashwish", "filelions", "vidguard"
]


class StreamWishResolver:
    """Resolvedor de enlaces StreamWish estilo Alfa/ResolveURL."""

    @classmethod
    def can_resolve(cls, url):
        url_lower = url.lower()
        return any(d in url_lower for d in STREAMWISH_DOMAINS)

    @classmethod
    def resolve(cls, url):
        """
        Descarga la página de inserción (embed), desempaqueta el código JS ofuscado
        y extrae el enlace M3U8 directo con los encabezados adecuados para Kodi.
        """
        if not url:
            return None

        # Si ya es un enlace directo m3u8 o mp4
        if url.endswith((".m3u8", ".mp4")):
            return network_helper.prepare_kodi_stream_url(url, referer=url)

        # Normalizar a embed URL si viene como enlace directo
        embed_url = cls._normalize_embed_url(url)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Referer": embed_url
        }

        try:
            req = urllib.request.Request(embed_url, headers=headers)
            with urllib.request.urlopen(req, timeout=7) as response:
                html = response.read().decode("utf-8", errors="ignore")

            # 1. Búsqueda directa de m3u8 en el HTML (cuando no está empacado)
            m3u8_direct = re.search(r'(https?://[^\s\'"<>]+?\.m3u8[^\s\'"<>]*)', html)
            if m3u8_direct:
                stream_url = m3u8_direct.group(1)
                return network_helper.prepare_kodi_stream_url(stream_url, referer=embed_url)

            # 2. Desempaquetar Dean Edwards Packer eval(function(p,a,c,k,e,d)...)
            packed_match = re.search(r"eval\(function\(p,a,c,k,e,[rd]\).*\)", html, re.DOTALL)
            if packed_match:
                unpacked = cls._unpack_packer(packed_match.group(0))
                if unpacked:
                    m3u8_match = re.search(r'(https?://[^\s\'"<>]+?\.m3u8[^\s\'"<>]*)', unpacked)
                    if m3u8_match:
                        stream_url = m3u8_match.group(1)
                        return network_helper.prepare_kodi_stream_url(stream_url, referer=embed_url)

            # Fallback con cabeceras Kodi
            return network_helper.prepare_kodi_stream_url(embed_url, referer=embed_url)
        except Exception:
            return network_helper.prepare_kodi_stream_url(url, referer=url)

    @classmethod
    def _normalize_embed_url(cls, url):
        if "/e/" in url or "/embed-" in url:
            return url
        # Convertir https://streamwish.to/xyz -> https://streamwish.to/e/xyz
        m = re.search(r'(https?://[^/]+)/([a-zA-Z0-9]+)$', url)
        if m:
            return f"{m.group(1)}/e/{m.group(2)}"
        return url

    @classmethod
    def _unpack_packer(cls, packed_code):
        """Desempaquetador Dean Edwards en Python puro."""
        try:
            pattern = r"\}\s*\('(.*)',\s*(\d+),\s*(\d+),\s*'(.*)'\.split\('\|'\)"
            m = re.search(pattern, packed_code, re.DOTALL)
            if not m:
                # Variante con comillas dobles
                pattern2 = r'\}\s*\("(.*)",\s*(\d+),\s*(\d+),\s*"(.*)"\.split\("\|"\)'
                m = re.search(pattern2, packed_code, re.DOTALL)
                if not m:
                    return ""

            payload, radix, count, symtab = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4).split("|")

            def unbase(val_str, b):
                alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                res = 0
                for c in val_str:
                    res = res * b + alphabet.index(c)
                return res

            def lookup(match):
                word = match.group(0)
                try:
                    idx = unbase(word, radix)
                    return symtab[idx] if idx < len(symtab) and symtab[idx] else word
                except Exception:
                    return word

            return re.sub(r"\b\w+\b", lookup, payload)
        except Exception:
            return ""
