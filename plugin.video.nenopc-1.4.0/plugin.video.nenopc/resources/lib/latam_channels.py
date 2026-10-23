# -*- coding: utf-8 -*-
"""
neno_pc LatAm TV Engine - Televisión en Español Latino de Todos los Países
Cubre los 20 países de Latinoamérica y habla hispana + señales panregionales en español latino.
Combina señales pre-verificadas (carga instantánea) con feeds dinámicos M3U actualizados por país y categoría.
"""

import re
from resources.lib import world_channels
from resources.lib import chile_channels

LATAM_COUNTRIES = [
    {"code": "latam", "name": "Señales Panregionales (Español Latino)", "flag": "🌎", "region": "Panregional"},
    {"code": "cl", "name": "Chile", "flag": "🇨🇱", "region": "Sudamérica"},
    {"code": "ar", "name": "Argentina", "flag": "🇦🇷", "region": "Sudamérica"},
    {"code": "mx", "name": "México", "flag": "🇲🇽", "region": "Norteamérica"},
    {"code": "co", "name": "Colombia", "flag": "🇨🇴", "region": "Sudamérica"},
    {"code": "pe", "name": "Perú", "flag": "🇵🇪", "region": "Sudamérica"},
    {"code": "uy", "name": "Uruguay", "flag": "🇺🇾", "region": "Sudamérica"},
    {"code": "py", "name": "Paraguay", "flag": "🇵🇾", "region": "Sudamérica"},
    {"code": "bo", "name": "Bolivia", "flag": "🇧🇴", "region": "Sudamérica"},
    {"code": "ec", "name": "Ecuador", "flag": "🇪🇨", "region": "Sudamérica"},
    {"code": "ve", "name": "Venezuela", "flag": "🇻🇪", "region": "Sudamérica"},
    {"code": "pa", "name": "Panamá", "flag": "🇵🇦", "region": "Centroamérica"},
    {"code": "cr", "name": "Costa Rica", "flag": "🇨🇷", "region": "Centroamérica"},
    {"code": "sv", "name": "El Salvador", "flag": "🇸🇻", "region": "Centroamérica"},
    {"code": "gt", "name": "Guatemala", "flag": "🇬🇹", "region": "Centroamérica"},
    {"code": "hn", "name": "Honduras", "flag": "🇭🇳", "region": "Centroamérica"},
    {"code": "ni", "name": "Nicaragua", "flag": "🇳🇮", "region": "Centroamérica"},
    {"code": "do", "name": "República Dominicana", "flag": "🇩🇴", "region": "Caribe"},
    {"code": "pr", "name": "Puerto Rico", "flag": "🇵🇷", "region": "Caribe"},
    {"code": "cu", "name": "Cuba", "flag": "🇨🇺", "region": "Caribe"},
    {"code": "es", "name": "España & Señales Hispanas", "flag": "🇪🇸", "region": "Iberoamérica"}
]

LATAM_GENRE_GROUPS = [
    {"id": "deportes", "name": "⚽ Deportes Latinos en Vivo", "keywords": ["sport", "deporte", "futbol", "espn", "tnt", "dsports", "tyc", "fox"]},
    {"id": "noticias", "name": "📡 Noticias y Actualidad Latinoamericana", "keywords": ["news", "noticia", "info", "24", "cnn", "adn", "tn", "c5n", "milenio"]},
    {"id": "cine_series", "name": "🎬 Cine, Series y Telenovelas en Español", "keywords": ["movie", "cine", "serie", "fiction", "ficcion", "novela", "entertainment", "drama"]},
    {"id": "infantil", "name": "🧸 Infantil, Dibujos y Anime en Español Latino", "keywords": ["kid", "infantil", "animation", "animacion", "disney", "cartoon", "nick", "junior"]},
    {"id": "musica", "name": "🎵 Música Latina, Conciertos y Radio TV", "keywords": ["music", "musica", "festival", "radio", "hit", "cumbia", "pop", "rock"]},
    {"id": "cultura", "name": "🌍 Cultura, Documentales y Educación", "keywords": ["cultur", "document", "educa", "travel", "lifestyle", "science", "historia"]},
    {"id": "general", "name": "📺 Canales Nacionales y Regionales Abiertos", "keywords": ["general", "public", "nacional", "regional", "undefined"]}
]

