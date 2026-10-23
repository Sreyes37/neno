# -*- coding: utf-8 -*-
"""
neno_pc IPTV - Utilidades de Red, Headers, SSL y Failover Inteligente para Kodi Player
Garantiza compatibilidad universal en Kodi 19/20/21 y soporte para CDNs con puertos personalizados.
"""

import ssl
import urllib.request
import urllib.parse

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)

# Contexto SSL tolerante para streams IPTV en puertos personalizados (:1936, :4433, :19360)
UNVERIFIED_SSL_CONTEXT = ssl.create_default_context()
UNVERIFIED_SSL_CONTEXT.check_hostname = False
UNVERIFIED_SSL_CONTEXT.verify_mode = ssl.CERT_NONE


def strip_kodi_headers(url):
    """Separa la URL base de las cabeceras anexadas con '|' para pruebas HTTP."""
    if not url:
        return "", {}
    parts = url.split("|", 1)
    base_url = parts[0].strip()
    extra_headers = {}
    if len(parts) > 1 and parts[1]:
        for kv in urllib.parse.parse_qsl(parts[1]):
            extra_headers[kv[0]] = kv[1]
    return base_url, extra_headers


def check_stream_health(url, timeout=3.2):
    """Verifica si la URL de streaming responde 200/206/301/302 (con soporte SSL tolerante)."""
    if not url:
        return False
    u_low = url.lower()
    if u_low.startswith(("archive://", "peertube://", "plugin://")):
        return True

    base_url, custom_headers = strip_kodi_headers(url)
    if not base_url.startswith(("http://", "https://")):
        return False

    headers = {
        "User-Agent": custom_headers.get("User-Agent", DEFAULT_USER_AGENT),
        "Accept": "*/*",
        "Connection": "keep-alive"
    }
    if "Referer" in custom_headers:
        headers["Referer"] = custom_headers["Referer"]

    try:
        req = urllib.request.Request(base_url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout, context=UNVERIFIED_SSL_CONTEXT) as response:
            return response.status in (200, 206, 301, 302)
    except Exception:
        return False


def get_best_stream_url(primary_url, backup_urls=None, timeout=2.5):
    """
    Evalúa la URL primaria; si el servidor está caído o rechaza la conexión,
    conmuta automáticamente al primer servidor de respaldo (mirror) activo.
    """
    if not backup_urls:
        return primary_url

    if primary_url and check_stream_health(primary_url, timeout=timeout):
        return primary_url

    for backup in backup_urls:
        if backup and check_stream_health(backup, timeout=timeout):
            return backup

    return primary_url or (backup_urls[0] if backup_urls else "")


def prepare_kodi_stream_url(url, referer=None, user_agent=None):
    """
    Formatea la URL para Kodi con cabeceras HTTP limpias sin romper URLs HLS ni duplicar '|'.
    """
    if not url:
        return ""

    if "|" in url:
        return url

    ua = user_agent or DEFAULT_USER_AGENT
    headers = [f"User-Agent={urllib.parse.quote(ua)}"]
    if referer:
        headers.append(f"Referer={urllib.parse.quote(referer)}")

    return f"{url}|{'&'.join(headers)}"
