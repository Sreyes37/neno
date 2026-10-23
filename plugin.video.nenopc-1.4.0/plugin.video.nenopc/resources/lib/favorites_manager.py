# -*- coding: utf-8 -*-
"""
neno_pc Favorites Manager - Sistema de Guardado de Canales y Películas Favoritas
Permite guardar, eliminar y listar canales favoritos como en Alfa y los mejores addons.
"""

import os
import json
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

FAVORITES_FILE = os.path.join(PROFILE_DIR, "favorites.json")


def load_favorites():
    if not os.path.exists(FAVORITES_FILE):
        return []
    try:
        with open(FAVORITES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_favorites(fav_list):
    try:
        with open(FAVORITES_FILE, "w", encoding="utf-8") as f:
            json.dump(fav_list, f, indent=2, ensure_ascii=False)
        return True
    except Exception:
        return False


def is_favorite(item_id, stream_url=None):
    favs = load_favorites()
    for item in favs:
        if item_id and item.get("id") == item_id:
            return True
        if stream_url and item.get("url") == stream_url:
            return True
    return False


def toggle_favorite(item_dict):
    """Agrega o quita de favoritos y notifica al usuario."""
    favs = load_favorites()
    target_id = item_dict.get("id") or item_dict.get("url")

    idx_to_remove = -1
    for idx, f in enumerate(favs):
        if (target_id and f.get("id") == target_id) or (f.get("url") and f.get("url") == item_dict.get("url")):
            idx_to_remove = idx
            break

    if idx_to_remove >= 0:
        favs.pop(idx_to_remove)
        save_favorites(favs)
        xbmcgui.Dialog().notification("neno_pc", f"Eliminado de Favoritos: {item_dict.get('name') or item_dict.get('title')}", xbmcgui.NOTIFICATION_INFO)
    else:
        favs.append(item_dict)
        save_favorites(favs)
        xbmcgui.Dialog().notification("neno_pc", f"Guardado en Favoritos ⭐: {item_dict.get('name') or item_dict.get('title')}", xbmcgui.NOTIFICATION_INFO)
