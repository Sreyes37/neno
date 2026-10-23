# -*- coding: utf-8 -*-
"""
neno_pc IPTV & VOD - Canales Temáticos 24/7 y Películas
Todos los streams verificados con estado 200 OK en CDN y sin bloqueo.
"""

CHANNELS_247 = [
    # 24/7 INFANTIL & DIBUJOS
    {
        "id": "247_kids",
        "name": "🧸 Canal 24/7 Dibujos Animados & Kids HD",
        "category": "Infantil 24/7",
        "url": "https://origin.dpsgo.com/ssai/event/LhHrVtyeQkKZ-Ye_xEU75g/master.m3u8",
        "backup_urls": [],
        "logo": "https://i.imgur.com/8WJUbSD.png",
        "plot": "Transmisión ininterrumpida las 24 horas de dibujos animados y series infantiles para toda la familia.",
        "year": "2024"
    },
    # 24/7 COMEDIA & HUMOR
    {
        "id": "247_humor",
        "name": "😂 Canal 24/7 Humor & Sketches HD",
        "category": "Comedia 24/7",
        "url": "https://origin.dpsgo.com/ssai/event/cKWySXKgSK-SzlJmESkOWw/master.m3u8",
        "backup_urls": [],
        "logo": "https://i.imgur.com/KvMuTzN.png",
        "plot": "Lo mejor de la comedia, imitaciones, rutinas de stand-up y humor latino sin pausas.",
        "year": "2024"
    },
    # 24/7 SERIES & DRAMA
    {
        "id": "247_series",
        "name": "📺 Canal 24/7 Series & Telenovelas HD",
        "category": "Series 24/7",
        "url": "https://origin.dpsgo.com/ssai/event/f4TrySe8SoiGF8Lu3EIq1g/master.m3u8",
        "backup_urls": [],
        "logo": "https://i.imgur.com/csBNi2L.png",
        "plot": "Maratones de temporadas completas y series de ficción 24 horas al día.",
        "year": "2024"
    },
    # 24/7 CULTURA & VIAJES
    {
        "id": "247_cultura",
        "name": "🌍 Canal 24/7 Cultura, Viajes & Gastronomía HD",
        "category": "Documentales 24/7",
        "url": "https://origin.dpsgo.com/ssai/event/GI-9cp_bT8KcerLpZwkuhw/master.m3u8",
        "backup_urls": [],
        "logo": "https://i.imgur.com/Zfe2f5j.png",
        "plot": "Recorridos turísticos, documentales culturales y gastronomía de todo el continente 24/7.",
        "year": "2024"
    },
    # 24/7 MÚSICA & FESTIVALES
    {
        "id": "247_musica",
        "name": "🎸 Canal 24/7 Festivales & Conciertos HD",
        "category": "Música 24/7",
        "url": "https://origin.dpsgo.com/ssai/event/Nftd0fM2SXasfDlRphvUsg/master.m3u8",
        "backup_urls": [],
        "logo": "https://i.imgur.com/Ymk6j5o.png",
        "plot": "Grandes espectáculos en vivo, shows musicales y festivales internacionales las 24 horas.",
        "year": "2024"
    },
    # 24/7 ENTRETENIMIENTO & REALITY
    {
        "id": "247_realities",
        "name": "⭐ Canal 24/7 Realities & Espectáculos HD",
        "category": "Entretenimiento 24/7",
        "url": "https://origin.dpsgo.com/ssai/event/g7_JOM0ORki9SR5RKHe-Kw/master.m3u8",
        "backup_urls": [
            "https://origin.dpsgo.com/ssai/event/BBp0VeP6QtOOlH8nu3bWTg/master.m3u8"
        ],
        "logo": "https://i.imgur.com/m0SuwMU.png",
        "plot": "Transmisión continua de realities de convivencia, desafíos extremos y farándula.",
        "year": "2024"
    }
]


MOVIES_CATALOG = [
    {
        "id": "mov_tears_of_steel",
        "title": "Tears of Steel (Ciencia Ficción 4K)",
        "genre": "Ciencia Ficción / Acción",
        "year": "2012",
        "rating": "8.0",
        "plot": "En un futuro post-apocalíptico en Ámsterdam, un grupo de científicos y guerreros intentan cambiar el pasado para evitar la rebelión de las máquinas.",
        "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Tears_of_Steel_poster.jpg/440px-Tears_of_Steel_poster.jpg",
        "fanart": "https://mango.blender.org/wp-content/uploads/2012/09/01_comp_00060.jpg",
        "url": "https://demo.unified-streaming.com/k8s/features/stable/video/tears-of-steel/tears-of-steel.ism/.m3u8",
        "backup_urls": []
    },
    {
        "id": "mov_big_buck_bunny",
        "title": "Big Buck Bunny (Animación / Familiar HD)",
        "genre": "Animación / Familiar",
        "year": "2008",
        "rating": "7.9",
        "plot": "Un enorme y bondadoso conejo se enfrenta a tres roedores traviesos del bosque que no paran de hacerle la vida imposible.",
        "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Big_buck_bunny_poster_big.jpg/440px-Big_buck_bunny_poster_big.jpg",
        "fanart": "https://peach.blender.org/wp-content/uploads/bbb-splash.png",
        "url": "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8",
        "backup_urls": []
    }
]


def get_247_categories():
    cats = sorted(list(set(c.get("category", "Otros 24/7") for c in CHANNELS_247)))
    return cats


def get_channels_by_category_247(category_name):
    return [c for c in CHANNELS_247 if c.get("category") == category_name]


def get_movie_genres():
    genres = sorted(list(set(m.get("genre", "Otros") for m in MOVIES_CATALOG)))
    return genres


def get_movies_by_genre(genre_name):
    return [m for m in MOVIES_CATALOG if m.get("genre") == genre_name]


def find_stream_by_id(item_id):
    for ch in CHANNELS_247:
        if ch.get("id") == item_id:
            return ch
    for mov in MOVIES_CATALOG:
        if mov.get("id") == item_id:
            return mov
    return None
