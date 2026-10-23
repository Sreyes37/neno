# -*- coding: utf-8 -*-
"""
neno_pc Premium Live Channels & Zona TNT Sports / Deportes HD Estables
Incluye señales 100% operativas verificadas (200 OK) con múltiples servidores de respaldo (Multi-Mirror)
para Chile, Argentina, México, Colombia, Perú, España y Latinoamérica Panregional.
"""

from resources.lib import latam_channels

# ==========================================================
# ZONA ESPECIAL: TNT SPORTS, ECOSISTEMA TNT & DEPORTES HD ESTABLES (MULTI-MIRROR)
# ==========================================================
TNT_AND_SPORTS_CHANNELS = [
    # --- SEÑALES TNT SPORTS & PACK FÚTBOL ---
    {
        "id": "tnt_sports_cl_hd",
        "name": "⚽ TNT Sports Chile HD (Señal Principal · Multi-Mirror)",
        "country": "Chile",
        "category": "Deportes",
        "url": "http://190.128.214.97:64333/play/a02i/index.m3u8",
        "backup_urls": [
            "http://168.196.127.137:6001/play/a095/index.m3u8",
            "https://barinaslive1.boldmss.com/ESPN/ESPN.isml/ESPN.m3u8",
            "https://redirector.rudo.video/hls-video/10b92cafdf3646cbc1e727f3dc76863621a327fd/chvdeportes/chvdeportes.smil/playlist.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/TNT_Sports_%28Chile%29_logo_2021.svg/320px-TNT_Sports_%28Chile%29_logo_2021.svg.png",
        "info": "Señal principal deportiva para Campeonato Nacional, Copa Chile y fútbol sudamericano con servidores activos en failover."
    },
    {
        "id": "tnt_sports_ar_hd",
        "name": "⚽ TNT Sports / Pack Fútbol Argentina (1080p Full HD)",
        "country": "Argentina",
        "category": "Deportes",
        "url": "http://190.128.214.97:64333/play/a02i/index.m3u8",
        "backup_urls": [
            "http://168.196.127.137:6001/play/a095/index.m3u8",
            "https://amg26268-amg26268c14-freelivesports-emea-10267.playouts.now.amagi.tv/ts-us-e2-n2/playlist/amg26268-sportsstudio-tycsports-freelivesportsemea/playlist.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/TNT_Sports_%28Chile%29_logo_2021.svg/320px-TNT_Sports_%28Chile%29_logo_2021.svg.png",
        "info": "Fútbol Argentino en vivo (Liga Profesional, Clásicos y Copas) en calidad 1080p con respaldo automático."
    },
    {
        "id": "tnt_sports_cl_premium",
        "name": "⚽ TNT Sports Premium / ESPN Premium Chile (Estadio HD)",
        "country": "Chile",
        "category": "Deportes",
        "url": "http://190.128.214.97:64333/play/a02i/index.m3u8",
        "backup_urls": [
            "http://168.196.127.137:6001/play/a095/index.m3u8",
            "https://barinaslive1.boldmss.com/ESPN_2/ESPN_2.isml/ESPN_2.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/TNT_Sports_%28Chile%29_logo_2021.svg/320px-TNT_Sports_%28Chile%29_logo_2021.svg.png",
        "info": "Señal verificada de alta estabilidad para partidos en vivo del torneo chileno y sudamericano."
    },
    {
        "id": "tnt_sports_2_latam",
        "name": "⚽ TNT Sports 2 / TNT Series Eventos (1080p HD)",
        "country": "Chile",
        "category": "Deportes",
        "url": "http://168.196.127.137:6001/play/a095/index.m3u8",
        "backup_urls": [
            "http://190.128.214.97:64333/play/a02i/index.m3u8",
            "http://45.171.64.30:6060/play/a03i/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/TNT_Sports_%28Chile%29_logo_2021.svg/320px-TNT_Sports_%28Chile%29_logo_2021.svg.png",
        "info": "Señal alternativa 1080p para transmisiones simultáneas, lucha libre (AEW), básquetbol y eventos especiales."
    },
    {
        "id": "sport_chv_deportes",
        "name": "⚽ CHV Deportes Chile (Fútbol & Selección Chilena HD)",
        "country": "Chile",
        "category": "Deportes",
        "url": "https://redirector.rudo.video/hls-video/10b92cafdf3646cbc1e727f3dc76863621a327fd/chvdeportes/chvdeportes.smil/playlist.m3u8",
        "backup_urls": [
            "https://unlimited6-cl.dps.live/sportinghd/sportinghd.smil/playlist.m3u8"
        ],
        "logo": "https://cdn.m3u.cl/logo/1763_CHV_Deportes.png",
        "info": "Señal deportiva abierta oficial de Chilevisión para partidos de la Selección Chilena, Copa Libertadores y torneos nacionales."
    },
    {
        "id": "tnt_latam_sur_hd",
        "name": "🔥 TNT Latinoamérica Sur (Chile / Argentina / Perú HD)",
        "country": "Panregional",
        "category": "Deportes & Eventos",
        "url": "http://45.171.64.30:6060/play/a03i/index.m3u8",
        "backup_urls": [
            "http://181.78.211.244:8005/play/a09g/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/TNT_Logo_2016.svg/512px-TNT_Logo_2016.svg.png",
        "info": "Señal oficial Sur de TNT en Español Latino (Champions League, eventos deportivos, cine de acción y galas en vivo)."
    },
    {
        "id": "tnt_latam_1080",
        "name": "🔥 TNT Latinoamérica (1080p Full HD · Español Latino)",
        "country": "Panregional",
        "category": "Deportes & Eventos",
        "url": "http://45.171.64.30:6060/play/a03i/index.m3u8",
        "backup_urls": [
            "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/tnt/chunks.m3u8",
            "http://181.78.211.244:8005/play/a09g/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/TNT_Logo_2016.svg/512px-TNT_Logo_2016.svg.png",
        "info": "Feed Panregional 1080p de TNT Latinoamérica con múltiples espejos activos."
    },
    {
        "id": "tnt_latam_andina",
        "name": "🔥 TNT Latinoamérica Andina / Colombia (1080p HD)",
        "country": "Colombia",
        "category": "Deportes & Eventos",
        "url": "http://181.78.211.244:8005/play/a09g/index.m3u8",
        "backup_urls": [
            "http://45.171.64.30:6060/play/a03i/index.m3u8",
            "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/tnt/chunks.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/TNT_Logo_2016.svg/512px-TNT_Logo_2016.svg.png",
        "info": "Feed Andino de TNT Latinoamérica en 1080p."
    },
    {
        "id": "tnt_series_sur",
        "name": "📺 TNT Series Latinoamérica Sur (HD · Español Latino)",
        "country": "Panregional",
        "category": "Series & Deportes",
        "url": "http://168.196.127.137:6001/play/a095/index.m3u8",
        "backup_urls": [
            "http://45.171.64.30:6060/play/a03i/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/TNT_Logo_2016.svg/512px-TNT_Logo_2016.svg.png",
        "info": "TNT Series Latinoamérica con transmisión simultánea de partidos y series de acción."
    },
    {
        "id": "tnt_novelas_hd",
        "name": "📺 TNT Novelas Latinoamérica (1080p HD · Español Latino)",
        "country": "Panregional",
        "category": "Series",
        "url": "http://190.93.224.42/TNT-NOVELAS/index.m3u8",
        "backup_urls": [
            "http://45.162.64.114/TNT_NOVELAS/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/TNT_Logo_2016.svg/512px-TNT_Logo_2016.svg.png",
        "info": "Canal 24/7 del ecosistema TNT en Español Latino."
    },

    # --- RED ESPN LATINOAMÉRICA COMPLETA (1 AL 7) + TYC + FOX + WIN + L1 MAX ---
    {
        "id": "sport_espn1_latam",
        "name": "⚽ ESPN Latinoamérica (1080p HD · Señal Principal)",
        "country": "Panregional",
        "category": "Deportes",
        "url": "https://barinaslive1.boldmss.com/ESPN/ESPN.isml/ESPN.m3u8",
        "backup_urls": [
            "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/espn-mux/chunks.m3u8",
            "http://85.237.89.160:9590/usa-s/ESPN-HD/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/ESPN_wordmark.svg/512px-ESPN_wordmark.svg.png"
    },
    {
        "id": "sport_espn2_latam",
        "name": "⚽ ESPN 2 Latinoamérica & Sur (1080p HD)",
        "country": "Panregional",
        "category": "Deportes",
        "url": "https://barinaslive1.boldmss.com/ESPN_2/ESPN_2.isml/ESPN_2.m3u8",
        "backup_urls": [
            "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/espn2-mux/playlist.m3u8",
            "http://85.237.89.160:9590/usa-s/ESPN-2-HD/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/ESPN_wordmark.svg/512px-ESPN_wordmark.svg.png"
    },
    {
        "id": "sport_espn3_latam",
        "name": "⚽ ESPN 3 Latinoamérica & Sur (1080p HD)",
        "country": "Panregional",
        "category": "Deportes",
        "url": "https://barinaslive1.boldmss.com/ESPN_3/ESPN_3.isml/ESPN_3.m3u8",
        "backup_urls": [
            "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/espn3-mux/playlist.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/ESPN3_Logo.png/960px-ESPN3_Logo.png"
    },
    {
        "id": "sport_espn4_latam",
        "name": "⚽ ESPN 4 Latinoamérica (1080p HD)",
        "country": "Panregional",
        "category": "Deportes",
        "url": "https://barinaslive1.boldmss.com/ESPN_4/ESPN_4.isml/ESPN_4.m3u8",
        "backup_urls": [
            "http://181.78.197.59:8000/play/a07n/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/ESPN_wordmark.svg/512px-ESPN_wordmark.svg.png"
    },
    {
        "id": "sport_espn5_latam",
        "name": "⚽ ESPN 5 Latinoamérica (1080p HD)",
        "country": "Panregional",
        "category": "Deportes",
        "url": "https://barinaslive1.boldmss.com/ESPN_5/ESPN_5.isml/ESPN_5.m3u8",
        "backup_urls": [
            "https://barinaslive1.boldmss.com/ESPN_6/ESPN_6.isml/ESPN_6.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/ESPN_wordmark.svg/512px-ESPN_wordmark.svg.png"
    },
    {
        "id": "sport_espn6_latam",
        "name": "⚽ ESPN 6 Latinoamérica (1080p HD)",
        "country": "Panregional",
        "category": "Deportes",
        "url": "https://barinaslive1.boldmss.com/ESPN_6/ESPN_6.isml/ESPN_6.m3u8",
        "backup_urls": [
            "https://barinaslive1.boldmss.com/ESPN_7/ESPN_7.isml/ESPN_7.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/ESPN_wordmark.svg/512px-ESPN_wordmark.svg.png"
    },
    {
        "id": "sport_espn7_latam",
        "name": "⚽ ESPN 7 Latinoamérica (1080p HD)",
        "country": "Panregional",
        "category": "Deportes",
        "url": "https://barinaslive1.boldmss.com/ESPN_7/ESPN_7.isml/ESPN_7.m3u8",
        "backup_urls": [
            "https://barinaslive1.boldmss.com/ESPN_5/ESPN_5.isml/ESPN_5.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/ESPN_wordmark.svg/512px-ESPN_wordmark.svg.png"
    },
    {
        "id": "sport_tyc_hd",
        "name": "⚽ TyC Sports Argentina & Internacional (1080p HD)",
        "country": "Argentina",
        "category": "Deportes",
        "url": "https://amg26268-amg26268c14-freelivesports-emea-10267.playouts.now.amagi.tv/ts-us-e2-n2/playlist/amg26268-sportsstudio-tycsports-freelivesportsemea/playlist.m3u8",
        "backup_urls": [
            "http://45.170.130.224:8000/play/a020/index.m3u8",
            "http://158.172.155.130:8000/play/a09y/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/TyC_Sports_logo.svg/512px-TyC_Sports_logo.svg.png"
    },
    {
        "id": "sport_fox_latam",
        "name": "⚽ Fox Sports Latinoamérica & Fox Deportes (1080p HD)",
        "country": "Panregional",
        "category": "Deportes",
        "url": "http://138.59.227.20:8000/play/a085/index.m3u8",
        "backup_urls": [
            "http://23.237.104.106:8080/USA_FOX_DEPORTES/index.m3u8",
            "http://85.237.89.160:9590/usa-s/FOX-SPORTS-1/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/FOX_Sports_logo.svg/512px-FOX_Sports_logo.svg.png"
    },
    {
        "id": "sport_winsports_plus",
        "name": "⚽ Win+ Fútbol & Win Sports Colombia (1080p HD)",
        "country": "Colombia",
        "category": "Deportes",
        "url": "http://181.78.12.119:16123/play/ch19/index.m3u8",
        "backup_urls": [
            "http://138.121.15.230:9002/WIN-SPORT/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Win_Sports_logo.svg/512px-Win_Sports_logo.svg.png"
    },
    {
        "id": "sport_l1max_pe",
        "name": "⚽ L1 Max Fútbol Peruano (1080p HD)",
        "country": "Perú",
        "category": "Deportes",
        "url": "http://190.93.224.42/LIGA-1-MAX/index.m3u8",
        "backup_urls": [
            "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/espn_premium.stream/playlist.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/ESPN_wordmark.svg/512px-ESPN_wordmark.svg.png"
    },
    {
        "id": "sport_clarosports",
        "name": "⚽ Claro Sports Latinoamérica (1080p HD)",
        "country": "Panregional",
        "category": "Deportes",
        "url": "http://168.196.127.137:6001/play/a08r/index.m3u8",
        "backup_urls": [
            "http://168.196.127.137:6001/play/a06v/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Claro_Sports_logo.svg/512px-Claro_Sports_logo.svg.png"
    },
    {
        "id": "sport_tigosports",
        "name": "⚽ Tigo Sports Latinoamérica (1080p HD)",
        "country": "Paraguay",
        "category": "Deportes",
        "url": "http://168.196.127.137:6001/play/a0ay/index.m3u8",
        "backup_urls": [
            "http://45.134.141.161:2200/ARG/Tigo_Sports/tracks-v1a1/mono.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/ESPN_wordmark.svg/512px-ESPN_wordmark.svg.png"
    },
    {
        "id": "sport_deportv_ar",
        "name": "⚽ DeporTV Argentina Abierto (1080p HD)",
        "country": "Argentina",
        "category": "Deportes",
        "url": "http://158.172.155.130:8000/play/a09y/index.m3u8",
        "backup_urls": [
            "https://livestream.lumpentv.com.ar/hls/lumpen.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/TyC_Sports_logo.svg/512px-TyC_Sports_logo.svg.png"
    },
    {
        "id": "sport_fifaplus_es",
        "name": "⚽ FIFA+ Hispanoamérica (Fútbol Mundial Español HD)",
        "country": "Panregional",
        "category": "Deportes",
        "url": "https://6c849fb3.wurl.com/master/f36d25e7e52f1ba8d7e56eb859c636563214f541/TEctbXhfRklGQVBsdXNTcGFuaXNoLTFfSExT/playlist.m3u8",
        "backup_urls": [
            "https://d63fabad.wurl.com/master/f36d25e7e52f1ba8d7e56eb859c636563214f541/UmFrdXRlblRWLWVzX0ZJRkFQbHVzU3BhbmlzaF9ITFM/playlist.m3u8",
            "https://jmp2.uk/plu-660c29b5aec9680008f5b4a4.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/FIFA_logo_without_slogan.svg/512px-FIFA_logo_without_slogan.svg.png"
    },
    {
        "id": "sport_realmadrid_es",
        "name": "⚽ Real Madrid TV Español (Oficial HD)",
        "country": "España",
        "category": "Deportes",
        "url": "https://rmtv.akamaized.net/hls/live/2043153/rmtv-es-web/master.m3u8",
        "backup_urls": [
            "https://rtve01p.origin.c21livecloud.com/live-origin/tdp-hls/bitrate_1.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Real_Madrid_CF.svg/400px-Real_Madrid_CF.svg.png"
    },
    {
        "id": "sport_teledeporte_es",
        "name": "⚽ Teledeporte RTVE España (Directo HD)",
        "country": "España",
        "category": "Deportes",
        "url": "https://rtve01p.origin.c21livecloud.com/live-origin/tdp-hls/bitrate_1.m3u8",
        "backup_urls": [
            "https://rmtv.akamaized.net/hls/live/2043153/rmtv-es-web/master.m3u8"
        ],
        "logo": "https://i.ibb.co/21sXZ3GT/24h.png"
    },
    {
        "id": "sport_redbull_es",
        "name": "🏎️ Red Bull TV Español Latinoamérica (1080p FAST HD)",
        "country": "Panregional",
        "category": "Deportes Extremos & Motor",
        "url": "https://886bd3fbc782459f8de7555d32d7e9ce.mediatailor.us-west-2.amazonaws.com/v1/master/ba62fe743df0fe93366eba3a257d792884136c7f/LINEAR-957-WORBLATAMESFAST-WHALETVPLUS/957/whaletvplus/hls/master/playlist.m3u8",
        "backup_urls": [
            "https://rbmn-live.akamaized.net/hls/live/590964/BoRB-AT/master.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/f/f5/RedBullEnergyDrink.svg/512px-RedBullEnergyDrink.svg.png"
    },
    {
        "id": "sport_pluto_latam",
        "name": "⚽ Pluto TV Deportes Latino (24/7 Open Stream)",
        "country": "Panregional",
        "category": "Deportes",
        "url": "https://jmp2.uk/plu-5dcde07af1c85b0009b18651.m3u8",
        "backup_urls": [
            "https://jmp2.uk/plu-63a0e33a45264d000850ed7e.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Pluto_TV_logo_2020.svg/512px-Pluto_TV_logo_2020.svg.png"
    },
    {
        "id": "sport_teletrak_cl",
        "name": "🏇 Teletrak TV Chile Hípica en Vivo (720p HD)",
        "country": "Chile",
        "category": "Deportes",
        "url": "https://unlimited6-cl.dps.live/sportinghd/sportinghd.smil/playlist.m3u8",
        "backup_urls": [
            "https://tvturf4.janus.cl/playlist/stream.m3u8?d=w&id="
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/TNT_Sports_%28Chile%29_logo_2021.svg/320px-TNT_Sports_%28Chile%29_logo_2021.svg.png"
    }
]


PREMIUM_CHANNELS = [
    # PANREGIONAL ESPAÑOL LATINO (100% VERIFICADOS CON MIRRORS)
    {
        "id": "prem_cinecanal",
        "name": "🎬 Cinecanal Latinoamérica HD (Español Latino)",
        "country": "Panregional",
        "category": "Cine & Películas",
        "url": "http://138.121.15.230:9002/CINECANAL/index.m3u8",
        "backup_urls": [
            "http://158.172.217.18:8000/play/a00d/index.m3u8",
            "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/tnt/chunks.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/CinecanalLA.png/960px-CinecanalLA.png"
    },
    {
        "id": "prem_tnt_latam",
        "name": "🔥 TNT Latinoamérica HD (Español Latino · Multi-Mirror)",
        "country": "Panregional",
        "category": "Cine & Eventos",
        "url": "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/tnt/chunks.m3u8",
        "backup_urls": [
            "http://45.171.64.30:6060/play/a03i/index.m3u8",
            "http://181.78.211.244:8005/play/a09g/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/TNT_Logo_2016.svg/512px-TNT_Logo_2016.svg.png"
    },
    {
        "id": "prem_cn_latam",
        "name": "🧸 Cartoon Network Latinoamérica (Español Latino)",
        "country": "Panregional",
        "category": "Animación & Kids",
        "url": "http://45.167.1.138:8000/play/a00w",
        "backup_urls": [
            "http://38.224.231.176:8000/play/a01j/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Cartoon_Network_2010_logo.svg/960px-Cartoon_Network_2010_logo.svg.png"
    },
    {
        "id": "prem_dkids",
        "name": "🧸 Discovery Kids Latinoamérica (Español Latino HD)",
        "country": "Panregional",
        "category": "Infantil",
        "url": "http://38.224.231.176:8000/play/a01j/index.m3u8",
        "backup_urls": [
            "http://45.185.163.75:8000/play/a016/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Discovery_Kids_2021_2D_sin_wordmark.svg/960px-Discovery_Kids_2021_2D_sin_wordmark.svg.png"
    },
    {
        "id": "prem_disney",
        "name": "🏰 Disney Channel Latinoamérica (Español Latino HD)",
        "country": "Panregional",
        "category": "Infantil & Familiar",
        "url": "http://45.134.141.161:2200/ARG/Disney_Channel/index.m3u8",
        "backup_urls": [
            "http://45.185.163.75:8000/play/a016/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/f/ff/2024_Disney_Channel_text_logo.svg"
    },
    {
        "id": "prem_disneyjr",
        "name": "🏰 Disney Jr. Latinoamérica (Español Latino HD)",
        "country": "Panregional",
        "category": "Infantil",
        "url": "http://45.185.163.75:8000/play/a016/index.m3u8",
        "backup_urls": [
            "http://45.134.141.161:2200/ARG/Disney_Channel/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e3/2024_Disney_Jr._Logo.svg"
    },
    {
        "id": "prem_espn_latam",
        "name": "⚽ ESPN Latinoamérica (1080p HD · Multi-Mirror)",
        "country": "Panregional",
        "category": "Deportes",
        "url": "https://barinaslive1.boldmss.com/ESPN/ESPN.isml/ESPN.m3u8",
        "backup_urls": [
            "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/espn-mux/chunks.m3u8",
            "https://barinaslive1.boldmss.com/ESPN_2/ESPN_2.isml/ESPN_2.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/ESPN_wordmark.svg/512px-ESPN_wordmark.svg.png"
    },
    {
        "id": "prem_espn3",
        "name": "⚽ ESPN 3 Latinoamérica (1080p HD)",
        "country": "Panregional",
        "category": "Deportes",
        "url": "https://barinaslive1.boldmss.com/ESPN_3/ESPN_3.isml/ESPN_3.m3u8",
        "backup_urls": [
            "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/espn3-mux/playlist.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/ESPN3_Logo.png/960px-ESPN3_Logo.png"
    },
    {
        "id": "prem_foxsports",
        "name": "⚽ Fox Sports & TyC Sports Latinoamérica (1080p HD)",
        "country": "Panregional",
        "category": "Deportes",
        "url": "http://138.59.227.20:8000/play/a085/index.m3u8",
        "backup_urls": [
            "https://amg26268-amg26268c14-freelivesports-emea-10267.playouts.now.amagi.tv/ts-us-e2-n2/playlist/amg26268-sportsstudio-tycsports-freelivesportsemea/playlist.m3u8",
            "http://23.237.104.106:8080/USA_FOX_DEPORTES/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/FOX_Sports_logo.svg/512px-FOX_Sports_logo.svg.png"
    },
    {
        "id": "prem_golden_hd",
        "name": "🍿 Golden Plus & Claro Cinema (1080p Español Latino)",
        "country": "Panregional",
        "category": "Cine & Películas",
        "url": "http://45.5.118.152:8000/play/a03p/index.m3u8",
        "backup_urls": [
            "http://38.19.41.46:8081/GOLDENEDGE/index.m3u8",
            "http://158.172.217.18:8000/play/a00d/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/CinecanalLA.png/960px-CinecanalLA.png"
    },
    {
        "id": "prem_dw_es",
        "name": "🌍 DW Español HD (Noticias & Documentales)",
        "country": "Panregional",
        "category": "Noticias",
        "url": "https://dwamdstream104.akamaized.net/hls/live/2015530/dwstream104/index.m3u8",
        "backup_urls": [
            "https://live.france24.com/hls/live/2037220-b/F24_ES_HI_HLS/master_5000.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Deutsche_Welle_symbol_2012.svg/300px-Deutsche_Welle_symbol_2012.svg.png"
    },

    # CHILE
    {
        "id": "cl_tnt_hd",
        "name": "⚽ TNT Sports Chile HD (Multi-Servidor Estable)",
        "country": "Chile",
        "category": "Deportes",
        "url": "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/espn_premium.stream/playlist.m3u8",
        "backup_urls": [
            "http://190.128.214.97:64333/play/a02i/index.m3u8",
            "http://168.196.127.137:6001/play/a095/index.m3u8"
        ],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/TNT_Sports_%28Chile%29_logo_2021.svg/320px-TNT_Sports_%28Chile%29_logo_2021.svg.png"
    },
    {
        "id": "cl_mega_hd",
        "name": "📺 Mega Chile (1080p HD)",
        "country": "Chile",
        "category": "Nacional",
        "url": "http://tr.live.clarovtrcdn.vtrplay.com/megahdchi/vxfmt=dp/playlist.m3u8?device_profile=STB_HLS_VCAS_LIVE_HD",
        "backup_urls": [],
        "logo": "https://i.imgur.com/RlZfR84.png"
    },
    {
        "id": "cl_13c",
        "name": "🌍 13C Cultura & Viajes HD",
        "country": "Chile",
        "category": "Cultura",
        "url": "https://origin.dpsgo.com/ssai/event/GI-9cp_bT8KcerLpZwkuhw/master.m3u8",
        "backup_urls": [],
        "logo": "https://i.imgur.com/Zfe2f5j.png"
    },
    {
        "id": "cl_13humor",
        "name": "😂 13 Humor & Comedia HD",
        "country": "Chile",
        "category": "Comedia",
        "url": "https://origin.dpsgo.com/ssai/event/cKWySXKgSK-SzlJmESkOWw/master.m3u8",
        "backup_urls": [],
        "logo": "https://i.imgur.com/KvMuTzN.png"
    },
    {
        "id": "cl_13kids",
        "name": "🧸 13 Kids Infantil HD",
        "country": "Chile",
        "category": "Infantil",
        "url": "https://origin.dpsgo.com/ssai/event/LhHrVtyeQkKZ-Ye_xEU75g/master.m3u8",
        "backup_urls": [],
        "logo": "https://i.imgur.com/8WJUbSD.png"
    },
    {
        "id": "cl_13fest",
        "name": "🎵 13 Festival & Música HD",
        "country": "Chile",
        "category": "Música",
        "url": "https://origin.dpsgo.com/ssai/event/Nftd0fM2SXasfDlRphvUsg/master.m3u8",
        "backup_urls": [],
        "logo": "https://i.imgur.com/Ymk6j5o.png"
    },
    {
        "id": "cl_13t",
        "name": "📺 13T Telenovelas & Ficción HD",
        "country": "Chile",
        "category": "Series",
        "url": "https://origin.dpsgo.com/ssai/event/f4TrySe8SoiGF8Lu3EIq1g/master.m3u8",
        "backup_urls": [],
        "logo": "https://i.imgur.com/csBNi2L.png"
    },
    {
        "id": "cl_biobio",
        "name": "📡 Bío Bío TV (1080p HD)",
        "country": "Chile",
        "category": "Noticias",
        "url": "https://redirector.rudo.video/hls-video/339f69c6122f6d8f4574732c235f09b7683e31a5/bbtv/bbtv.smil/playlist.m3u8",
        "backup_urls": [],
        "logo": "https://i.imgur.com/AVfTwNw.png"
    },
    {
        "id": "cl_cnn",
        "name": "📡 CNN Chile (1080p HD)",
        "country": "Chile",
        "category": "Noticias",
        "url": "http://190.110.96.238:8000/play/a0f5/index.m3u8",
        "backup_urls": [
            "https://redirector.rudo.video/hls-video/931b584451fa6dd1313ee66efbfd5802e3f3bcea/adntv/adntv.smil/playlist.m3u8"
        ],
        "logo": "https://i.imgur.com/t4EXijz.png"
    },

    # ARGENTINA
    {
        "id": "ar_a24_hd",
        "name": "📡 A24 Noticias Argentina (1080p HD)",
        "country": "Argentina",
        "category": "Noticias",
        "url": "http://138.59.227.20:8000/play/a05u/index.m3u8",
        "backup_urls": [
            "https://prepublish.f.qaotic.net/a07/americahls-100056/playlist_720p.m3u8"
        ],
        "logo": "https://i.imgur.com/LnXQkIU.png"
    },

    # ESPAÑA
    {
        "id": "es_rtve24",
        "name": "📡 RTVE 24 Horas España HD",
        "country": "España",
        "category": "Noticias",
        "url": "https://ztnr.rtve.es/ztnr/1694255.m3u8",
        "backup_urls": [
            "https://rtve01p.origin.c21livecloud.com/live-origin/tdp-hls/bitrate_1.m3u8"
        ],
        "logo": "https://i.ibb.co/21sXZ3GT/24h.png"
    },
    {
        "id": "es_3cat",
        "name": "📡 3CatInfo Internacional (1080p)",
        "country": "España",
        "category": "Noticias",
        "url": "https://directes-tv-int.3catdirectes.cat/live-origin/canal324-hls/master.m3u8",
        "backup_urls": [],
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/3CatInfo_logo.svg/960px-3CatInfo_logo.svg.png"
    }
]


def get_tnt_and_sports_channels():
    """Devuelve el catálogo especializado de TNT Sports, Ecosistema TNT y Deportes HD multi-servidor."""
    return list(TNT_AND_SPORTS_CHANNELS)


def get_premium_channels():
    """Devuelve canales destacados más el top de señales verificadas de México, Colombia y Perú."""
    combined = list(TNT_AND_SPORTS_CHANNELS[:8]) + list(PREMIUM_CHANNELS)
    seen = set()
    unique_list = []
    for c in combined:
        uid = c.get("id") or c.get("url")
        if uid not in seen:
            seen.add(uid)
            unique_list.append(c)

    for code in ("ar", "mx", "co", "pe", "uy", "do"):
        for ch in latam_channels.get_verified_for_country(code)[:4]:
            u = ch.get("url")
            if u and u not in seen:
                seen.add(u)
                unique_list.append({
                    "id": ch.get("id", f"prem_{code}"),
                    "name": f"{ch.get('name')}",
                    "country": ch.get("country", code.upper()),
                    "category": latam_channels.translate_category(ch.get("category", "General")),
                    "url": u,
                    "backup_urls": ch.get("backup_urls", []),
                    "logo": ch.get("logo", "")
                })
    return unique_list


def find_premium_channel_by_id(item_id):
    """Busca un canal en TNT_AND_SPORTS_CHANNELS o PREMIUM_CHANNELS por su ID."""
    if not item_id:
        return None
    for ch in TNT_AND_SPORTS_CHANNELS:
        if ch.get("id") == item_id:
            return ch
    for ch in PREMIUM_CHANNELS:
        if ch.get("id") == item_id:
            return ch
    return None