VERIFIED_LATAM_BY_COUNTRY = {
  "ar": [
    {
      "code": "ar",
      "country": "Argentina",
      "name": "Allegro HD (1080p)",
      "category": "Music",
      "url": "http://158.172.155.130:8000/play/a0dn/index.m3u8",
      "logo": "https://i.imgur.com/bRH34Rn.png",
      "id": "latam_ar_1",
      "verified": True
    },
    {
      "code": "ar",
      "country": "Argentina",
      "name": "AMC Series Latin America (1080p)",
      "category": "Series",
      "url": "http://45.171.64.30:6060/play/a005/index.m3u8",
      "logo": "https://amc-series.s3.amazonaws.com/menu/hbfen1Gom0_k1cyqi7rw4-amc-series-train-w.png",
      "id": "latam_ar_2",
      "verified": True
    },
    {
      "code": "ar",
      "country": "Argentina",
      "name": "ABTV Bariloche",
      "category": "General",
      "url": "https://videostream.shockmedia.com.ar/hls/abtvbariloche/abtvbariloche.m3u8",
      "logo": "https://i.imgur.com/l4TSfDr.png",
      "id": "latam_ar_3",
      "verified": True
    },
    {
      "code": "ar",
      "country": "Argentina",
      "name": "America TV (720p)",
      "category": "General",
      "url": "https://prepublish.f.qaotic.net/a07/americahls-100056/playlist_720p.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Am%C3%A9rica_TV_%28Nuevo_logo_Junio_2020%29.png/500px-Am%C3%A9rica_TV_%28Nuevo_logo_Junio_2020%29.png",
      "id": "latam_ar_4",
      "verified": True
    },
    {
      "code": "ar",
      "country": "Argentina",
      "name": "AXN Latin America South",
      "category": "Movies",
      "url": "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/axn.stream/chunks.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/AXN_logo_%282015%29.svg/960px-AXN_logo_%282015%29.svg.png",
      "id": "latam_ar_5",
      "verified": True
    },
    {
      "code": "ar",
      "country": "Argentina",
      "name": "Argentinisima Satelital (540p)",
      "category": "General",
      "url": "https://stream1.sersat.com/hls/argentinisima.m3u8",
      "logo": "https://i.imgur.com/xFgJawa.png",
      "id": "latam_ar_6",
      "verified": True
    },
    {
      "code": "ar",
      "country": "Argentina",
      "name": "5tv",
      "category": "General",
      "url": "https://617c5175c970b.streamlock.net:4444/tvcinco/live1/playlist.m3u8",
      "logo": "https://i.imgur.com/mSn7ACs.png",
      "id": "latam_ar_7",
      "verified": True
    },
    {
      "code": "ar",
      "country": "Argentina",
      "name": "Canal 4 Posadas (1080p)",
      "category": "Undefined",
      "url": "http://190.128.214.97:64333/play/a06l/index.m3u8",
      "logo": "https://i.imgur.com/tElJr3e.png",
      "id": "latam_ar_8",
      "verified": True
    },
    {
      "code": "ar",
      "country": "Argentina",
      "name": "24/7 Canal de Noticias",
      "category": "News",
      "url": "https://panel.host-live.com:19360/cn247tv/cn247tv.m3u8",
      "logo": "https://i.imgur.com/4hDCB1M.png",
      "id": "latam_ar_9",
      "verified": True
    },
    {
      "code": "ar",
      "country": "Argentina",
      "name": "Canal 3 Tacural",
      "category": "General",
      "url": "http://vivo.canal3tacural.com.ar:8081/hls/stream.m3u8",
      "logo": "https://i.imgur.com/RKvSa52.jpeg",
      "id": "latam_ar_10",
      "verified": True
    },
    {
      "code": "ar",
      "country": "Argentina",
      "name": "Azahares Radiovisual Multimedia (720p)",
      "category": "Music",
      "url": "https://streamyes.alsolnet.com/azaharesfm/live/playlist.m3u8",
      "logo": "https://i.imgur.com/g1BFoSs.png",
      "id": "latam_ar_11",
      "verified": True
    },
    {
      "code": "ar",
      "country": "Argentina",
      "name": "Canal 2 Misiones (1080p)",
      "category": "Undefined",
      "url": "https://nd106.republicaservers.com:4433/hls/canal2misioness/index.m3u8",
      "logo": "https://i.imgur.com/YqTNXDf.png",
      "id": "latam_ar_12",
      "verified": True
    },
    {
      "code": "ar",
      "country": "Argentina",
      "name": "Canal 2 NexTV Rafaela (720p)",
      "category": "General",
      "url": "https://edge.enhdtv.com/nexthd/index.m3u8",
      "logo": "https://i.imgur.com/hgj3CaR.jpeg",
      "id": "latam_ar_13",
      "verified": True
    },
    {
      "code": "ar",
      "country": "Argentina",
      "name": "Beats Radio (480p)",
      "category": "Music",
      "url": "https://videostream.shockmedia.com.ar:19360/beatsradio/beatsradio.m3u8",
      "logo": "https://i.imgur.com/zkNUO5p.png",
      "id": "latam_ar_14",
      "verified": True
    },
    {
      "code": "ar",
      "country": "Argentina",
      "name": "Canal 3 La Pampa (1080p)",
      "category": "Undefined",
      "url": "https://stream.arcast.com.ar/c3lapampa/ngrp:c3lapampa_all/playlist.m3u8",
      "logo": "https://i.imgur.com/SsNFudZ.png",
      "id": "latam_ar_15",
      "verified": True
    }
  ],
  "mx": [
    {
      "code": "mx",
      "country": "México",
      "name": "Azteca Deportes Network (1080p)",
      "category": "Sports",
      "url": "http://181.119.66.28:8081/AZTECA-DEPORTES-HD/index.m3u8",
      "logo": "https://match-images.icdb.tv/5913207f2494844101287828e87625eb.jpg",
      "id": "latam_mx_1",
      "verified": True
    },
    {
      "code": "mx",
      "country": "México",
      "name": "AyM Sports (1080p)",
      "category": "Sports",
      "url": "http://168.196.127.137:6001/play/a06v/index.m3u8",
      "logo": "https://i.imgur.com/yu3Bpbd.png",
      "id": "latam_mx_2",
      "verified": True
    },
    {
      "code": "mx",
      "country": "México",
      "name": "Azteca 7 (1080p)",
      "category": "General",
      "url": "http://187.245.231.226:8000/play/a0uz/index.m3u8",
      "logo": "https://i.imgur.com/UtFXjIn.png",
      "id": "latam_mx_3",
      "verified": True
    },
    {
      "code": "mx",
      "country": "México",
      "name": "Bandamax (1080p)",
      "category": "Music",
      "url": "http://181.78.106.127:5000/play/ca064/index.m3u8",
      "logo": "https://i.imgur.com/4DfnOTA.png",
      "id": "latam_mx_4",
      "verified": True
    },
    {
      "code": "mx",
      "country": "México",
      "name": "15TV",
      "category": "General",
      "url": "https://servilive.com:3380/live/v3n6thy7glive.m3u8",
      "logo": "https://i.imgur.com/CZ8LKmA.png",
      "id": "latam_mx_5",
      "verified": True
    },
    {
      "code": "mx",
      "country": "México",
      "name": "Canal 5 (Mexico) XET-TDT (1080p)",
      "category": "General",
      "url": "http://45.5.118.152:8000/play/a03i/index.m3u8",
      "logo": "https://i.imgur.com/cBC2Jre.png",
      "id": "latam_mx_6",
      "verified": True
    },
    {
      "code": "mx",
      "country": "México",
      "name": "bitMe (1080p)",
      "category": "Entertainment",
      "url": "https://cablered.iptvperu.tv:1936/cablered/bitme-srt_new/playlist.m3u8",
      "logo": "https://i.imgur.com/79hrcx8.png",
      "id": "latam_mx_7",
      "verified": True
    },
    {
      "code": "mx",
      "country": "México",
      "name": "Azteca Internacional (1080p)",
      "category": "Entertainment",
      "url": "https://azt-mun.otteravision.com/azt/mun/mun.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Azteca_Internacional_logo_2023.png",
      "id": "latam_mx_8",
      "verified": True
    },
    {
      "code": "mx",
      "country": "México",
      "name": "8NTV (1080p)",
      "category": "General",
      "url": "https://60417ddeaf0d9.streamlock.net/ntv/videontv/playlist.m3u8",
      "logo": "https://i.imgur.com/7ecgGIG.png",
      "id": "latam_mx_9",
      "verified": True
    },
    {
      "code": "mx",
      "country": "México",
      "name": "Alcance TV (Mexico) (720p)",
      "category": "Religious",
      "url": "https://5bf8041cb3fed.streamlock.net/AlcanceTV/AlcanceTV/playlist.m3u8",
      "logo": "https://i.imgur.com/5nYjRlb.png",
      "id": "latam_mx_10",
      "verified": True
    },
    {
      "code": "mx",
      "country": "México",
      "name": "Acustik TV",
      "category": "News",
      "url": "https://s5.mexside.net:1936/clientetv/clientetv/playlist.m3u8",
      "logo": "https://i.imgur.com/dhiNIng.png",
      "id": "latam_mx_11",
      "verified": True
    },
    {
      "code": "mx",
      "country": "México",
      "name": "Canal 5 TV Cozumel (1080p)",
      "category": "General",
      "url": "https://video0.rogohosting.com:19360/tvcozumel/tvcozumel.m3u8",
      "logo": "https://i.imgur.com/0nzNMuP.jpeg",
      "id": "latam_mx_12",
      "verified": True
    },
    {
      "code": "mx",
      "country": "México",
      "name": "B15 Fresnillo (1080p)",
      "category": "General",
      "url": "https://s5.mexside.net:1936/lsac/lsac/playlist.m3u8",
      "logo": "https://i.imgur.com/kaUhEQy.png",
      "id": "latam_mx_13",
      "verified": True
    },
    {
      "code": "mx",
      "country": "México",
      "name": "Antena TV",
      "category": "General",
      "url": "https://5ca9af4645e15.streamlock.net/grd/videogrd/playlist.m3u8",
      "logo": "https://i.imgur.com/1sAgSME.png",
      "id": "latam_mx_14",
      "verified": True
    },
    {
      "code": "mx",
      "country": "México",
      "name": "AMX Noticias (720p) [Not 24/7]",
      "category": "News",
      "url": "https://5e50264bd6766.streamlock.net/mexiquense2/videomexiquense2/playlist.m3u8",
      "logo": "https://i.imgur.com/snIU1UA.jpg",
      "id": "latam_mx_15",
      "verified": True
    }
  ],
  "co": [
    {
      "code": "co",
      "country": "Colombia",
      "name": "AXN Latin America Andes (1080p)",
      "category": "Movies",
      "url": "http://181.78.8.199:8000/play/a0cu/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/AXN_logo_%282015%29.svg/960px-AXN_logo_%282015%29.svg.png",
      "id": "latam_co_1",
      "verified": True
    },
    {
      "code": "co",
      "country": "Colombia",
      "name": "Cablenoticias (1080p)",
      "category": "News",
      "url": "http://181.78.211.244:8005/play/a09u/index.m3u8",
      "logo": "https://i.imgur.com/FfhOGR9.png",
      "id": "latam_co_2",
      "verified": True
    },
    {
      "code": "co",
      "country": "Colombia",
      "name": "Canal 1 (Colombia) (1080p)",
      "category": "General",
      "url": "http://190.109.2.92:8000/play/a010/index.m3u8",
      "logo": "https://i.imgur.com/YFywPLC.png",
      "id": "latam_co_3",
      "verified": True
    },
    {
      "code": "co",
      "country": "Colombia",
      "name": "Canal Institucional (1080p)",
      "category": "General",
      "url": "http://190.61.47.54:8000/play/a00v/index.m3u8",
      "logo": "https://i.imgur.com/hqfQVrU.png",
      "id": "latam_co_4",
      "verified": True
    },
    {
      "code": "co",
      "country": "Colombia",
      "name": "Bethel Colombia (720p)",
      "category": "Religious",
      "url": "http://138.121.15.230:9002/BETHEL/index.m3u8",
      "logo": "https://i.imgur.com/BYdMsLL.png",
      "id": "latam_co_5",
      "verified": True
    },
    {
      "code": "co",
      "country": "Colombia",
      "name": "Canal Dos (720p)",
      "category": "General",
      "url": "http://131.221.41.94/hls/canal2.m3u8",
      "logo": "https://i.imgur.com/BYsyNHZ.jpg",
      "id": "latam_co_6",
      "verified": True
    },
    {
      "code": "co",
      "country": "Colombia",
      "name": "Canal Capital (1080p)",
      "category": "General",
      "url": "http://138.121.15.230:9002/CANAL-CAPITAL/index.m3u8",
      "logo": "https://i.imgur.com/zAYtbYi.png",
      "id": "latam_co_7",
      "verified": True
    },
    {
      "code": "co",
      "country": "Colombia",
      "name": "Aupur Television (1080p)",
      "category": "General",
      "url": "https://canal.aupurtv.co/live/stream/index.m3u8",
      "logo": "https://i.imgur.com/FTv7zpJ.jpeg",
      "id": "latam_co_8",
      "verified": True
    },
    {
      "code": "co",
      "country": "Colombia",
      "name": "Canal RCN (1080p)",
      "category": "General",
      "url": "http://138.121.15.230:9002/RCN/index.m3u8",
      "logo": "https://i.imgur.com/5PhTaHp.png",
      "id": "latam_co_9",
      "verified": True
    },
    {
      "code": "co",
      "country": "Colombia",
      "name": "Canal 2 Alpavision Neiva (720p) [Not 24/7]",
      "category": "General",
      "url": "https://stmv1.voxtvhd.com.br/alpavision/alpavision/playlist.m3u8",
      "logo": "https://i.imgur.com/Yv8XIGW.png",
      "id": "latam_co_10",
      "verified": True
    },
    {
      "code": "co",
      "country": "Colombia",
      "name": "Bendicion Channel (720p)",
      "category": "Religious",
      "url": "https://s.emisoras.tv:8081/bendicionchannel/index.m3u8",
      "logo": "https://i.imgur.com/yKzV7m7.png",
      "id": "latam_co_11",
      "verified": True
    },
    {
      "code": "co",
      "country": "Colombia",
      "name": "Amaga Television (720p)",
      "category": "General",
      "url": "https://viewhn.com/amagatelevision/sdfUYWKegHKRPpSirG/playlist.m3u8",
      "logo": "https://i.imgur.com/hvpbfzG.png",
      "id": "latam_co_12",
      "verified": True
    },
    {
      "code": "co",
      "country": "Colombia",
      "name": "Buenisima Radio TV",
      "category": "Music",
      "url": "https://canal.mediaserver.com.co/live/buenisimatv.m3u8",
      "logo": "https://i.imgur.com/URKDlOZ.png",
      "id": "latam_co_13",
      "verified": True
    },
    {
      "code": "co",
      "country": "Colombia",
      "name": "Canal PyC (720p)",
      "category": "News",
      "url": "https://live20.bozztv.com/akamaissh101/ssh101/pyctelevision/playlist.m3u8",
      "logo": "https://i.imgur.com/3qxBDhV.png",
      "id": "latam_co_14",
      "verified": True
    },
    {
      "code": "co",
      "country": "Colombia",
      "name": "ANC Television (720p)",
      "category": "Entertainment",
      "url": "https://live.amelbatv.co:81/anctvlive/index.m3u8",
      "logo": "https://i.imgur.com/xjTU14t.jpg",
      "id": "latam_co_15",
      "verified": True
    }
  ],
  "pe": [
    {
      "code": "pe",
      "country": "Perú",
      "name": "A&E Latin America (1080p)",
      "category": "Entertainment",
      "url": "http://138.121.15.230:9002/A&E/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/A%26E_Network_logo.svg/960px-A%26E_Network_logo.svg.png",
      "id": "latam_pe_1",
      "verified": True
    },
    {
      "code": "pe",
      "country": "Perú",
      "name": "ATV Sur (1080p)",
      "category": "General",
      "url": "http://190.93.224.42/ATV-SUR/index.m3u8",
      "logo": "https://i.imgur.com/LnyVa5H.png",
      "id": "latam_pe_2",
      "verified": True
    },
    {
      "code": "pe",
      "country": "Perú",
      "name": "Antena 1 (Peru) (1080p)",
      "category": "General",
      "url": "http://bantel-cdn1.iptvperu.tv:1935/btnscrtn/antenauno.stream/playlist.m3u8",
      "logo": "https://i.imgur.com/Bt0yGtw.jpeg",
      "id": "latam_pe_3",
      "verified": True
    },
    {
      "code": "pe",
      "country": "Perú",
      "name": "ATV (Peru) (1080p)",
      "category": "General",
      "url": "http://190.93.224.42/ATV/index.m3u8",
      "logo": "https://i.imgur.com/eUzYZfg.png",
      "id": "latam_pe_4",
      "verified": True
    },
    {
      "code": "pe",
      "country": "Perú",
      "name": "AXN Latin America Andes (1080p)",
      "category": "Movies",
      "url": "http://181.78.8.199:8000/play/a0cu/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/AXN_logo_%282015%29.svg/960px-AXN_logo_%282015%29.svg.png",
      "id": "latam_pe_5",
      "verified": True
    },
    {
      "code": "pe",
      "country": "Perú",
      "name": "Canal IPe (720p)",
      "category": "Family",
      "url": "http://187.102.210.46/IPE/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Identidad_Peruana_ipe_2020.png/960px-Identidad_Peruana_ipe_2020.png",
      "id": "latam_pe_6",
      "verified": True
    },
    {
      "code": "pe",
      "country": "Perú",
      "name": "ATV+ (1080p)",
      "category": "News",
      "url": "http://45.171.108.253:8888/ATV/index.m3u8",
      "logo": "https://i.imgur.com/fY9256H.png",
      "id": "latam_pe_7",
      "verified": True
    },
    {
      "code": "pe",
      "country": "Perú",
      "name": "ABC Teleshow (720p)",
      "category": "General",
      "url": "https://live-evg10.tv360.bitel.com.pe/bitel/abctv/playlist.m3u8",
      "logo": "https://i.imgur.com/cF7gJ2Q.jpeg",
      "id": "latam_pe_8",
      "verified": True
    },
    {
      "code": "pe",
      "country": "Perú",
      "name": "Amazonia TV",
      "category": "General",
      "url": "https://servilive.com:3199/live/amazoniatvlive.m3u8",
      "logo": "https://i.imgur.com/sSW7d8e.png",
      "id": "latam_pe_9",
      "verified": True
    },
    {
      "code": "pe",
      "country": "Perú",
      "name": "36 TV Huacho (720p)",
      "category": "General",
      "url": "https://live-evg10.tv360.bitel.com.pe/bitel/36tvSRT/playlist.m3u8",
      "logo": "https://i.imgur.com/F4NZM3s.jpeg",
      "id": "latam_pe_10",
      "verified": True
    },
    {
      "code": "pe",
      "country": "Perú",
      "name": "AsiriTV (720p) [Not 24/7]",
      "category": "Culture",
      "url": "https://video2.lhdserver.es/asiritv/live.m3u8",
      "logo": "https://i.imgur.com/7bGVFBa.png",
      "id": "latam_pe_11",
      "verified": True
    },
    {
      "code": "pe",
      "country": "Perú",
      "name": "Autentica Television (720p) [Not 24/7]",
      "category": "General",
      "url": "https://live.obslivestream.com/autenticatvmux/index.m3u8",
      "logo": "https://i.imgur.com/bEJK3RN.png",
      "id": "latam_pe_12",
      "verified": True
    },
    {
      "code": "pe",
      "country": "Perú",
      "name": "Canal 8 Catacaos (720p) [Not 24/7]",
      "category": "General",
      "url": "https://live.obslivestream.com/canal8/index.m3u8",
      "logo": "https://i.imgur.com/O5MrFjY.png",
      "id": "latam_pe_13",
      "verified": True
    },
    {
      "code": "pe",
      "country": "Perú",
      "name": "Cadena TV (720p) [Not 24/7]",
      "category": "Undefined",
      "url": "https://tv.bitstreaming.net:3789/live/cdntvlive.m3u8",
      "logo": "https://i.imgur.com/stvzqzd.png",
      "id": "latam_pe_14",
      "verified": True
    },
    {
      "code": "pe",
      "country": "Perú",
      "name": "Cadena TV SD",
      "category": "Undefined",
      "url": "https://live-evg10.tv360.bitel.com.pe/bitel/cadenatv/playlist.m3u8",
      "logo": "https://i.imgur.com/stvzqzd.png",
      "id": "latam_pe_15",
      "verified": True
    }
  ],
  "uy": [
    {
      "code": "uy",
      "country": "Uruguay",
      "name": "AXN Latin America South",
      "category": "Movies",
      "url": "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/axn.stream/chunks.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/AXN_logo_%282015%29.svg/960px-AXN_logo_%282015%29.svg.png",
      "id": "latam_uy_1",
      "verified": True
    },
    {
      "code": "uy",
      "country": "Uruguay",
      "name": "AMC Series Latin America (1080p)",
      "category": "Series",
      "url": "http://45.171.64.30:6060/play/a005/index.m3u8",
      "logo": "https://amc-series.s3.amazonaws.com/menu/hbfen1Gom0_k1cyqi7rw4-amc-series-train-w.png",
      "id": "latam_uy_2",
      "verified": True
    },
    {
      "code": "uy",
      "country": "Uruguay",
      "name": "Cartoon Network Latin America South Atlantic (1080p)",
      "category": "Animation;Kids",
      "url": "http://158.172.217.18:8000/play/a03a/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Cartoon_Network_2010_logo.svg/960px-Cartoon_Network_2010_logo.svg.png",
      "id": "latam_uy_3",
      "verified": True
    },
    {
      "code": "uy",
      "country": "Uruguay",
      "name": "Cartoon Network Latin America",
      "category": "Animation;Kids",
      "url": "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/cartoonnetwork.stream/chunks.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Cartoon_Network_2010_logo.svg/960px-Cartoon_Network_2010_logo.svg.png",
      "id": "latam_uy_4",
      "verified": True
    },
    {
      "code": "uy",
      "country": "Uruguay",
      "name": "Disney Jr. Latin America South HD (1080p)",
      "category": "Animation;Kids",
      "url": "http://bantel-cdn1.iptvperu.tv:1935/btnscrtn/disney_jr.stream/playlist.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e3/2024_Disney_Jr._Logo.svg",
      "id": "latam_uy_5",
      "verified": True
    },
    {
      "code": "uy",
      "country": "Uruguay",
      "name": "Cinecanal South",
      "category": "Movies",
      "url": "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/Cinecanal-key/chunks.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/CinecanalLA.png/960px-CinecanalLA.png",
      "id": "latam_uy_6",
      "verified": True
    },
    {
      "code": "uy",
      "country": "Uruguay",
      "name": "E! Latin America (1080p)",
      "category": "Entertainment;News",
      "url": "http://bantel-cdn1.iptvperu.tv:1935/btnscrtn/entertainment.stream/playlist.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/E%21_Logo_2012.svg/500px-E%21_Logo_2012.svg.png",
      "id": "latam_uy_7",
      "verified": True
    },
    {
      "code": "uy",
      "country": "Uruguay",
      "name": "Disney Channel Latin America Panregional HD (1080p)",
      "category": "Animation;Kids",
      "url": "http://45.134.141.161:2200/ARG/Disney_Channel/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/f/ff/2024_Disney_Channel_text_logo.svg",
      "id": "latam_uy_8",
      "verified": True
    },
    {
      "code": "uy",
      "country": "Uruguay",
      "name": "Canal Mas (720p)",
      "category": "Religious",
      "url": "https://canalmasuruguay.com/hls/master-abr.m3u8",
      "logo": "https://i.imgur.com/gs1L1mW.png",
      "id": "latam_uy_9",
      "verified": True
    },
    {
      "code": "uy",
      "country": "Uruguay",
      "name": "Disney Channel Latin America South",
      "category": "Animation;Kids",
      "url": "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/disney-channel-key/chunks.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/f/ff/2024_Disney_Channel_text_logo.svg",
      "id": "latam_uy_10",
      "verified": True
    },
    {
      "code": "uy",
      "country": "Uruguay",
      "name": "El Gourmet South (1080p)",
      "category": "Cooking",
      "url": "https://iptv.bitred.cl/ELGOURMET_HD/index.m3u8",
      "logo": "https://i.imgur.com/ByMyRI9.png",
      "id": "latam_uy_11",
      "verified": True
    },
    {
      "code": "uy",
      "country": "Uruguay",
      "name": "Disney Jr. Latin America South (1080p)",
      "category": "Animation;Kids",
      "url": "http://45.185.163.75:8000/play/a016/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e3/2024_Disney_Jr._Logo.svg",
      "id": "latam_uy_12",
      "verified": True
    },
    {
      "code": "uy",
      "country": "Uruguay",
      "name": "FX Latin America South",
      "category": "Entertainment",
      "url": "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/fx-key/chunks.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/FX_International_logo.svg/960px-FX_International_logo.svg.png",
      "id": "latam_uy_13",
      "verified": True
    },
    {
      "code": "uy",
      "country": "Uruguay",
      "name": "Pakapaka (1080p)",
      "category": "Kids",
      "url": "http://138.59.227.20:8000/play/a05t/index.m3u8",
      "logo": "https://i.imgur.com/GJbRWwH.png",
      "id": "latam_uy_14",
      "verified": True
    },
    {
      "code": "uy",
      "country": "Uruguay",
      "name": "Comedy Central Latin America (1080p)",
      "category": "Comedy",
      "url": "https://barinaslive1.boldmss.com/COMEDY/COMEDY.isml/COMEDY.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Comedy_Central_2018.svg/960px-Comedy_Central_2018.svg.png",
      "id": "latam_uy_15",
      "verified": True
    }
  ],
  "py": [
    {
      "code": "py",
      "country": "Paraguay",
      "name": "America Paraguay (720p)",
      "category": "General",
      "url": "http://45.170.130.224:8000/play/a02o/index.m3u8?hls",
      "logo": "https://i.imgur.com/rCEu3fM.png",
      "id": "latam_py_1",
      "verified": True
    },
    {
      "code": "py",
      "country": "Paraguay",
      "name": "AMC Series Latin America (1080p)",
      "category": "Series",
      "url": "http://45.171.64.30:6060/play/a005/index.m3u8",
      "logo": "https://amc-series.s3.amazonaws.com/menu/hbfen1Gom0_k1cyqi7rw4-amc-series-train-w.png",
      "id": "latam_py_2",
      "verified": True
    },
    {
      "code": "py",
      "country": "Paraguay",
      "name": "Alt Media TV",
      "category": "Entertainment",
      "url": "https://video.hostingcaaguazu.com:19360/altmedia/altmedia.m3u8",
      "logo": "https://i.imgur.com/YkOgWMc.png",
      "id": "latam_py_3",
      "verified": True
    },
    {
      "code": "py",
      "country": "Paraguay",
      "name": "AGR FM TV",
      "category": "General",
      "url": "https://tigocloud.desdeparaguay.net/agrtv/agrtv/playlist.m3u8",
      "logo": "https://i.imgur.com/tg6EjTU.png",
      "id": "latam_py_4",
      "verified": True
    },
    {
      "code": "py",
      "country": "Paraguay",
      "name": "AXN Latin America South",
      "category": "Movies",
      "url": "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/axn.stream/chunks.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/AXN_logo_%282015%29.svg/960px-AXN_logo_%282015%29.svg.png",
      "id": "latam_py_5",
      "verified": True
    },
    {
      "code": "py",
      "country": "Paraguay",
      "name": "Alcance FM PLAY TV",
      "category": "Music",
      "url": "https://video.wilohosting.com:19360/alcancefmtv/alcancefmtv.m3u8",
      "logo": "https://i.imgur.com/ymcWecA.png",
      "id": "latam_py_6",
      "verified": True
    },
    {
      "code": "py",
      "country": "Paraguay",
      "name": "Cartoon Network Latin America South Atlantic (1080p)",
      "category": "Animation;Kids",
      "url": "http://158.172.217.18:8000/play/a03a/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Cartoon_Network_2010_logo.svg/960px-Cartoon_Network_2010_logo.svg.png",
      "id": "latam_py_7",
      "verified": True
    },
    {
      "code": "py",
      "country": "Paraguay",
      "name": "Disney Channel Latin America Panregional HD (1080p)",
      "category": "Animation;Kids",
      "url": "http://45.134.141.161:2200/ARG/Disney_Channel/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/f/ff/2024_Disney_Channel_text_logo.svg",
      "id": "latam_py_8",
      "verified": True
    },
    {
      "code": "py",
      "country": "Paraguay",
      "name": "4Dmas Noticias TV (1080p) [Not 24/7]",
      "category": "News",
      "url": "https://rds3.desdeparaguay.net/4dmasnoticiastv/4dmasnoticiastv/playlist.m3u8",
      "logo": "https://i.ibb.co/1fb5BtN/unnamed.png",
      "id": "latam_py_9",
      "verified": True
    },
    {
      "code": "py",
      "country": "Paraguay",
      "name": "Disney Jr. Latin America South HD (1080p)",
      "category": "Animation;Kids",
      "url": "http://bantel-cdn1.iptvperu.tv:1935/btnscrtn/disney_jr.stream/playlist.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e3/2024_Disney_Jr._Logo.svg",
      "id": "latam_py_10",
      "verified": True
    },
    {
      "code": "py",
      "country": "Paraguay",
      "name": "E! Latin America (1080p)",
      "category": "Entertainment;News",
      "url": "http://bantel-cdn1.iptvperu.tv:1935/btnscrtn/entertainment.stream/playlist.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/E%21_Logo_2012.svg/500px-E%21_Logo_2012.svg.png",
      "id": "latam_py_11",
      "verified": True
    },
    {
      "code": "py",
      "country": "Paraguay",
      "name": "Bruno Masi TV (720p)",
      "category": "General",
      "url": "https://rds3.desdeparaguay.net/brunomasitv/brunomasitv/playlist.m3u8",
      "logo": "https://i.ibb.co/QFmyjZN/unnamed-1.png",
      "id": "latam_py_12",
      "verified": True
    },
    {
      "code": "py",
      "country": "Paraguay",
      "name": "Educanal (1080p)",
      "category": "Education",
      "url": "http://190.128.214.97:64333/play/a011/index.m3u8",
      "logo": "https://i.imgur.com/857OkFf.png",
      "id": "latam_py_13",
      "verified": True
    },
    {
      "code": "py",
      "country": "Paraguay",
      "name": "El Gourmet South (1080p)",
      "category": "Cooking",
      "url": "https://iptv.bitred.cl/ELGOURMET_HD/index.m3u8",
      "logo": "https://i.imgur.com/ByMyRI9.png",
      "id": "latam_py_14",
      "verified": True
    },
    {
      "code": "py",
      "country": "Paraguay",
      "name": "Canal 8 Vision TV (1080p)",
      "category": "General",
      "url": "https://tigocloudgen.desdeparaguay.net/satelitaltv/satelitaltv/playlist.m3u8",
      "logo": "https://i.imgur.com/mKju6hk.png",
      "id": "latam_py_15",
      "verified": True
    }
  ],
  "bo": [
    {
      "code": "bo",
      "country": "Bolivia",
      "name": "A&E Latin America (1080p)",
      "category": "Entertainment",
      "url": "http://138.121.15.230:9002/A&E/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/A%26E_Network_logo.svg/960px-A%26E_Network_logo.svg.png",
      "id": "latam_bo_1",
      "verified": True
    },
    {
      "code": "bo",
      "country": "Bolivia",
      "name": "Bolivia TV (1080p)",
      "category": "General",
      "url": "http://190.181.61.93:8000/play/a001/index.m3u8",
      "logo": "https://i.imgur.com/tKLYYys.png",
      "id": "latam_bo_2",
      "verified": True
    },
    {
      "code": "bo",
      "country": "Bolivia",
      "name": "AXN Latin America Andes (1080p)",
      "category": "Movies",
      "url": "http://181.78.8.199:8000/play/a0cu/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/AXN_logo_%282015%29.svg/960px-AXN_logo_%282015%29.svg.png",
      "id": "latam_bo_3",
      "verified": True
    },
    {
      "code": "bo",
      "country": "Bolivia",
      "name": "Canal 56 Quiero TV (720p)",
      "category": "General",
      "url": "http://45.5.118.152:8000/play/a08z/index.m3u8",
      "logo": "https://i.imgur.com/l9kDNld.jpeg",
      "id": "latam_bo_4",
      "verified": True
    },
    {
      "code": "bo",
      "country": "Bolivia",
      "name": "Cinecanal Pacific (1080p)",
      "category": "Movies",
      "url": "http://138.121.15.230:9002/CINECANAL/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/CinecanalLA.png/960px-CinecanalLA.png",
      "id": "latam_bo_5",
      "verified": True
    },
    {
      "code": "bo",
      "country": "Bolivia",
      "name": "Cartoon Network Latin America South Pacific (576p)",
      "category": "Animation;Kids",
      "url": "http://45.167.1.138:8000/play/a00w",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Cartoon_Network_2010_logo.svg/960px-Cartoon_Network_2010_logo.svg.png",
      "id": "latam_bo_6",
      "verified": True
    },
    {
      "code": "bo",
      "country": "Bolivia",
      "name": "Disney Channel Latin America Panregional HD (1080p)",
      "category": "Animation;Kids",
      "url": "http://45.134.141.161:2200/ARG/Disney_Channel/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/f/ff/2024_Disney_Channel_text_logo.svg",
      "id": "latam_bo_7",
      "verified": True
    },
    {
      "code": "bo",
      "country": "Bolivia",
      "name": "Disney Jr. Latin America South HD (1080p)",
      "category": "Animation;Kids",
      "url": "http://bantel-cdn1.iptvperu.tv:1935/btnscrtn/disney_jr.stream/playlist.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e3/2024_Disney_Jr._Logo.svg",
      "id": "latam_bo_8",
      "verified": True
    },
    {
      "code": "bo",
      "country": "Bolivia",
      "name": "Discovery Channel Latin America (1080p)",
      "category": "Entertainment",
      "url": "http://45.171.64.30:6060/play/a032/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/2019_Discovery_logo.svg/960px-2019_Discovery_logo.svg.png",
      "id": "latam_bo_9",
      "verified": True
    },
    {
      "code": "bo",
      "country": "Bolivia",
      "name": "Disney Jr. Latin America South (1080p)",
      "category": "Animation;Kids",
      "url": "http://45.185.163.75:8000/play/a016/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e3/2024_Disney_Jr._Logo.svg",
      "id": "latam_bo_10",
      "verified": True
    },
    {
      "code": "bo",
      "country": "Bolivia",
      "name": "Audiokiss (1080p)",
      "category": "Music",
      "url": "https://master.tucableip.com/audiokisstv/index.m3u8",
      "logo": "https://www.audiokiss.com/audiokiss/wp-content/uploads/sites/4/2021/02/Audio_kiss800-768x405.png",
      "id": "latam_bo_11",
      "verified": True
    },
    {
      "code": "bo",
      "country": "Bolivia",
      "name": "Disney Channel Latin America South",
      "category": "Animation;Kids",
      "url": "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/disney-channel-key/chunks.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/f/ff/2024_Disney_Channel_text_logo.svg",
      "id": "latam_bo_12",
      "verified": True
    },
    {
      "code": "bo",
      "country": "Bolivia",
      "name": "Comedy Central Latin America (1080p)",
      "category": "Comedy",
      "url": "https://barinaslive1.boldmss.com/COMEDY/COMEDY.isml/COMEDY.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Comedy_Central_2018.svg/960px-Comedy_Central_2018.svg.png",
      "id": "latam_bo_13",
      "verified": True
    },
    {
      "code": "bo",
      "country": "Bolivia",
      "name": "As Contenidos (720p)",
      "category": "General",
      "url": "https://master.tucableip.com/ascontenido/index.m3u8",
      "logo": "https://ascontenidos.com.bo/wp-content/uploads/2023/07/cropped-logo512.png",
      "id": "latam_bo_14",
      "verified": True
    },
    {
      "code": "bo",
      "country": "Bolivia",
      "name": "Coral TV (720p)",
      "category": "General",
      "url": "https://tv.mediacp.eu:8081/coraltv/index.m3u8",
      "logo": "https://i.ibb.co/xDrc5MD/CORALTv.png",
      "id": "latam_bo_15",
      "verified": True
    }
  ],
  "ec": [
    {
      "code": "ec",
      "country": "Ecuador",
      "name": "A&E Latin America (1080p)",
      "category": "Entertainment",
      "url": "http://138.121.15.230:9002/A&E/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/A%26E_Network_logo.svg/960px-A%26E_Network_logo.svg.png",
      "id": "latam_ec_1",
      "verified": True
    },
    {
      "code": "ec",
      "country": "Ecuador",
      "name": "AXN Latin America Andes (1080p)",
      "category": "Movies",
      "url": "http://181.78.8.199:8000/play/a0cu/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/AXN_logo_%282015%29.svg/960px-AXN_logo_%282015%29.svg.png",
      "id": "latam_ec_2",
      "verified": True
    },
    {
      "code": "ec",
      "country": "Ecuador",
      "name": "Disney Channel Latin America Panregional HD (1080p)",
      "category": "Animation;Kids",
      "url": "http://45.134.141.161:2200/ARG/Disney_Channel/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/f/ff/2024_Disney_Channel_text_logo.svg",
      "id": "latam_ec_3",
      "verified": True
    },
    {
      "code": "ec",
      "country": "Ecuador",
      "name": "Disney Jr. Latin America South HD (1080p)",
      "category": "Animation;Kids",
      "url": "http://bantel-cdn1.iptvperu.tv:1935/btnscrtn/disney_jr.stream/playlist.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e3/2024_Disney_Jr._Logo.svg",
      "id": "latam_ec_4",
      "verified": True
    },
    {
      "code": "ec",
      "country": "Ecuador",
      "name": "Cartoon Network Latin America South Pacific (576p)",
      "category": "Animation;Kids",
      "url": "http://45.167.1.138:8000/play/a00w",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Cartoon_Network_2010_logo.svg/960px-Cartoon_Network_2010_logo.svg.png",
      "id": "latam_ec_5",
      "verified": True
    },
    {
      "code": "ec",
      "country": "Ecuador",
      "name": "Discovery Channel Latin America (1080p)",
      "category": "Entertainment",
      "url": "http://45.171.64.30:6060/play/a032/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/2019_Discovery_logo.svg/960px-2019_Discovery_logo.svg.png",
      "id": "latam_ec_6",
      "verified": True
    },
    {
      "code": "ec",
      "country": "Ecuador",
      "name": "Disney Channel Latin America South",
      "category": "Animation;Kids",
      "url": "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/disney-channel-key/chunks.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/f/ff/2024_Disney_Channel_text_logo.svg",
      "id": "latam_ec_7",
      "verified": True
    },
    {
      "code": "ec",
      "country": "Ecuador",
      "name": "Bacan Te Veo (360p)",
      "category": "Entertainment",
      "url": "https://stmv6.voxtvhd.com.br/vacantveo2/vacantveo2/playlist.m3u8",
      "logo": "https://i.imgur.com/m1LK6rY.png",
      "id": "latam_ec_8",
      "verified": True
    },
    {
      "code": "ec",
      "country": "Ecuador",
      "name": "Antena Uno Radiovideo (360p)",
      "category": "Undefined",
      "url": "https://tvdatta.com:3578/live/antenaunolive.m3u8",
      "logo": "https://i.imgur.com/PCN6iZJ.png",
      "id": "latam_ec_9",
      "verified": True
    },
    {
      "code": "ec",
      "country": "Ecuador",
      "name": "Austral TV (1080p)",
      "category": "General",
      "url": "https://stmv3.voxtvhd.com.br/australtv/australtv/playlist.m3u8",
      "logo": "https://i.imgur.com/zgGuCYL.png",
      "id": "latam_ec_10",
      "verified": True
    },
    {
      "code": "ec",
      "country": "Ecuador",
      "name": "Ecuador TV (1080p)",
      "category": "General",
      "url": "http://45.224.97.181:9999/EcuadorTV/index.m3u8",
      "logo": "https://i.imgur.com/hj6EYwe.png",
      "id": "latam_ec_11",
      "verified": True
    },
    {
      "code": "ec",
      "country": "Ecuador",
      "name": "America Estereo Ibarra (720p)",
      "category": "General",
      "url": "https://video.makrodigital.com/americaestereoibarra/americaestereoibarra/playlist.m3u8",
      "logo": "https://i.imgur.com/gUqKymM.png",
      "id": "latam_ec_12",
      "verified": True
    },
    {
      "code": "ec",
      "country": "Ecuador",
      "name": "Comedy Central Latin America (1080p)",
      "category": "Comedy",
      "url": "https://barinaslive1.boldmss.com/COMEDY/COMEDY.isml/COMEDY.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Comedy_Central_2018.svg/960px-Comedy_Central_2018.svg.png",
      "id": "latam_ec_13",
      "verified": True
    },
    {
      "code": "ec",
      "country": "Ecuador",
      "name": "America Estereo Tulcan (614p)",
      "category": "General",
      "url": "https://video.makrodigital.com/americaestereotulcan/americaestereotulcan/playlist.m3u8",
      "logo": "https://i.imgur.com/gUqKymM.png",
      "id": "latam_ec_14",
      "verified": True
    },
    {
      "code": "ec",
      "country": "Ecuador",
      "name": "Asomavision (614p)",
      "category": "Religious",
      "url": "https://asomatv.cloud-ip.cc/livestream/stream.m3u8",
      "logo": "https://i.imgur.com/VqwyCV1.png",
      "id": "latam_ec_15",
      "verified": True
    }
  ],
  "ve": [
    {
      "code": "ve",
      "country": "Venezuela",
      "name": "ANTV (Venezuela) (720p)",
      "category": "Legislative",
      "url": "http://181.78.8.199:8000/play/a0fo/index.m3u8",
      "logo": "https://i.imgur.com/Qm88HT0.png",
      "id": "latam_ve_1",
      "verified": True
    },
    {
      "code": "ve",
      "country": "Venezuela",
      "name": "BTA TV (720p)",
      "category": "Music",
      "url": "https://cloud.fastchannel.es/manifiest/hls/prog9/btatv.m3u8",
      "logo": "https://i.imgur.com/vygOosC.png",
      "id": "latam_ve_2",
      "verified": True
    },
    {
      "code": "ve",
      "country": "Venezuela",
      "name": "Canal I (1080p)",
      "category": "News",
      "url": "https://streaming.canal-i.com/canal-i/live/master.m3u8",
      "logo": "https://i.imgur.com/vKfOavW.png",
      "id": "latam_ve_3",
      "verified": True
    },
    {
      "code": "ve",
      "country": "Venezuela",
      "name": "Aguacate TV (1080p)",
      "category": "Entertainment",
      "url": "https://streamtv.intervenhosting.net:3040/hybrid/play.m3u8",
      "logo": "https://i.ibb.co/wpWBsgf/IMG-20230705-154622.jpg",
      "id": "latam_ve_4",
      "verified": True
    },
    {
      "code": "ve",
      "country": "Venezuela",
      "name": "Disney Channel Latin America Panregional HD (1080p)",
      "category": "Animation;Kids",
      "url": "http://45.134.141.161:2200/ARG/Disney_Channel/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/f/ff/2024_Disney_Channel_text_logo.svg",
      "id": "latam_ve_5",
      "verified": True
    },
    {
      "code": "ve",
      "country": "Venezuela",
      "name": "Disney Channel Latin America Center (1080p)",
      "category": "Animation;Kids",
      "url": "http://181.78.8.199:8000/play/a0dn/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/f/ff/2024_Disney_Channel_text_logo.svg",
      "id": "latam_ve_6",
      "verified": True
    },
    {
      "code": "ve",
      "country": "Venezuela",
      "name": "Canal 21 Tachira (360p)",
      "category": "General",
      "url": "https://stmv2.voxtvhd.com.br/canal21/canal21/playlist.m3u8",
      "logo": "https://i.imgur.com/7Tb7CF4.jpg",
      "id": "latam_ve_7",
      "verified": True
    },
    {
      "code": "ve",
      "country": "Venezuela",
      "name": "Catatumbo TV (406p)",
      "category": "General",
      "url": "https://cloud.fastchannel.es/manifiest/hls/prog9/catatumbotv.m3u8",
      "logo": "https://i.imgur.com/LBI2la0.png",
      "id": "latam_ve_8",
      "verified": True
    },
    {
      "code": "ve",
      "country": "Venezuela",
      "name": "Disney Jr. Latin America North HD (1080p)",
      "category": "Animation;Kids",
      "url": "http://181.78.14.26:4000/play/a073/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e3/2024_Disney_Jr._Logo.svg",
      "id": "latam_ve_9",
      "verified": True
    },
    {
      "code": "ve",
      "country": "Venezuela",
      "name": "AS3 Sport TV (1080p)",
      "category": "Sports",
      "url": "https://streamtv.as3sport.online:3394/hybrid/play.m3u8",
      "logo": "https://i.ibb.co/bRmGbsyV/A3-SPORTTV.jpg",
      "id": "latam_ve_10",
      "verified": True
    },
    {
      "code": "ve",
      "country": "Venezuela",
      "name": "ESPN Latin America Colombia (1080p)",
      "category": "Sports",
      "url": "http://190.61.47.54:8000/play/a004/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/ESPN_wordmark.svg/960px-ESPN_wordmark.svg.png",
      "id": "latam_ve_11",
      "verified": True
    },
    {
      "code": "ve",
      "country": "Venezuela",
      "name": "Globovision (576p)",
      "category": "General",
      "url": "http://181.78.8.199:8000/play/a09k/index.m3u8",
      "logo": "https://i.imgur.com/v6nRdxQ.png",
      "id": "latam_ve_12",
      "verified": True
    },
    {
      "code": "ve",
      "country": "Venezuela",
      "name": "Anzoategui TV (360p) [Not 24/7]",
      "category": "General",
      "url": "https://vcp2.myplaytv.com/anzoateguitv/anzoateguitv/playlist.m3u8",
      "logo": "https://i.imgur.com/SLqrEOz.png",
      "id": "latam_ve_13",
      "verified": True
    },
    {
      "code": "ve",
      "country": "Venezuela",
      "name": "Disney Jr. Latin America (1080p)",
      "category": "Animation;Kids",
      "url": "http://190.14.10.19:16000/play/a02d/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e3/2024_Disney_Jr._Logo.svg",
      "id": "latam_ve_14",
      "verified": True
    },
    {
      "code": "ve",
      "country": "Venezuela",
      "name": "Comedy Central Latin America (1080p)",
      "category": "Comedy",
      "url": "https://barinaslive1.boldmss.com/COMEDY/COMEDY.isml/COMEDY.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Comedy_Central_2018.svg/960px-Comedy_Central_2018.svg.png",
      "id": "latam_ve_15",
      "verified": True
    }
  ],
  "pa": [
    {
      "code": "pa",
      "country": "Panamá",
      "name": "A&R Canal (720p)",
      "category": "Religious",
      "url": "http://51.222.9.192:3589/stream/play.m3u8",
      "logo": "https://i.imgur.com/ejRJqSI.png",
      "id": "latam_pa_1",
      "verified": True
    },
    {
      "code": "pa",
      "country": "Panamá",
      "name": "AXN Latin America (1080p)",
      "category": "Movies",
      "url": "http://138.121.15.230:9002/AXN/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/AXN_logo_%282015%29.svg/960px-AXN_logo_%282015%29.svg.png",
      "id": "latam_pa_2",
      "verified": True
    },
    {
      "code": "pa",
      "country": "Panamá",
      "name": "Discovery Channel Latin America (1080p)",
      "category": "Entertainment",
      "url": "http://45.171.64.30:6060/play/a032/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/2019_Discovery_logo.svg/960px-2019_Discovery_logo.svg.png",
      "id": "latam_pa_3",
      "verified": True
    },
    {
      "code": "pa",
      "country": "Panamá",
      "name": "Hosanna Vision (720p) [Not 24/7]",
      "category": "Religious",
      "url": "https://1206618505.rsc.cdn77.org/LS-ATL-59020-1/playlist.m3u8",
      "logo": "https://i.imgur.com/v0tc51l.png",
      "id": "latam_pa_4",
      "verified": True
    },
    {
      "code": "pa",
      "country": "Panamá",
      "name": "Comedy Central Latin America (1080p)",
      "category": "Comedy",
      "url": "https://barinaslive1.boldmss.com/COMEDY/COMEDY.isml/COMEDY.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Comedy_Central_2018.svg/960px-Comedy_Central_2018.svg.png",
      "id": "latam_pa_5",
      "verified": True
    },
    {
      "code": "pa",
      "country": "Panamá",
      "name": "TNT Series Latin America (1080p)",
      "category": "Series",
      "url": "http://168.196.127.137:6001/play/a095/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/7/75/TNT_Series_Logo_2016.png",
      "id": "latam_pa_6",
      "verified": True
    },
    {
      "code": "pa",
      "country": "Panamá",
      "name": "TNT Latin America (1080p)",
      "category": "Undefined",
      "url": "http://45.171.64.30:6060/play/a03i/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/TNT_Logo_2016.svg/960px-TNT_Logo_2016.svg.png",
      "id": "latam_pa_7",
      "verified": True
    },
    {
      "code": "pa",
      "country": "Panamá",
      "name": "Telemetro (720p)",
      "category": "General",
      "url": "http://181.78.121.15:8000/play/a001/index.m3u8",
      "logo": "https://i.imgur.com/vJJrGgV.png",
      "id": "latam_pa_8",
      "verified": True
    },
    {
      "code": "pa",
      "country": "Panamá",
      "name": "Vision Latina (1080p)",
      "category": "Religious",
      "url": "https://cdn-cloudfront.us-east-1.prod.ingest.aws-infra.dacast.com/live/64917431-2f51-0a46-d4d0-04d111b2393f/master.m3u8",
      "logo": "https://i.imgur.com/TG30lWA.jpg",
      "id": "latam_pa_9",
      "verified": True
    },
    {
      "code": "pa",
      "country": "Panamá",
      "name": "Planet 100.9 FM (1080p)",
      "category": "Music",
      "url": "https://streamlov.alsolnet.com/planet1009fm/live/playlist.m3u8",
      "logo": "https://i.imgur.com/8ZIBs8l.png",
      "id": "latam_pa_10",
      "verified": True
    },
    {
      "code": "pa",
      "country": "Panamá",
      "name": "Dreiko TV (720p) [Not 24/7]",
      "category": "Animation",
      "url": "https://cloudvideo.servers10.com:8081/8020/index.m3u8",
      "logo": "https://i.imgur.com/k8U0e0b.png",
      "id": "latam_pa_11",
      "verified": True
    },
    {
      "code": "pa",
      "country": "Panamá",
      "name": "Corazon TV",
      "category": "Music",
      "url": "https://sistemastr.tropicalmoonmedia.com/live/7FFCFEC3978B68D1A2ED0A38DE96AF76/12.m3u8",
      "logo": "https://i.imgur.com/HVdbXku.png",
      "id": "latam_pa_12",
      "verified": True
    },
    {
      "code": "pa",
      "country": "Panamá",
      "name": "Radio Hogar (720p)",
      "category": "Religious",
      "url": "https://www.streaming507.net:19360/videoradiohogar/videoradiohogar.m3u8",
      "logo": "https://i.imgur.com/P4A1Zwl.jpg",
      "id": "latam_pa_13",
      "verified": True
    },
    {
      "code": "pa",
      "country": "Panamá",
      "name": "Fabulosa Estereo 100.5 FM (720p)",
      "category": "Music",
      "url": "https://www.streaming507.net:19360/videofabulosa/videofabulosa.m3u8",
      "logo": "https://i.imgur.com/YFmzkOp.png",
      "id": "latam_pa_14",
      "verified": True
    },
    {
      "code": "pa",
      "country": "Panamá",
      "name": "Tropi Q 99.7 FM (1080p)",
      "category": "Music",
      "url": "https://www.streaming507.net:19360/videotropiq/videotropiq.m3u8",
      "logo": "https://i.imgur.com/5rPdHhb.png",
      "id": "latam_pa_15",
      "verified": True
    }
  ],
  "cr": [
    {
      "code": "cr",
      "country": "Costa Rica",
      "name": "88 Stereo (720p) [Not 24/7]",
      "category": "Music",
      "url": "http://k3.usastreams.com/CableLatino/88stereo/playlist.m3u8",
      "logo": "https://i.imgur.com/i3YwORV.png",
      "id": "latam_cr_1",
      "verified": True
    },
    {
      "code": "cr",
      "country": "Costa Rica",
      "name": "FUTV",
      "category": "Sports",
      "url": "http://190.61.90.17:40000/play/a03v/index.m3u8",
      "logo": "https://i.imgur.com/f8BkLql.png",
      "id": "latam_cr_2",
      "verified": True
    },
    {
      "code": "cr",
      "country": "Costa Rica",
      "name": "BestClasicosTV (720p) [Not 24/7]",
      "category": "Undefined",
      "url": "https://acceso.mediosdecostarica.com:3873/hybrid/play.m3u8",
      "logo": "https://i.imgur.com/a/BRb8AVL.png",
      "id": "latam_cr_3",
      "verified": True
    },
    {
      "code": "cr",
      "country": "Costa Rica",
      "name": "Canal 3 KMK TV (720p)",
      "category": "Music",
      "url": "https://live20.bozztv.com/giatv/giatv-KMKTV/KMKTV/chunks.m3u8",
      "logo": "https://i.imgur.com/sgRDRBK.jpg",
      "id": "latam_cr_4",
      "verified": True
    },
    {
      "code": "cr",
      "country": "Costa Rica",
      "name": "Antena Seis TV (720p) [Geo-blocked]",
      "category": "General",
      "url": "https://video1.azulstream.com:8081/antenaseistv/index.m3u8",
      "logo": "https://i.imgur.com/9Nh2mo9.png",
      "id": "latam_cr_5",
      "verified": True
    },
    {
      "code": "cr",
      "country": "Costa Rica",
      "name": "Canal 8 (720p) [Not 24/7]",
      "category": "General",
      "url": "https://mdstrm.com/live-stream-playlist/5a7b1e63a8da282c34d65445.m3u8",
      "logo": "https://i.imgur.com/nefPi2Y.png",
      "id": "latam_cr_6",
      "verified": True
    },
    {
      "code": "cr",
      "country": "Costa Rica",
      "name": "Costa Rica Channel (576p) [Not 24/7]",
      "category": "Culture;Travel",
      "url": "https://video0.rogohosting.com:19360/8006/8006.m3u8",
      "logo": "https://i.imgur.com/N4pFVVF.png",
      "id": "latam_cr_7",
      "verified": True
    },
    {
      "code": "cr",
      "country": "Costa Rica",
      "name": "¡OPA! (720p)",
      "category": "Entertainment",
      "url": "https://5f1af61612fb5.streamlock.net/genteopa/videogenteopa_720p/playlist.m3u8",
      "logo": "https://i.imgur.com/300c1ZH.png",
      "id": "latam_cr_8",
      "verified": True
    },
    {
      "code": "cr",
      "country": "Costa Rica",
      "name": "360 RFTV (576p) [Geo-blocked]",
      "category": "General",
      "url": "https://acceso.mediosdecostarica.com:3638/live/360rftvcrlive.m3u8",
      "logo": "https://i.imgur.com/EBtgnxR.png",
      "id": "latam_cr_9",
      "verified": True
    },
    {
      "code": "cr",
      "country": "Costa Rica",
      "name": "Limon TV (1080p) [Not 24/7]",
      "category": "General",
      "url": "http://k4.usastreams.com/limontv1/limontv1/playlist.m3u8",
      "logo": "https://i.ibb.co/rdpcv7C/1689421727166.jpg",
      "id": "latam_cr_10",
      "verified": True
    },
    {
      "code": "cr",
      "country": "Costa Rica",
      "name": "Canal 10 (Costa Rica) (720p) [Not 24/7]",
      "category": "General",
      "url": "https://acceso.mediosdecostarica.com:3606/hybrid/play.m3u8",
      "logo": "https://i.imgur.com/TO6WQbW.png",
      "id": "latam_cr_11",
      "verified": True
    },
    {
      "code": "cr",
      "country": "Costa Rica",
      "name": "Canal 1 (Costa Rica) (720p) [Not 24/7]",
      "category": "General",
      "url": "https://vid.canal1cr.com:3424/multi_live/play_720.m3u8",
      "logo": "https://i.ibb.co/KhNS8Dy/cropped-logoo-1.png",
      "id": "latam_cr_12",
      "verified": True
    },
    {
      "code": "cr",
      "country": "Costa Rica",
      "name": "Colosal TV",
      "category": "Entertainment",
      "url": "https://5eac7b031d945.streamlock.net/COLOSAL/COLOSAL/playlist.m3u8",
      "logo": "https://i.imgur.com/0DZB3eB.png",
      "id": "latam_cr_13",
      "verified": True
    },
    {
      "code": "cr",
      "country": "Costa Rica",
      "name": "Conexion Positiva Television",
      "category": "Religious",
      "url": "https://tvstream.conexionpositivaradio.com/memfs/69239c4d-4116-4f4f-b065-bf17e81b1411.m3u8",
      "logo": "https://i.ibb.co/HSSyRDs/conexion-positiva.png",
      "id": "latam_cr_14",
      "verified": True
    },
    {
      "code": "cr",
      "country": "Costa Rica",
      "name": "Guatuso TV",
      "category": "General",
      "url": "https://5cf4a2c2512a2.streamlock.net/8176/8176/playlist.m3u8",
      "logo": "https://www.grupodgrajal.com/images/logoguatusochannel.png",
      "id": "latam_cr_15",
      "verified": True
    }
  ],
  "sv": [
    {
      "code": "sv",
      "country": "El Salvador",
      "name": "Canal 12 (576p)",
      "category": "General",
      "url": "http://186.33.26.18:8000/play/a0nw/index.m3u8",
      "logo": "https://i.imgur.com/WMv3yEf.png",
      "id": "latam_sv_1",
      "verified": True
    },
    {
      "code": "sv",
      "country": "El Salvador",
      "name": "Canal 2 (El Salvador) (720p)",
      "category": "General",
      "url": "http://186.33.26.18:8000/play/a0qp/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Canal_2_TCS.png/960px-Canal_2_TCS.png",
      "id": "latam_sv_2",
      "verified": True
    },
    {
      "code": "sv",
      "country": "El Salvador",
      "name": "Canal 3 Impresionante (480p)",
      "category": "General",
      "url": "https://cloud2.streaminglivehd.com:2020/hls/8036/8036.m3u8",
      "logo": "https://i.imgur.com/mdfiWG9.png",
      "id": "latam_sv_3",
      "verified": True
    },
    {
      "code": "sv",
      "country": "El Salvador",
      "name": "Canal 10 (El Salvador) (720p)",
      "category": "General",
      "url": "https://5ca3e84a76d30.streamlock.net/tves/videotves/playlist.m3u8",
      "logo": "https://i.imgur.com/y2ppMnY.png",
      "id": "latam_sv_4",
      "verified": True
    },
    {
      "code": "sv",
      "country": "El Salvador",
      "name": "Agape TV (720p)",
      "category": "Religious",
      "url": "https://5fc584f3f19c9.streamlock.net/agape/smil:agape.smil/playlist.m3u8",
      "logo": "https://i.imgur.com/DsGmrnc.png",
      "id": "latam_sv_5",
      "verified": True
    },
    {
      "code": "sv",
      "country": "El Salvador",
      "name": "Canal 11 TuTV (349p)",
      "category": "General",
      "url": "https://stream.giostreaming.app/canal11/canal11.m3u8",
      "logo": "https://i.imgur.com/itqQEux.png",
      "id": "latam_sv_6",
      "verified": True
    },
    {
      "code": "sv",
      "country": "El Salvador",
      "name": "RTV Canal 57 (720p)",
      "category": "General",
      "url": "https://stream.giostreaming.app/rtvcanal57/rtvcanal57.m3u8",
      "logo": "https://i.imgur.com/tnOGWqL.png",
      "id": "latam_sv_7",
      "verified": True
    },
    {
      "code": "sv",
      "country": "El Salvador",
      "name": "Elim TV (720p)",
      "category": "Religious",
      "url": "https://stream.soporteccrtv.xyz/live/elimtv/main_stream.m3u8",
      "logo": "https://i.imgur.com/payIg0N.png",
      "id": "latam_sv_8",
      "verified": True
    },
    {
      "code": "sv",
      "country": "El Salvador",
      "name": "SolTV (El Salvador) (720p)",
      "category": "General",
      "url": "https://videostream.shockmedia.com.ar/hls/canalsoltv/canalsoltv.m3u8",
      "logo": "https://i.imgur.com/jaBxxpt.png",
      "id": "latam_sv_9",
      "verified": True
    },
    {
      "code": "sv",
      "country": "El Salvador",
      "name": "El Camino TV (480p)",
      "category": "Religious",
      "url": "https://5d32e2b9b7eed.streamlock.net:4443/ectv/ectv/playlist.m3u8",
      "logo": "https://i.imgur.com/ZSktjGB.png",
      "id": "latam_sv_10",
      "verified": True
    },
    {
      "code": "sv",
      "country": "El Salvador",
      "name": "JFV TV (720p)",
      "category": "Religious",
      "url": "https://2nbyj587d53k-hls-live.5centscdn.com/09/25b94ec89b2aa708c3c4ad0014b09845.sdp/playlist.m3u8",
      "logo": "https://i.imgur.com/SrmI6nU.jpeg",
      "id": "latam_sv_11",
      "verified": True
    },
    {
      "code": "sv",
      "country": "El Salvador",
      "name": "Megavision Canal 21 (720p)",
      "category": "General",
      "url": "https://mgvchannel21-ioriver-cdn.encoders.immergo.tv/master.m3u8",
      "logo": "https://i.imgur.com/HbdYU9k.png",
      "id": "latam_sv_12",
      "verified": True
    },
    {
      "code": "sv",
      "country": "El Salvador",
      "name": "Canal TRV (576p)",
      "category": "General",
      "url": "https://stream.ontvmx.com/ontv/CNMLXR0Z6FPtGdjcI4/playlist.m3u8",
      "logo": "https://i.imgur.com/g5QKQ2E.png",
      "id": "latam_sv_13",
      "verified": True
    },
    {
      "code": "sv",
      "country": "El Salvador",
      "name": "Josue TV (1080p)",
      "category": "Religious",
      "url": "https://videoserver.tmcreativos.com:19360/abbftuhxxs/abbftuhxxs.m3u8",
      "logo": "https://i.imgur.com/LNWGe1D.jpg",
      "id": "latam_sv_14",
      "verified": True
    },
    {
      "code": "sv",
      "country": "El Salvador",
      "name": "Megavision Canal 19 (720p)",
      "category": "General",
      "url": "https://mgvchannel19-ioriver-cdn.encoders.immergo.tv/master.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Canal_19%27s_logo_%28Second_Era%29_in_2002.png",
      "id": "latam_sv_15",
      "verified": True
    }
  ],
  "gt": [
    {
      "code": "gt",
      "country": "Guatemala",
      "name": "Canal 13 (Guatemala) (720p)",
      "category": "General",
      "url": "http://190.61.101.11:7050/play/a07f/index.m3u8",
      "logo": "https://i.imgur.com/C1yVU3J.png",
      "id": "latam_gt_1",
      "verified": True
    },
    {
      "code": "gt",
      "country": "Guatemala",
      "name": "Amigos TV Chiquimula (480p)",
      "category": "Religious",
      "url": "https://antmedia.cablevisionrobles.com:5443/LiveApp/streams/CqwAgRagMvBNYN8c1731608980342.m3u8",
      "logo": "https://i.ibb.co/tLhcNTD/amigos-tv-chiquimula.png",
      "id": "latam_gt_2",
      "verified": True
    },
    {
      "code": "gt",
      "country": "Guatemala",
      "name": "Canal 30 TV Bethel (720p) [Not 24/7]",
      "category": "Religious",
      "url": "https://s.emisoras.tv:8081/canal30tvbethel/index.m3u8",
      "logo": "https://i.imgur.com/PP4U1JL.png",
      "id": "latam_gt_3",
      "verified": True
    },
    {
      "code": "gt",
      "country": "Guatemala",
      "name": "Canal TV Radio Maya TGBA (480p)",
      "category": "Religious",
      "url": "https://s.emisoras.tv:8081/radiomaya/index.m3u8",
      "logo": "https://i.imgur.com/kORStT1.png",
      "id": "latam_gt_4",
      "verified": True
    },
    {
      "code": "gt",
      "country": "Guatemala",
      "name": "Canal 13 Esquipulas (720p)",
      "category": "General",
      "url": "https://tv91.hostingnuclear.com:19360/intercable/intercable.m3u8",
      "logo": "https://i.imgur.com/INKZvlN.png",
      "id": "latam_gt_5",
      "verified": True
    },
    {
      "code": "gt",
      "country": "Guatemala",
      "name": "Guatevision (1080p)",
      "category": "News",
      "url": "http://200.115.120.1:8000/play/ca066/index.m3u8",
      "logo": "https://i.imgur.com/mbmHPnO.png",
      "id": "latam_gt_6",
      "verified": True
    },
    {
      "code": "gt",
      "country": "Guatemala",
      "name": "Aurora Media Films (720p)",
      "category": "Movies",
      "url": "https://cdn.streamhispanatv.net:3417/live/auroramflive.m3u8",
      "logo": "https://i.imgur.com/DVC5w6H.png",
      "id": "latam_gt_7",
      "verified": True
    },
    {
      "code": "gt",
      "country": "Guatemala",
      "name": "Canal 100 Chinique (1080p)",
      "category": "Undefined",
      "url": "https://live20.bozztv.com/giatv/giatv-chinique100tvenvivo/chinique100tvenvivo/playlist.m3u8",
      "logo": "https://i.imgur.com/ygNKJXx.png",
      "id": "latam_gt_8",
      "verified": True
    },
    {
      "code": "gt",
      "country": "Guatemala",
      "name": "Barbe TV (720p) [Not 24/7]",
      "category": "General",
      "url": "https://cdn.streamhispanatv.net:3549/live/barbetvlive.m3u8",
      "logo": "https://i.imgur.com/2Sekew2.png",
      "id": "latam_gt_9",
      "verified": True
    },
    {
      "code": "gt",
      "country": "Guatemala",
      "name": "Conectados con Dios",
      "category": "Religious",
      "url": "https://cdn.oktvus.com/ConectadoConDios/tracks-v2a1/mono.ts.m3u8",
      "logo": "https://i.imgur.com/Drn8nql.png",
      "id": "latam_gt_10",
      "verified": True
    },
    {
      "code": "gt",
      "country": "Guatemala",
      "name": "Jubilo TV (720p)",
      "category": "Religious",
      "url": "http://173.249.60.54/hls/jubilotv.m3u8",
      "logo": "https://i.ibb.co/R4QSfYd/Ba073d3280959c5ba7d25d40052a7349.png",
      "id": "latam_gt_11",
      "verified": True
    },
    {
      "code": "gt",
      "country": "Guatemala",
      "name": "Iglesia Del Camino (480p) [Not 24/7]",
      "category": "Religious",
      "url": "http://streamingcontrol.com:1935/ectv/ectv/playlist.m3u8",
      "logo": "https://i.imgur.com/vHfb3Z4.png",
      "id": "latam_gt_12",
      "verified": True
    },
    {
      "code": "gt",
      "country": "Guatemala",
      "name": "MAS TV",
      "category": "General",
      "url": "https://cdn.streamhispanatv.net:3011/live/mastvgtlive.m3u8",
      "logo": "https://i.imgur.com/3XuwlkQ.jpg",
      "id": "latam_gt_13",
      "verified": True
    }
  ],
  "hn": [
    {
      "code": "hn",
      "country": "Honduras",
      "name": "Canal 5 El Lider (720p)",
      "category": "General",
      "url": "http://186.33.26.18:8000/play/a0s4/index.m3u8",
      "logo": "https://i.imgur.com/4hEYFa9.png",
      "id": "latam_hn_1",
      "verified": True
    },
    {
      "code": "hn",
      "country": "Honduras",
      "name": "Buendia TV",
      "category": "News",
      "url": "https://servilive.com:3508/stream/play.m3u8",
      "logo": "https://i.imgur.com/m5hNyNE.png",
      "id": "latam_hn_2",
      "verified": True
    },
    {
      "code": "hn",
      "country": "Honduras",
      "name": "Alsacias Television (720p)",
      "category": "General",
      "url": "https://s.emisoras.tv:8081/atv/index.m3u8",
      "logo": "https://i.imgur.com/SbuD1UW.png",
      "id": "latam_hn_3",
      "verified": True
    },
    {
      "code": "hn",
      "country": "Honduras",
      "name": "Canal 7 Talanga Vision (720p)",
      "category": "General",
      "url": "https://amixtv.com:8081/talangavision/index.m3u8",
      "logo": "https://i.ibb.co/0cqcyz4/Logo-2020-azul-El-lider-de-la-zona.png",
      "id": "latam_hn_4",
      "verified": True
    },
    {
      "code": "hn",
      "country": "Honduras",
      "name": "Choluteca TV (1080p)",
      "category": "Religious",
      "url": "https://s.emisoras.tv:8081/cholutecatv/index.m3u8",
      "logo": "https://i.imgur.com/mpc4Isd.png",
      "id": "latam_hn_5",
      "verified": True
    },
    {
      "code": "hn",
      "country": "Honduras",
      "name": "Dios Te Ve (720p)",
      "category": "Religious",
      "url": "https://s.emisoras.tv:8081/diostevetv/index.m3u8",
      "logo": "https://i.imgur.com/7hNwUV2.png",
      "id": "latam_hn_6",
      "verified": True
    },
    {
      "code": "hn",
      "country": "Honduras",
      "name": "Dios Te Ve Kids (720p)",
      "category": "Kids;Religious",
      "url": "https://s.emisoras.tv:8081/diostevekids/index.m3u8",
      "logo": "https://i.imgur.com/GnZicVH.png",
      "id": "latam_hn_7",
      "verified": True
    },
    {
      "code": "hn",
      "country": "Honduras",
      "name": "CCI Channel (1080p)",
      "category": "Religious",
      "url": "https://livestream.mediacci.com/ccitv/index.m3u8",
      "logo": "https://i.imgur.com/c6hm03f.png",
      "id": "latam_hn_8",
      "verified": True
    },
    {
      "code": "hn",
      "country": "Honduras",
      "name": "Girasol TV (1080i)",
      "category": "Entertainment",
      "url": "https://s.emisoras.tv:8081/girasoltv/index.m3u8",
      "logo": "https://i.imgur.com/2t7A2yg.png",
      "id": "latam_hn_9",
      "verified": True
    },
    {
      "code": "hn",
      "country": "Honduras",
      "name": "EDN TV (1080p) [Not 24/7]",
      "category": "Entertainment",
      "url": "https://60417ddeaf0d9.streamlock.net/edntv/videoedntv/playlist.m3u8",
      "logo": "https://i.imgur.com/5fPsYTz.png",
      "id": "latam_hn_10",
      "verified": True
    },
    {
      "code": "hn",
      "country": "Honduras",
      "name": "Guayape TV",
      "category": "General",
      "url": "https://tv.bitstreaming.net:8443/live/guayapetv.m3u8",
      "logo": "https://i.imgur.com/cteBdAJ.jpg",
      "id": "latam_hn_11",
      "verified": True
    },
    {
      "code": "hn",
      "country": "Honduras",
      "name": "AZA TV HD (1080p)",
      "category": "General",
      "url": "https://tv.webmedialive.com/azatvhn/live/playlist.m3u8",
      "logo": "https://i.imgur.com/Jytpy32.png",
      "id": "latam_hn_12",
      "verified": True
    },
    {
      "code": "hn",
      "country": "Honduras",
      "name": "CHTV (1080p)",
      "category": "General",
      "url": "https://viewhn.com/chtv/live/playlist.m3u8",
      "logo": "https://i.imgur.com/QLQgwc6.png",
      "id": "latam_hn_13",
      "verified": True
    },
    {
      "code": "hn",
      "country": "Honduras",
      "name": "ICN Digital",
      "category": "News",
      "url": "https://streaming.icndigital.com/live_output/icn_live_stream_1.m3u8",
      "logo": "https://i.imgur.com/UCZVQgj.png",
      "id": "latam_hn_14",
      "verified": True
    },
    {
      "code": "hn",
      "country": "Honduras",
      "name": "Dios Tv Talanga (1080p)",
      "category": "Religious",
      "url": "https://tv.webmedialive.com/unciontv/live/playlist.m3u8",
      "logo": "https://i.ibb.co/mb8F7R1/Db52f621d30793337de1cdcfc4f02be1.png",
      "id": "latam_hn_15",
      "verified": True
    }
  ],
  "ni": [
    {
      "code": "ni",
      "country": "Nicaragua",
      "name": "Canal 10 (Nicaragua) (360p) [Geo-blocked]",
      "category": "General",
      "url": "https://www.canal10.com.ni/envivo",
      "logo": "https://i.imgur.com/ztp781b.png",
      "id": "latam_ni_1",
      "verified": True
    },
    {
      "code": "ni",
      "country": "Nicaragua",
      "name": "Escuchame Radio TV (720p) [Not 24/7]",
      "category": "Religious",
      "url": "https://stmv1.transmissaodigital.com/pedro9800/pedro9800/playlist.m3u8",
      "logo": "https://i.imgur.com/gt6UvG8.png",
      "id": "latam_ni_2",
      "verified": True
    },
    {
      "code": "ni",
      "country": "Nicaragua",
      "name": "Viva Nicaragua Canal 13 (720p)",
      "category": "General",
      "url": "https://cdn.vivamediosni.com/viva_720p/index.m3u8",
      "logo": "https://i.imgur.com/9q7Ajz4.png",
      "id": "latam_ni_3",
      "verified": True
    },
    {
      "code": "ni",
      "country": "Nicaragua",
      "name": "MegaBox (720p) [Not 24/7]",
      "category": "Music",
      "url": "https://hdbox.chunklistv.com/live?stream=megabox",
      "logo": "https://i.imgur.com/JqaW7Ei.png",
      "id": "latam_ni_4",
      "verified": True
    },
    {
      "code": "ni",
      "country": "Nicaragua",
      "name": "WTV Canal 20 (1080p)",
      "category": "Entertainment",
      "url": "https://cootv.cootel.com.ni:8095/Canal40_WTV/playlist.m3u8",
      "logo": "https://i.imgur.com/nb81xeU.png",
      "id": "latam_ni_5",
      "verified": True
    },
    {
      "code": "ni",
      "country": "Nicaragua",
      "name": "Olam Metro TV (720p)",
      "category": "Religious",
      "url": "https://netzerstreaming.com:4433/hls/olammetro/index.m3u8",
      "logo": "https://i.imgur.com/dDZnyUA.jpeg",
      "id": "latam_ni_6",
      "verified": True
    }
  ],
  "do": [
    {
      "code": "do",
      "country": "República Dominicana",
      "name": "A&E Latin America (1080p)",
      "category": "Entertainment",
      "url": "http://138.121.15.230:9002/A&E/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/A%26E_Network_logo.svg/960px-A%26E_Network_logo.svg.png",
      "id": "latam_do_1",
      "verified": True
    },
    {
      "code": "do",
      "country": "República Dominicana",
      "name": "A7 TV (1080p)",
      "category": "General",
      "url": "https://183.bozztv.com/ssh101/ssh101/a7tvjarabacoa/playlist.m3u8",
      "logo": "https://a7tvjarabacoa.netlify.app/IMG_1968.PNG",
      "id": "latam_do_2",
      "verified": True
    },
    {
      "code": "do",
      "country": "República Dominicana",
      "name": "Adoram TV (720p)",
      "category": "Religious",
      "url": "https://live20.bozztv.com/giatv/giatv-adoram/adoram/chunks.m3u8",
      "logo": "https://i.imgur.com/uU01KHz.png",
      "id": "latam_do_3",
      "verified": True
    },
    {
      "code": "do",
      "country": "República Dominicana",
      "name": "Alcarrizos TV (720p) [Not 24/7]",
      "category": "General",
      "url": "https://5790d294af2dc.streamlock.net/alcarrizostv/alcarrizostv/playlist.m3u8",
      "logo": "https://i.ibb.co/C3fdPYGs/Alcarrizo.jpg",
      "id": "latam_do_4",
      "verified": True
    },
    {
      "code": "do",
      "country": "República Dominicana",
      "name": "Acento TV",
      "category": "News",
      "url": "https://acentotv01.streamprolive.com/hls/live.m3u8",
      "logo": "https://i.imgur.com/jhiZfHf.png",
      "id": "latam_do_5",
      "verified": True
    },
    {
      "code": "do",
      "country": "República Dominicana",
      "name": "Altanto TV (1080p) [Not 24/7]",
      "category": "General",
      "url": "https://stream.haislin.com/ls_j3BOKxBbUJ/index.m3u8",
      "logo": "https://i.imgur.com/KWvVLhc.png",
      "id": "latam_do_6",
      "verified": True
    },
    {
      "code": "do",
      "country": "República Dominicana",
      "name": "AION TV (1080p) [Not 24/7]",
      "category": "General",
      "url": "https://edge.essastream.com/aiontelevision/playlist.m3u8",
      "logo": "https://i.imgur.com/DBvm7YS.png",
      "id": "latam_do_7",
      "verified": True
    },
    {
      "code": "do",
      "country": "República Dominicana",
      "name": "Antena 7 HD (1080p) [Not 24/7]",
      "category": "General",
      "url": "https://hls.tvabierta.net/hls/007.m3u8",
      "logo": "https://i.imgur.com/zKWFgeQ.png",
      "id": "latam_do_8",
      "verified": True
    },
    {
      "code": "do",
      "country": "República Dominicana",
      "name": "Ame 47 (576p)",
      "category": "General",
      "url": "https://ss2.tvrdomi.com:1936/ame47/ame47/playlist.m3u8",
      "logo": "https://i.imgur.com/MUEbjeP.png",
      "id": "latam_do_9",
      "verified": True
    },
    {
      "code": "do",
      "country": "República Dominicana",
      "name": "Alegre TV RD (720p) [Not 24/7]",
      "category": "Entertainment",
      "url": "https://streamunoapp.com:3149/live/alegretvlive.m3u8",
      "logo": "https://i.imgur.com/O6USO8r.png",
      "id": "latam_do_10",
      "verified": True
    },
    {
      "code": "do",
      "country": "República Dominicana",
      "name": "Bebeto TV (1080p) [Not 24/7]",
      "category": "General",
      "url": "https://edge.essastream.com/bebetotelevision/index.m3u8",
      "logo": "",
      "id": "latam_do_11",
      "verified": True
    },
    {
      "code": "do",
      "country": "República Dominicana",
      "name": "Ahora TV (1080p) [Not 24/7]",
      "category": "General",
      "url": "https://stream.haislin.com/ahoratv/index.m3u8",
      "logo": "https://i.imgur.com/dyJyuXc.png",
      "id": "latam_do_12",
      "verified": True
    },
    {
      "code": "do",
      "country": "República Dominicana",
      "name": "Antena 21 HD (720p) [Not 24/7]",
      "category": "Entertainment",
      "url": "https://hls.tvabierta.net/hls/021.m3u8",
      "logo": "https://i.imgur.com/QE0XWLh.png",
      "id": "latam_do_13",
      "verified": True
    },
    {
      "code": "do",
      "country": "República Dominicana",
      "name": "Camu TV (480p) [Not 24/7]",
      "category": "General",
      "url": "https://live20.bozztv.com/akamaissh101/ssh101/camutv/playlist.m3u8",
      "logo": "https://i.imgur.com/3d8cLm9.jpg",
      "id": "latam_do_14",
      "verified": True
    },
    {
      "code": "do",
      "country": "República Dominicana",
      "name": "Boreal (720p) [Not 24/7]",
      "category": "Movies",
      "url": "https://edge.essastream.com/borealtelevision/tracks-v1a1/mono.m3u8",
      "logo": "https://i.imgur.com/KSquHTG.png",
      "id": "latam_do_15",
      "verified": True
    }
  ],
  "pr": [
    {
      "code": "pr",
      "country": "Puerto Rico",
      "name": "CAtv (1080p) [Not 24/7]",
      "category": "General",
      "url": "https://video2.getstreamhosting.com:19360/8216/8216.m3u8",
      "logo": "https://caribbeanadvantage.com/images/CAtv-logo-512.png",
      "id": "latam_pr_1",
      "verified": True
    },
    {
      "code": "pr",
      "country": "Puerto Rico",
      "name": "Telemundo WKAQ-TV (1080p)",
      "category": "General",
      "url": "https://nbculocallive.akamaized.net/hls/live/2037499/puertorico/stream1/master.m3u8",
      "logo": "https://imgx.fubo.tv/station_logos/telemundo_c.png",
      "id": "latam_pr_2",
      "verified": True
    },
    {
      "code": "pr",
      "country": "Puerto Rico",
      "name": "America TeVe (1080p)",
      "category": "Entertainment;General",
      "url": "https://live.gideo.video/americateve2/master.m3u8",
      "logo": "https://i.imgur.com/K9o3mLP.png",
      "id": "latam_pr_3",
      "verified": True
    },
    {
      "code": "pr",
      "country": "Puerto Rico",
      "name": "DeFiance Media (1080p)",
      "category": "Business",
      "url": "https://amg01529-defiancetv-defiancemedia-glewed-tre8x.amagi.tv/playlist.m3u8",
      "logo": "https://xstreamcp-assets-msp.streamready.in/assets/DISTROTV/LIVECHANNEL/66698943bac4421ebc533695/images/logo_20231219_193005_68.png",
      "id": "latam_pr_4",
      "verified": True
    },
    {
      "code": "pr",
      "country": "Puerto Rico",
      "name": "TyC Sports USA",
      "category": "Sports",
      "url": "http://45.170.130.224:8000/play/a020/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/TyC_Sports_logo.svg/960px-TyC_Sports_logo.svg.png",
      "id": "latam_pr_5",
      "verified": True
    },
    {
      "code": "pr",
      "country": "Puerto Rico",
      "name": "Candelita TV (480p)",
      "category": "Religious",
      "url": "https://6110f70ea8d0e.streamlock.net/1689/1689/playlist.m3u8",
      "logo": "https://i.imgur.com/34BvVDl.png",
      "id": "latam_pr_6",
      "verified": True
    },
    {
      "code": "pr",
      "country": "Puerto Rico",
      "name": "Salvacion TV (720p)",
      "category": "Religious",
      "url": "https://stream.eleden.com/livesalvatv/ngrp:livesalvatv_all/playlist.m3u8",
      "logo": "https://i.imgur.com/6HOViG9.png",
      "id": "latam_pr_7",
      "verified": True
    },
    {
      "code": "pr",
      "country": "Puerto Rico",
      "name": "La-X (720p)",
      "category": "Music",
      "url": "https://stream.eleden.com/livelax/ngrp:livelax_all/playlist.m3u8",
      "logo": "https://i.imgur.com/i2GnQTq.png",
      "id": "latam_pr_8",
      "verified": True
    },
    {
      "code": "pr",
      "country": "Puerto Rico",
      "name": "Paraiso TV (720p)",
      "category": "Religious",
      "url": "https://stream.eleden.com/livewtpm/ngrp:livewtpm_all/playlist.m3u8",
      "logo": "https://i.imgur.com/wE31GIP.jpg",
      "id": "latam_pr_9",
      "verified": True
    },
    {
      "code": "pr",
      "country": "Puerto Rico",
      "name": "Familia Vision HD [Not 24/7]",
      "category": "Religious",
      "url": "https://584097344c1f0.streamlock.net/29/stream/playlist.m3u8",
      "logo": "https://i.imgur.com/uqTH7m5.jpg",
      "id": "latam_pr_10",
      "verified": True
    },
    {
      "code": "pr",
      "country": "Puerto Rico",
      "name": "Nueva Vida FM (720p)",
      "category": "Music;Religious",
      "url": "https://stream.nuevavidafm.net:3937/live/nuevavidalive.m3u8",
      "logo": "https://i.ibb.co/3mbZWyN/nav-Bar-title-Image-iphone6plus.png",
      "id": "latam_pr_11",
      "verified": True
    },
    {
      "code": "pr",
      "country": "Puerto Rico",
      "name": "Faro de Santidad TV (720p)",
      "category": "Religious",
      "url": "https://5dbcd1053301e.streamlock.net:4443/farodesantidad/farodesantidad/playlist.m3u8",
      "logo": "https://i.imgur.com/GoNBFzI.png",
      "id": "latam_pr_12",
      "verified": True
    },
    {
      "code": "pr",
      "country": "Puerto Rico",
      "name": "CDM Internacional (480p) [Not 24/7]",
      "category": "Religious",
      "url": "https://627bb251f23c7.streamlock.net:444/CDMInternacional/CDMInternacional/playlist.m3u8",
      "logo": "https://i.imgur.com/N7IneVk.png",
      "id": "latam_pr_13",
      "verified": True
    },
    {
      "code": "pr",
      "country": "Puerto Rico",
      "name": "WKAQ-TV 2.2 (1080p)",
      "category": "Undefined",
      "url": "https://nbculocallive.akamaized.net/hls/live/2037499/puertorico/stream2/master_720.m3u8",
      "logo": "https://i.imgur.com/TL6xy4y.png",
      "id": "latam_pr_14",
      "verified": True
    },
    {
      "code": "pr",
      "country": "Puerto Rico",
      "name": "Pura Palabra (718p) [Not 24/7]",
      "category": "Undefined",
      "url": "https://59825a54e4454.streamlock.net:8443/william233/william233/playlist.m3u8",
      "logo": "https://i.imgur.com/nl5vyIw.png",
      "id": "latam_pr_15",
      "verified": True
    }
  ],
  "cu": [
    {
      "code": "cu",
      "country": "Cuba",
      "name": "Radio y Television Marti (720p)",
      "category": "General",
      "url": "https://ocb-ingest.akamaized.net/hls/live/2037032/tvmc01/playlist.m3u8",
      "logo": "https://i.imgur.com/J2ZMa4g.png",
      "id": "latam_cu_1",
      "verified": True
    },
    {
      "code": "cu",
      "country": "Cuba",
      "name": "Prensa Latina TV (1080p)",
      "category": "News",
      "url": "https://eu1.servers10.com:8081/8192/index.m3u8",
      "logo": "https://i.imgur.com/jbm2S9O.jpg",
      "id": "latam_cu_2",
      "verified": True
    }
  ],
  "es": [
    {
      "code": "es",
      "country": "España",
      "name": "12tv (720p)",
      "category": "General",
      "url": "https://cloud.fastchannel.es/mic/manifiest/hls/12tv/12tv.m3u8",
      "logo": "https://i.imgur.com/VSTgXsh.png",
      "id": "latam_es_1",
      "verified": True
    },
    {
      "code": "es",
      "country": "España",
      "name": "3Cat Cameres del temps (1080p)",
      "category": "Public;Weather",
      "url": "https://directes-tv-int.3catdirectes.cat/live-content/beauties-hls/master.m3u8",
      "logo": "https://i.imgur.com/zXy2kbe.png",
      "id": "latam_es_2",
      "verified": True
    },
    {
      "code": "es",
      "country": "España",
      "name": "3CatInfo (1080p)",
      "category": "News;Public",
      "url": "https://directes-tv-int.3catdirectes.cat/live-origin/canal324-hls/master.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/3CatInfo_logo.svg/960px-3CatInfo_logo.svg.png",
      "id": "latam_es_3",
      "verified": True
    },
    {
      "code": "es",
      "country": "España",
      "name": "8 La Marina TV (576p)",
      "category": "General",
      "url": "https://streaming005.gestec-video.com/hls/canal24.m3u8",
      "logo": "https://i.imgur.com/BTJvvBK.png",
      "id": "latam_es_4",
      "verified": True
    },
    {
      "code": "es",
      "country": "España",
      "name": "Alcarria TV (576p) [Not 24/7]",
      "category": "General",
      "url": "http://217.182.77.27/live/alcarriatv-livestream.m3u8",
      "logo": "https://i.imgur.com/pzJAYan.png",
      "id": "latam_es_5",
      "verified": True
    },
    {
      "code": "es",
      "country": "España",
      "name": "3Cat Plats bruts (1080p)",
      "category": "Classic;Comedy;Public;Series",
      "url": "https://fast-tailor.3catdirectes.cat/v1/channel/ccma-channel2/hls.m3u8",
      "logo": "https://i.imgur.com/49ZENis.png",
      "id": "latam_es_6",
      "verified": True
    },
    {
      "code": "es",
      "country": "España",
      "name": "A Punt (720p)",
      "category": "General;Public",
      "url": "https://fastly.live.brightcove.com/1846756479408303045/eu-central-1/6057955885001/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJob3N0IjoiZWFxNWh4LmVncmVzcy53YzQ3bTEiLCJhY2NvdW50X2lkIjoiNjA1Nzk1NTg4NTAwMSIsImVobiI6ImZhc3RseS5saXZlLmJyaWdodGNvdmUuY29tIiwiaXNzIjoiYmxpdmUtcGxheWJhY2stc291cmNlLWFwaSIsInN1YiI6InBhdGhtYXB0b2tlbiIsImF1ZCI6WyI2MDU3OTU1ODg1MDAxIl0sImp0aSI6IjE4NDY3NTY0Nzk0MDgzMDMwNDUifQ.o6wb_VA-TVxl3ERgr7FKLlaTjY7smErmsf73QAydySE/playlist-hls-dvr.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Logotip_d%27%C3%80_Punt_%282017-%29.svg/960px-Logotip_d%27%C3%80_Punt_%282017-%29.svg.png",
      "id": "latam_es_7",
      "verified": True
    },
    {
      "code": "es",
      "country": "España",
      "name": "Az Corazon (720p)",
      "category": "Series",
      "url": "http://200.115.120.1:8000/play/ca020/index.m3u8",
      "logo": "https://i.imgur.com/KIpSdQC.png",
      "id": "latam_es_8",
      "verified": True
    },
    {
      "code": "es",
      "country": "España",
      "name": "Ana y los 7",
      "category": "Series",
      "url": "https://jmp2.uk/plu-5f1acce7f17797000718f9be.m3u8",
      "logo": "https://i.imgur.com/X5g6gXS.png",
      "id": "latam_es_9",
      "verified": True
    },
    {
      "code": "es",
      "country": "España",
      "name": "28 kanala",
      "category": "General",
      "url": "https://streaming.28kanala.eus/hls/z.m3u8",
      "logo": "https://i.imgur.com/DyvK28q.png",
      "id": "latam_es_10",
      "verified": True
    },
    {
      "code": "es",
      "country": "España",
      "name": "Activa TV (720p)",
      "category": "Music",
      "url": "https://streamtv.mediasector.es/hls/activatv/index.m3u8",
      "logo": "https://i.imgur.com/VCUZKiw.png",
      "id": "latam_es_11",
      "verified": True
    },
    {
      "code": "es",
      "country": "España",
      "name": "24 Horas (Spain) (720p)",
      "category": "News;Public",
      "url": "https://ztnr.rtve.es/ztnr/1694255.m3u8",
      "logo": "https://i.ibb.co/21sXZ3GT/24h.png",
      "id": "latam_es_12",
      "verified": True
    },
    {
      "code": "es",
      "country": "España",
      "name": "24 Horas Catalunya (720p)",
      "category": "News;Public",
      "url": "https://ztnr.rtve.es/ztnr/4952053.m3u8",
      "logo": "https://i.ibb.co/21sXZ3GT/24h.png",
      "id": "latam_es_13",
      "verified": True
    },
    {
      "code": "es",
      "country": "España",
      "name": "Alacanti TV (576p) [Not 24/7]",
      "category": "General",
      "url": "https://streaming01.gestec-video.com/hls/artequatreAlacanti.m3u8",
      "logo": "https://i.imgur.com/pcWU6e1.png",
      "id": "latam_es_14",
      "verified": True
    },
    {
      "code": "es",
      "country": "España",
      "name": "Arabi TV (1080p)",
      "category": "General",
      "url": "https://streamtv2.elitecomunicacion.cloud:3628/live/arabitv2025live.m3u8",
      "logo": "https://i.ibb.co/9Vp9Ghg/LOGO-WEB-ARABI-TV-3.png",
      "id": "latam_es_15",
      "verified": True
    }
  ],
  "latam": [
    {
      "code": "latam",
      "country": "Latinoamérica",
      "name": "DW Español HD (Noticias Internacionales)",
      "category": "Noticias",
      "url": "https://dwamdstream104.akamaized.net/hls/live/2015530/dwstream104/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Deutsche_Welle_symbol_2012.svg/300px-Deutsche_Welle_symbol_2012.svg.png",
      "id": "latam_latam_1",
      "verified": True
    },
    {
      "code": "latam",
      "country": "Latinoamérica",
      "name": "RT en Español Documentales HD",
      "category": "Documentales",
      "url": "https://rt-esp.rttv.com/live/rtd_es/playlist.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/RT_logo.svg/300px-RT_logo.svg.png",
      "id": "latam_latam_2",
      "verified": True
    },
    {
      "code": "latam",
      "country": "Latinoamérica",
      "name": "RT Noticias en Español En Vivo",
      "category": "Noticias",
      "url": "https://rt-esp.rttv.com/live/rtesp/playlist.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/RT_logo.svg/300px-RT_logo.svg.png",
      "id": "latam_latam_3",
      "verified": True
    },
    {
      "code": "latam",
      "country": "Latinoamérica",
      "name": "France 24 Español HD",
      "category": "Noticias",
      "url": "https://live.france24.com/hls/live/2037220-b/F24_ES_HI_HLS/master_5000.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/France24.png/240px-France24.png",
      "id": "latam_latam_4",
      "verified": True
    },
    {
      "code": "latam",
      "country": "Latinoamérica",
      "name": "Cinecanal Panregional (Español Latino HD)",
      "category": "Movies",
      "url": "http://138.121.15.230:9002/CINECANAL/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/CinecanalLA.png/960px-CinecanalLA.png",
      "id": "latam_latam_5",
      "verified": True
    },
    {
      "code": "latam",
      "country": "Latinoamérica",
      "name": "Cartoon Network Latinoamérica (Español Latino)",
      "category": "Animation;Kids",
      "url": "http://45.167.1.138:8000/play/a00w",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Cartoon_Network_2010_logo.svg/960px-Cartoon_Network_2010_logo.svg.png",
      "id": "latam_latam_6",
      "verified": True
    },
    {
      "code": "latam",
      "country": "Latinoamérica",
      "name": "Discovery Kids Latinoamérica (Español Latino HD)",
      "category": "Kids",
      "url": "http://38.224.231.176:8000/play/a01j/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Discovery_Kids_2021_2D_sin_wordmark.svg/960px-Discovery_Kids_2021_2D_sin_wordmark.svg.png",
      "id": "latam_latam_7",
      "verified": True
    },
    {
      "code": "latam",
      "country": "Latinoamérica",
      "name": "Disney Channel Latinoamérica (Español Latino HD)",
      "category": "Animation;Kids",
      "url": "http://45.134.141.161:2200/ARG/Disney_Channel/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/f/ff/2024_Disney_Channel_text_logo.svg",
      "id": "latam_latam_8",
      "verified": True
    },
    {
      "code": "latam",
      "country": "Latinoamérica",
      "name": "Disney Jr. Latinoamérica (Español Latino HD)",
      "category": "Animation;Kids",
      "url": "http://45.185.163.75:8000/play/a016/index.m3u8",
      "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e3/2024_Disney_Jr._Logo.svg",
      "id": "latam_latam_9",
      "verified": True
    },
    {
      "code": "latam",
      "country": "Latinoamérica",
      "name": "ESPN Latinoamérica (1080p HD · Multi-Mirror)",
      "category": "Sports",
      "url": "https://barinaslive1.boldmss.com/ESPN/ESPN.isml/ESPN.m3u8",
      "backup_urls": [
        "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/espn-mux/chunks.m3u8",
        "https://barinaslive1.boldmss.com/ESPN_2/ESPN_2.isml/ESPN_2.m3u8"
      ],
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/ESPN_wordmark.svg/512px-ESPN_wordmark.svg.png",
      "id": "latam_latam_10",
      "verified": True
    },
    {
      "code": "latam",
      "country": "Latinoamérica",
      "name": "ESPN 3 Latinoamérica (1080p HD)",
      "category": "Sports",
      "url": "https://barinaslive1.boldmss.com/ESPN_3/ESPN_3.isml/ESPN_3.m3u8",
      "backup_urls": [
        "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/espn3-mux/playlist.m3u8"
      ],
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/ESPN3_Logo.png/960px-ESPN3_Logo.png",
      "id": "latam_latam_11",
      "verified": True
    },
    {
      "code": "latam",
      "country": "Latinoamérica",
      "name": "TNT Latinoamérica HD (Español Latino · Multi-Mirror)",
      "category": "Movies;Sports",
      "url": "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/tnt/chunks.m3u8",
      "backup_urls": [
        "http://45.171.64.30:6060/play/a03i/index.m3u8",
        "http://181.78.211.244:8005/play/a09g/index.m3u8"
      ],
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/TNT_Logo_2016.svg/512px-TNT_Logo_2016.svg.png",
      "id": "latam_latam_12",
      "verified": True
    },
    {
      "code": "latam",
      "country": "Latinoamérica",
      "name": "TNT Series Latinoamérica (1080p HD)",
      "category": "Series;Sports",
      "url": "http://168.196.127.137:6001/play/a095/index.m3u8",
      "backup_urls": [
        "https://bantel-cdn1.iptvperu.tv:1936/btnscrtn/TNTseries.stream/chunks.m3u8"
      ],
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/TNT_Logo_2016.svg/512px-TNT_Logo_2016.svg.png",
      "id": "latam_latam_13",
      "verified": True
    },
    {
      "code": "latam",
      "country": "Latinoamérica",
      "name": "Fox Sports & TyC Sports Latinoamérica (1080p HD)",
      "category": "Sports",
      "url": "http://138.59.227.20:8000/play/a085/index.m3u8",
      "backup_urls": [
        "https://amg26268-amg26268c14-freelivesports-emea-10267.playouts.now.amagi.tv/ts-us-e2-n2/playlist/amg26268-sportsstudio-tycsports-freelivesportsemea/playlist.m3u8"
      ],
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/FOX_Sports_logo.svg/512px-FOX_Sports_logo.svg.png",
      "id": "latam_latam_14",
      "verified": True
    },
    {
      "code": "latam",
      "country": "Latinoamérica",
      "name": "FIFA+ Hispanoamérica (Fútbol en Español HD)",
      "category": "Sports",
      "url": "https://6c849fb3.wurl.com/master/f36d25e7e52f1ba8d7e56eb859c636563214f541/TEctbXhfRklGQVBsdXNTcGFuaXNoLTFfSExT/playlist.m3u8",
      "backup_urls": [
        "https://d63fabad.wurl.com/master/f36d25e7e52f1ba8d7e56eb859c636563214f541/UmFrdXRlblRWLWVzX0ZJRkFQbHVzU3BhbmlzaF9ITFM/playlist.m3u8"
      ],
      "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/FIFA_logo_without_slogan.svg/512px-FIFA_logo_without_slogan.svg.png",
      "id": "latam_latam_15",
      "verified": True
    }
  ]
}


