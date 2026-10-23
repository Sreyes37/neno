# -*- coding: utf-8 -*-
"""
neno_pc History Manager - Historial de Reproducción (Vistos Recientemente)
Guarda automáticamente los últimos canales y películas reproducidos para acceso rápido.
"""

import os
import json
import time
import xbmc
import xbmcgui
import xbmcaddon
import xbmcvfs

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

HISTORY_FILE = os.path.join(PROFILE_DIR, "watch_history.json")
MAX_HISTORY_ITEMS = 40


def load_history():
    """Carga la lista de elementos vistos recientemente."""
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []


def save_history(history_list):
    """Guarda la lista de historial en disco."""
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history_list[:MAX_HISTORY_ITEMS], f, indent=2, ensure_ascii=False)
        return True
    except Exception:
        return False


def add_to_history(item_dict):
    """Registra un canal o película al principio del historial evitando duplicados."""
    if not item_dict:
        return
    url = item_dict.get("url", "")
    title = item_dict.get("name") or item_dict.get("title") or ""
    if not url and not item_dict.get("id"):
        return

    history = load_history()
    filtered = []
    for h in history:
        same_id = item_dict.get("id") and h.get("id") == item_dict.get("id")
        same_url = url and h.get("url") == url
        if not (same_id or same_url):
            filtered.append(h)

    entry = {
        "id": item_dict.get("id", ""),
        "name": title,
        "url": url,
        "logo": item_dict.get("logo") or item_dict.get("poster") or "",
        "category": item_dict.get("category") or item_dict.get("genre") or "Reciente",
        "type": item_dict.get("type", "video"),
        "timestamp": time.strftime("%d/%m/%Y %H:%M")
    }
    filtered.insert(0, entry)
    save_history(filtered)


def clear_history():
    """Borra todo el historial de reproducción."""
    save_history([])
    xbmcgui.Dialog().notification(
        "neno_pc",
        "Historial de reproducción borrado correctamente",
        xbmcgui.NOTIFICATION_INFO
    )