def translate_category(cat_raw):
    """Traduce etiquetas de categoría en inglés a español claro."""
    if not cat_raw:
        return "General"
    c = cat_raw.lower()
    if "sport" in c or "deport" in c:
        return "Deportes"
    if "news" in c or "notic" in c:
        return "Noticias"
    if "movie" in c or "cine" in c:
        return "Cine & Películas"
    if "serie" in c:
        return "Series & Ficción"
    if "kid" in c or "animation" in c or "infantil" in c:
        return "Infantil & Animación"
    if "music" in c or "músic" in c:
        return "Música & Conciertos"
    if "cultur" in c or "document" in c or "educa" in c:
        return "Cultura & Documentales"
    if "entertain" in c or "entreten" in c or "comedy" in c:
        return "Entretenimiento"
    if "relig" in c:
        return "Religioso / Valores"
    return "TV Abierta / General"


def get_verified_for_country(country_code):
    """Retorna la lista pre-verificada de canales de un país."""
    if country_code == "cl":
        return chile_channels.get_chile_channels()
    return VERIFIED_LATAM_BY_COUNTRY.get(country_code, [])


def find_channel_by_id(item_id):
    """Busca cualquier canal verificado en Chile, Panregional o los 20 países de LatAm por su ID."""
    if not item_id:
        return None
    cl_match = chile_channels.find_chile_channel_by_id(item_id)
    if cl_match:
        return cl_match
    for ch_list in VERIFIED_LATAM_BY_COUNTRY.values():
        for ch in ch_list:
            if ch.get("id") == item_id:
                return ch
    return None


def get_country_channels_full(country_code, include_live_feed=True, max_dynamic=250):
    """
    Combina los canales pre-verificados del país con el feed dinámico de iptv-org
    sin duplicar URLs, garantizando máxima disponibilidad en todos los países latinos.
    """
    verified = list(get_verified_for_country(country_code))
    seen_urls = set()
    results = []

    for ch in verified:
        u = ch.get("url", "").strip()
        if u and u not in seen_urls:
            seen_urls.add(u)
            item = dict(ch)
            item["verified"] = True
            item["category_es"] = translate_category(item.get("category", ""))
            results.append(item)

    if include_live_feed and country_code != "cl":
        if country_code == "latam":
            dyn_channels = world_channels.get_latam_region_channels(max_items=max_dynamic)
        else:
            dyn_channels = world_channels.get_country_channels(country_code, max_items=max_dynamic)
        for idx, dch in enumerate(dyn_channels, 1):
            u = dch.get("url", "").strip()
            if u and u not in seen_urls:
                seen_urls.add(u)
                results.append({
                    "id": f"dyn_{country_code}_{idx}",
                    "code": country_code,
                    "country": next((c["name"] for c in LATAM_COUNTRIES if c["code"] == country_code), country_code.upper()),
                    "name": dch.get("name", "Canal TV"),
                    "url": u,
                    "logo": dch.get("logo", ""),
                    "category": dch.get("category", "General"),
                    "category_es": translate_category(dch.get("category", "")),
                    "verified": False
                })

    return results


def get_all_verified_latam_channels():
    """Devuelve todos los canales verificados de todos los países de Latinoamérica."""
    all_chs = []
    for c in LATAM_COUNTRIES:
        code = c["code"]
        flag = c["flag"]
        country_name = c["name"]
        chs = get_verified_for_country(code)
        for ch in chs:
            copy_ch = dict(ch)
            copy_ch.setdefault("country", country_name)
            copy_ch["flag"] = flag
            copy_ch["category_es"] = translate_category(copy_ch.get("category", ""))
            all_chs.append(copy_ch)
    return all_chs


def get_latam_by_genre(genre_id):
    """Filtra todos los canales verificados de Latinoamérica según el grupo temático."""
    group = next((g for g in LATAM_GENRE_GROUPS if g["id"] == genre_id), None)
    if not group:
        return []
    keywords = group["keywords"]
    matched = []
    seen_urls = set()

    # Si es Deportes, encabezar con las señales multi-mirror de TNT Sports y Deportes HD
    if genre_id == "deportes":
        from resources.lib import premium_channels
        for sch in premium_channels.TNT_AND_SPORTS_CHANNELS:
            u = sch.get("url", "")
            if u and u not in seen_urls:
                seen_urls.add(u)
                copy_s = dict(sch)
                copy_s["flag"] = "⚽"
                copy_s["category_es"] = "Deportes HD"
                copy_s["verified"] = True
                matched.append(copy_s)

    for ch in get_all_verified_latam_channels():
        u = ch.get("url", "")
        if u in seen_urls:
            continue
        haystack = f"{ch.get('name', '')} {ch.get('category', '')} {ch.get('category_es', '')}".lower()
        if any(k in haystack for k in keywords):
            seen_urls.add(u)
            matched.append(ch)
    return matched


def get_global_spanish_feed(max_items=350):
    """Descarga y cachea el feed global de televisión en idioma Español (languages/spa.m3u)."""
    url = "https://iptv-org.github.io/iptv/languages/spa.m3u"
    text = world_channels.fetch_url(url, "lang_spa.m3u")
    raw = world_channels.parse_m3u_text(text, max_items=max_items)
    for idx, ch in enumerate(raw, 1):
        ch["id"] = f"spa_global_{idx}"
        ch["category_es"] = translate_category(ch.get("category", ""))
    return raw

