# -*- coding: utf-8 -*-
"""
neno_pc Open Source Movies & Cine Español Latino HD Engine (v1.4.0)
Combina:
1. Catálogo Curado de Películas en 1080p Full HD y 720p HD en Español Latino, Anime/Series Latino y Obras Maestras Open Source
   con enlaces directos pre-resueltos (.mp4 / .mkv) para arranque instantáneo.
2. Motor de Exploración y Búsqueda en Vivo sobre Servidores Open Source:
   - Internet Archive JSON API (archive.org) filtrado en Español Latino / 1080p / 720p
   - PeerTube Fediverse Search API (SepiaSearch / Instancias Abiertas)
   - Soporte de Colecciones Multi-Archivo y Selector de Calidades / Servidores de Respaldo
"""

import json
import urllib.request
import urllib.parse
from resources.lib import network_helper

OPEN_MOVIES_CATALOG = [
    # ==========================================================
    # CINE FULL HD (1080P & 720P) EN ESPAÑOL LATINO (ENLACES DIRECTOS VERIFICADOS)
    # ==========================================================
    {
        "id": "lat_trolls_3_1080p",
        "title": "Trolls 3: Se Armó la Banda (1080p Full HD Español Latino)",
        "genre": "Animación / Familiar Latino",
        "language": "Español Latino 1080p",
        "quality": "1080p Full HD",
        "year": "2023",
        "rating": "7.3",
        "archive_id": "trolls-3_202312",
        "plot": "Poppy descubre que Branch formó parte en el pasado de su boyband favorita, BroZone, junto a sus cuatro hermanos. Cuando uno de ellos es secuestrado, Poppy y Branch se embarcan en un viaje musical para reunir a la familia. Audio Español Latino 1080p.",
        "poster": "https://archive.org/services/img/trolls-3_202312",
        "fanart": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=1280",
        "url": "https://archive.org/download/trolls-3_202312/tr0lls.b4nd.t0g3th3r.2023.hdrip.1080p.latino.mp4",
        "backup_urls": [
            "archive://trolls-3_202312"
        ]
    },
    {
        "id": "lat_angry_birds_1080",
        "title": "Angry Birds: La Película (1080p Full HD Español Latino)",
        "genre": "Animación / Familiar Latino",
        "language": "Español Latino 1080p",
        "quality": "1080p Full HD",
        "year": "2016",
        "rating": "7.2",
        "archive_id": "AngryBirds1080LatinoPelistvhd.com.mkv",
        "plot": "En una isla poblada por aves felices que no vuelan, Red, un pájaro con problemas de mal genio, el veloz Chuck y el volátil Bomb investigan la misteriosa llegada de unos cerdos verdes. Audio Español Latino Full HD.",
        "poster": "https://archive.org/services/img/AngryBirds1080LatinoPelistvhd.com.mkv",
        "fanart": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=1280",
        "url": "https://archive.org/download/AngryBirds1080LatinoPelistvhd.com.mkv/Angry%20Birds1080%20Latino-%20pelistvhd.com.mkv.mp4",
        "backup_urls": [
            "archive://AngryBirds1080LatinoPelistvhd.com.mkv"
        ]
    },
    {
        "id": "lat_porco_rosso_1080p",
        "title": "Porco Rosso - Studio Ghibli (1080p Full HD Español Latino)",
        "genre": "Animación / Anime Latino",
        "language": "Español Latino 1080p",
        "quality": "1080p Full HD",
        "year": "1992",
        "rating": "8.3",
        "archive_id": "porco-rosso-1992-1080p-aac",
        "plot": "Obra maestra de Hayao Miyazaki (Studio Ghibli). Marco Pagot es un experimentado piloto militar italiano que, tras un hechizo en la Primera Guerra Mundial, queda transformado en un cerdo antropomórfico y se dedica a cazar piratas aéreos en el Adriático.",
        "poster": "https://archive.org/services/img/porco-rosso-1992-1080p-aac",
        "fanart": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=1280",
        "url": "https://archive.org/download/porco-rosso-1992-1080p-aac/Porco%20Rosso%20%281992%29%201080p%20AAC.mkv",
        "backup_urls": [
            "archive://porco-rosso-1992-1080p-aac"
        ]
    },
    {
        "id": "lat_capitan_harlock_1080p",
        "title": "Capitán Harlock: Pirata Espacial (1080p Full HD Español Latino)",
        "genre": "Animación / Anime Latino",
        "language": "Español Latino 1080p",
        "quality": "1080p Full HD",
        "year": "2013",
        "rating": "7.6",
        "archive_id": "captain-herlock-espanol-latino-1080p-ec-92-eeb-8",
        "plot": "El legendario Capitán Harlock y la intrépida tripulación de su acorazado espacial Arcadia se rebelan contra la corrupta Coalición Gaia para defender el futuro de la humanidad.",
        "poster": "https://archive.org/services/img/captain-herlock-espanol-latino-1080p-ec-92-eeb-8",
        "fanart": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1280",
        "url": "https://archive.org/download/captain-herlock-espanol-latino-1080p-ec-92-eeb-8/Captain%20Herlock%20%5BEspa%C3%B1ol%20Latino%5D%20%5B1080p%5D%20%5BEC92EEB8%5D.mkv",
        "backup_urls": [
            "archive://captain-herlock-espanol-latino-1080p-ec-92-eeb-8"
        ]
    },
    {
        "id": "lat_dbz_broly_1080p",
        "title": "Dragon Ball Z: El Poder Invencible - Broly (1080p BluRay Español Latino)",
        "genre": "Animación / Anime Latino",
        "language": "Español Latino 1080p",
        "quality": "1080p Full HD",
        "year": "1993",
        "rating": "8.2",
        "archive_id": "dbz-08-el-poder-invencible-bluray-full-hd-1080p",
        "plot": "Paragus engaña a Vegeta para que viaje al Nuevo Planeta Vegeta, donde Gokú y los Guerreros Z se enfrentan al imparable Super Saiyajin Legendario: Broly. Edición BluRay 1080p con voces originales en Español Latino.",
        "poster": "https://archive.org/services/img/dbz-08-el-poder-invencible-bluray-full-hd-1080p",
        "fanart": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=1280",
        "url": "https://archive.org/download/dbz-08-el-poder-invencible-bluray-full-hd-1080p/DBZ%2008%20-%20El%20Poder%20Invencible%20Bluray%20FullHD%201080p.mkv",
        "backup_urls": [
            "archive://dbz-08-el-poder-invencible-bluray-full-hd-1080p"
        ]
    },
    {
        "id": "lat_dbz_bardock_1080p",
        "title": "Dragon Ball Z: La Batalla de Freezer contra el Padre de Gokú (1080p BluRay Latino)",
        "genre": "Animación / Anime Latino",
        "language": "Español Latino 1080p",
        "quality": "1080p Full HD",
        "year": "1990",
        "rating": "8.4",
        "archive_id": "dbz-especial-1-la-batalla-de-freezer-contra-el-padre-de-goku-bluray-full-hd-1080p",
        "plot": "Bardock, un guerrero Saiyajin de clase baja y padre de Kakarotto (Gokú), adquiere la capacidad de ver el futuro y descubre la traición de Freezer para destruir el Planeta Vegeta.",
        "poster": "https://archive.org/services/img/dbz-especial-1-la-batalla-de-freezer-contra-el-padre-de-goku-bluray-full-hd-1080p",
        "fanart": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=1280",
        "url": "https://archive.org/download/dbz-especial-1-la-batalla-de-freezer-contra-el-padre-de-goku-bluray-full-hd-1080p/DBZ%20Especial%201%20-%20La%20Batalla%20de%20Freezer%20Contra%20el%20Padre%20de%20Goku%20Bluray%20FullHD%201080p.mkv",
        "backup_urls": [
            "archive://dbz-especial-1-la-batalla-de-freezer-contra-el-padre-de-goku-bluray-full-hd-1080p"
        ]
    },
    {
        "id": "lat_dbz_batalla_dioses",
        "title": "Dragon Ball Z: La Batalla de los Dioses (Español Latino HD)",
        "genre": "Animación / Anime Latino",
        "language": "Español Latino HD",
        "quality": "720p HD",
        "year": "2013",
        "rating": "7.5",
        "archive_id": "dragon-ball-z-la-batalla-de-los-dioses-pelicula-completa-en-espanol-latino-hd",
        "plot": "Bills, el Dios de la Destrucción, despierta de un largo sueño en busca del legendario Super Saiyajin Fase Dios, obligando a Gokú y los Guerreros Z a librar la batalla más decisiva por la Tierra con las voces originales latinas.",
        "poster": "https://archive.org/services/img/dragon-ball-z-la-batalla-de-los-dioses-pelicula-completa-en-espanol-latino-hd",
        "fanart": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=1280",
        "url": "archive://dragon-ball-z-la-batalla-de-los-dioses-pelicula-completa-en-espanol-latino-hd",
        "backup_urls": []
    },
    {
        "id": "lat_antman_avispa_1080p",
        "title": "Ant-Man y La Avispa (1080p Full HD Español Latino)",
        "genre": "Acción / Ciencia Ficción Latino",
        "language": "Español Latino 1080p",
        "quality": "1080p Full HD",
        "year": "2018",
        "rating": "7.1",
        "archive_id": "Ver-Ant-Man-La-Avispa-Online-Espaol",
        "plot": "Scott Lang lidia con las consecuencias de sus elecciones como superhéroe y como padre mientras Hope van Dyne y el Dr. Hank Pym le encomiendan una urgente misión en el Reino Cuántico.",
        "poster": "https://archive.org/services/img/Ver-Ant-Man-La-Avispa-Online-Espaol",
        "fanart": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1280",
        "url": "https://archive.org/download/Ver-Ant-Man-La-Avispa-Online-Espaol/weasx_1%20-%20copia%20-%20copia.mp4",
        "backup_urls": [
            "archive://Ver-Ant-Man-La-Avispa-Online-Espaol"
        ]
    },
    {
        "id": "lat_buscando_dory_720p",
        "title": "Buscando a Dory (720p HD Español Latino)",
        "genre": "Animación / Familiar Latino",
        "language": "Español Latino HD",
        "quality": "720p HD",
        "year": "2016",
        "rating": "7.5",
        "archive_id": "buscando-a-dory-2016-720p-audio-latino",
        "plot": "La simpática y olvidadiza pez cirujano azul Dory recuerda de pronto que tiene una familia que podría estar buscándola, iniciando una gran aventura por el océano junto a Marlin y Nemo.",
        "poster": "https://archive.org/services/img/buscando-a-dory-2016-720p-audio-latino",
        "fanart": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=1280",
        "url": "https://archive.org/download/buscando-a-dory-2016-720p-audio-latino/Buscando%20a%20Dory%20%282016%29%20720p%20Audio%20Latino.mkv",
        "backup_urls": [
            "archive://buscando-a-dory-2016-720p-audio-latino"
        ]
    },
    {
        "id": "lat_tierra_osos_2_720p",
        "title": "Tierra de Osos 2 (720p HD Español Latino)",
        "genre": "Animación / Familiar Latino",
        "language": "Español Latino HD",
        "quality": "720p HD",
        "year": "2006",
        "rating": "7.0",
        "archive_id": "tierra-de-osos-2-2006-720p-audio-latino",
        "plot": "Kenai y su inseparable hermano pequeño Koda emprenden un viaje de verano cuando Kenai se reencuentra con Nita, su amiga de la infancia, con quien debe cumplir una misión ancestral.",
        "poster": "https://archive.org/services/img/tierra-de-osos-2-2006-720p-audio-latino",
        "fanart": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=1280",
        "url": "https://archive.org/download/tierra-de-osos-2-2006-720p-audio-latino/Tierra%20de%20Osos%202%20%282006%29%20720p%20Audio%20Latino.mkv",
        "backup_urls": [
            "archive://tierra-de-osos-2-2006-720p-audio-latino"
        ]
    },
    {
        "id": "lat_rey_leon_3_720p",
        "title": "El Rey León 3: Hakuna Matata (720p HD Español Latino)",
        "genre": "Animación / Familiar Latino",
        "language": "Español Latino HD",
        "quality": "720p HD",
        "year": "2004",
        "rating": "7.2",
        "archive_id": "el-rey-leon-1-12",
        "plot": "Timón y Pumba cuentan su propia e hilarante versión de la historia de El Rey León, revelando cómo se conocieron y cómo criaron al pequeño Simba.",
        "poster": "https://archive.org/services/img/el-rey-leon-1-12",
        "fanart": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=1280",
        "url": "https://archive.org/download/el-rey-leon-1-12/El%20rey%20le%C3%B3n%201%C2%BD.mkv",
        "backup_urls": [
            "archive://el-rey-leon-1-12"
        ]
    },
    {
        "id": "lat_era_hielo_4_hd",
        "title": "La Era de Hielo 4: La Deriva Continental (HD Español Latino)",
        "genre": "Animación / Familiar Latino",
        "language": "Español Latino HD",
        "quality": "720p HD",
        "year": "2012",
        "rating": "7.1",
        "archive_id": "la-era-de-hielo-4-la-deriva-continental-2012-hd-1080p-peliculas-completas-en-espanol-latino_202009",
        "plot": "La obsesión de Scrat por su bellota provoca la separación de los continentes, lanzando a Manny, Diego y Sid a una odisea marítima sobre un iceberg frente a una tripulación de piratas.",
        "poster": "https://archive.org/services/img/la-era-de-hielo-4-la-deriva-continental-2012-hd-1080p-peliculas-completas-en-espanol-latino_202009",
        "fanart": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=1280",
        "url": "https://archive.org/download/la-era-de-hielo-4-la-deriva-continental-2012-hd-1080p-peliculas-completas-en-espanol-latino_202009/la-era-de-hielo-4-la-deriva-continental-2012-hd-1080p-peliculas-completas-en-espanol-latino.mp4",
        "backup_urls": [
            "archive://la-era-de-hielo-4-la-deriva-continental-2012-hd-1080p-peliculas-completas-en-espanol-latino_202009"
        ]
    },
    {
        "id": "lat_marco_macaco_1080p",
        "title": "Marco Macaco (1080p Full HD Español Latino)",
        "genre": "Animación / Familiar Latino",
        "language": "Español Latino 1080p",
        "quality": "1080p Full HD",
        "year": "2012",
        "rating": "6.7",
        "archive_id": "marco-macaco-pelicula-completa-doblada-animacion-net-movies-peliculas-en-espanol-1080-p-hd",
        "plot": "Marco Macaco trabaja como oficial de playa en una isla tropical hasta que su rival Carlo construye un gigantesco casino con forma de mono que esconde un plan para apoderarse de la isla.",
        "poster": "https://archive.org/services/img/marco-macaco-pelicula-completa-doblada-animacion-net-movies-peliculas-en-espanol-1080-p-hd",
        "fanart": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=1280",
        "url": "https://archive.org/download/marco-macaco-pelicula-completa-doblada-animacion-net-movies-peliculas-en-espanol-1080-p-hd/Marco%20Macaco%20-%20Pel%C3%ADcula%20Completa%20Doblada%20-%20Animaci%C3%B3n%20_%20NetMovies%20-%20Pel%C3%ADculas%20En%20Espa%C3%B1ol%281080P_HD%29.mp4",
        "backup_urls": [
            "archive://marco-macaco-pelicula-completa-doblada-animacion-net-movies-peliculas-en-espanol-1080-p-hd"
        ]
    },
    {
        "id": "lat_click_sandler_720p",
        "title": "Click: Perdiendo el Control - Adam Sandler (720p HD Español Latino)",
        "genre": "Comedia / Humor Latino",
        "language": "Español Latino HD",
        "quality": "720p HD",
        "year": "2006",
        "rating": "7.4",
        "archive_id": "click-pelicula-completa-en-espan-ol-latino-hd-720-p-hd",
        "plot": "Michael Newman (Adam Sandler), un arquitecto adicto al trabajo, consigue un control remoto universal capaz de pausar, rebobinar y adelantar su propia vida, hasta que el aparato empieza a tomar el control.",
        "poster": "https://archive.org/services/img/click-pelicula-completa-en-espan-ol-latino-hd-720-p-hd",
        "fanart": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=1280",
        "url": "https://archive.org/download/click-pelicula-completa-en-espan-ol-latino-hd-720-p-hd/CLICK%20PELICULA%20COMPLETA%20EN%20ESPA%C3%91OL%20LATINO%20HD%28720P_HD%29.mp4",
        "backup_urls": [
            "archive://click-pelicula-completa-en-espan-ol-latino-hd-720-p-hd",
            "archive://click-perdiendo-el-control-comedia-pelicula-completa-en-espanol-latino-hd"
        ]
    },
    {
        "id": "lat_ace_ventura_duologia_720p",
        "title": "📦 [Duología] Ace Ventura 1 & 2 - Jim Carrey (720p HD Español Latino)",
        "genre": "Comedia / Humor Latino",
        "language": "Español Latino HD",
        "quality": "720p HD",
        "year": "1994",
        "rating": "7.6",
        "is_collection": True,
        "archive_id": "0076-ace-ventura-1-1994-720p-d-sspa-v",
        "plot": "Duología completa en 720p de Ace Ventura: Un Detective Diferente (1994) y Ace Ventura en África (1995) protagonizada por Jim Carrey con doblaje en Español.",
        "poster": "https://archive.org/services/img/0076-ace-ventura-1-1994-720p-d-sspa-v",
        "fanart": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=1280",
        "url": "https://archive.org/download/0076-ace-ventura-1-1994-720p-d-sspa-v/0077-Ace%20Ventura%202%20%281995%29%20720p%20D%20Sspa%20v.mkv",
        "backup_urls": [
            "archive://0076-ace-ventura-1-1994-720p-d-sspa-v"
        ]
    },
    {
        "id": "lat_precio_manana_hd",
        "title": "El Precio del Mañana / In Time (HD Español Latino)",
        "genre": "Acción / Ciencia Ficción Latino",
        "language": "Español Latino HD",
        "quality": "720p HD",
        "year": "2011",
        "rating": "7.3",
        "archive_id": "el-precio-del-manana-2011-pelicula-completa-espanol-latino-hd",
        "plot": "En un futuro donde el envejecimiento se detiene a los 25 años y el tiempo de vida se ha convertido en la única moneda de cambio, Will Salas (Justin Timberlake) es acusado falsamente de asesinato y lucha contra el sistema.",
        "poster": "https://archive.org/services/img/el-precio-del-manana-2011-pelicula-completa-espanol-latino-hd",
        "fanart": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1280",
        "url": "https://archive.org/download/el-precio-del-manana-2011-pelicula-completa-espanol-latino-hd/El%20Precio%20del%20ma%C3%B1ana%202011%20-%20Pel%C3%ADcula%20Completa%20Espa%C3%B1ol%20Latino%20HD.mp4",
        "backup_urls": [
            "archive://el-precio-del-manana-2011-pelicula-completa-espanol-latino-hd"
        ]
    },
    {
        "id": "lat_maximo_riesgo_720p",
        "title": "Máximo Riesgo / Cliffhanger - Stallone (720p HD Dual Español)",
        "genre": "Acción / Aventura Latino",
        "language": "Español Latino HD",
        "quality": "720p HD",
        "year": "1993",
        "rating": "7.4",
        "archive_id": "4441-maximo-riesgo-1993-720p-d-s-spa-eng-v_20240208",
        "plot": "Gabe Walker (Sylvester Stallone), un experimentado rescatista de montaña en las Rocosas, se ve obligado a enfrentar a un grupo de criminales armados que buscan recuperar maletines con 100 millones de dólares tras un accidente aéreo.",
        "poster": "https://archive.org/services/img/4441-maximo-riesgo-1993-720p-d-s-spa-eng-v_20240208",
        "fanart": "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=1280",
        "url": "https://archive.org/download/4441-maximo-riesgo-1993-720p-d-s-spa-eng-v_20240208/4441-Maximo%20Riesgo%20%281993%29%20720p%20D%20S%20spa%20eng%20v.mkv",
        "backup_urls": [
            "archive://4441-maximo-riesgo-1993-720p-d-s-spa-eng-v_20240208"
        ]
    },
    {
        "id": "lat_taxi_driver_1080p",
        "title": "Taxi Driver - Robert De Niro (1080p Full HD Doblaje Latino)",
        "genre": "Drama / Suspenso Latino",
        "language": "Español Latino 1080p",
        "quality": "1080p Full HD",
        "year": "1976",
        "rating": "8.6",
        "archive_id": "taxi-driver-1976_202512",
        "plot": "Clásico de Martin Scorsese protagonizado por Robert De Niro. Travis Bickle, un veterano de guerra con insomnio crónico, trabaja como taxista nocturno en las calles de Nueva York mientras desciende en una espiral de obsesión. Edición 35mm 1080p con doblajes latinos.",
        "poster": "https://archive.org/services/img/taxi-driver-1976_202512",
        "fanart": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=1280",
        "url": "https://archive.org/download/taxi-driver-1976_202512/Taxi%20Driver%201976%201080p%2035mm%20Latino%201er%20Mex%20-%202do%20Mex%20-%204to%20Arg.mkv",
        "backup_urls": [
            "archive://taxi-driver-1976_202512"
        ]
    },
    {
        "id": "lat_shutter_1080p",
        "title": "Shutter: Están Entre Nosotros (1080p Full HD Español Latino)",
        "genre": "Terror / Clásicos Open Source",
        "language": "Español Latino 1080p",
        "quality": "1080p Full HD",
        "year": "2004",
        "rating": "7.5",
        "archive_id": "4137-shutter-2004-1080p-d-t-s-spa-eng-por-fre-v-1-ok-ru",
        "plot": "Un joven fotógrafo y su novia descubren misteriosas sombras blancas en sus fotografías tras sufrir un accidente en una carretera solitaria, desentrañando un aterrador secreto.",
        "poster": "https://archive.org/services/img/4137-shutter-2004-1080p-d-t-s-spa-eng-por-fre-v-1-ok-ru",
        "fanart": "https://images.unsplash.com/photo-1509248961158-e54f6934749c?w=1280",
        "url": "https://archive.org/download/4137-shutter-2004-1080p-d-t-s-spa-eng-por-fre-v-1-ok-ru/%D0%92%D0%B8%D0%B4%D0%B5%D0%BE%204137-Shutter%202004%201080p%20D%20t%20S%20spa%20eng%20por%20fre%20v%201%20OK%20RU.mp4",
        "backup_urls": [
            "archive://4137-shutter-2004-1080p-d-t-s-spa-eng-por-fre-v-1-ok-ru"
        ]
    },
    {
        "id": "lat_azumi_1_1080p",
        "title": "Azumi: La Princesa Guerrera (1080p HD Español Latino)",
        "genre": "Acción / Aventura Latino",
        "language": "Español Latino 1080p",
        "quality": "1080p Full HD",
        "year": "2003",
        "rating": "7.3",
        "archive_id": "azumi-la-princesa-guerrera-2003-pelicula-completa-latino-1080-hd",
        "plot": "En el Japón feudal devastado por la guerra, una joven huérfana llamada Azumi es entrenada en secreto desde niña como una letal maestra de la espada con la misión de eliminar a los señores de la guerra.",
        "poster": "https://archive.org/services/img/azumi-la-princesa-guerrera-2003-pelicula-completa-latino-1080-hd",
        "fanart": "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=1280",
        "url": "https://archive.org/download/azumi-la-princesa-guerrera-2003-pelicula-completa-latino-1080-hd/AZUMI%20_%20LA%20PRINCESA%20GUERRERA%20%282003%29%20PELICULA%20COMPLETA%20LATINO%201080HD.mp4",
        "backup_urls": [
            "archive://azumi-la-princesa-guerrera-2003-pelicula-completa-latino-1080-hd"
        ]
    },
    {
        "id": "lat_azumi_2_1080p",
        "title": "Azumi 2: La Última Guerrera (1080p HD Español Latino)",
        "genre": "Acción / Aventura Latino",
        "language": "Español Latino 1080p",
        "quality": "1080p Full HD",
        "year": "2005",
        "rating": "7.1",
        "archive_id": "azumi-2-la-ultima-guerrera-2005-pelicula-completa-latino-1080-hd",
        "plot": "Secuela directa en Español Latino donde Azumi continúa su implacable misión enfrentando a un clan de ninjas de élite en el Japón feudal.",
        "poster": "https://archive.org/services/img/azumi-2-la-ultima-guerrera-2005-pelicula-completa-latino-1080-hd",
        "fanart": "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=1280",
        "url": "https://archive.org/download/azumi-2-la-ultima-guerrera-2005-pelicula-completa-latino-1080-hd/AZUMI%202%20_%20LA%20ULTIMA%20GUERRERA%20%282005%29%20PELICULA%20COMPLETA%20LATINO%201080HD.mp4",
        "backup_urls": [
            "archive://azumi-2-la-ultima-guerrera-2005-pelicula-completa-latino-1080-hd"
        ]
    },
    {
        "id": "lat_voces_inocentes_1080p",
        "title": "Voces Inocentes (1080p 60fps Cine Latinoamericano)",
        "genre": "Cine Latinoamericano & Época de Oro",
        "language": "Español Latino 1080p",
        "quality": "1080p Full HD",
        "year": "2004",
        "rating": "8.4",
        "archive_id": "voces-inocentes-2004-hd-1080p-60fps-latino-pelicula-completa-h-qy-453p-k-5bk",
        "plot": "Conmovedora obra maestra dirigida por Luis Mandoki. Chava, un niño de once años en El Salvador durante la década de 1980, se convierte en el ”hombre de la casa” mientras intenta escapar del reclutamiento forzoso.",
        "poster": "https://archive.org/services/img/voces-inocentes-2004-hd-1080p-60fps-latino-pelicula-completa-h-qy-453p-k-5bk",
        "fanart": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=1280",
        "url": "https://archive.org/download/voces-inocentes-2004-hd-1080p-60fps-latino-pelicula-completa-h-qy-453p-k-5bk/Voces%20inocentes%202004%20hd%201080p%2060fps%20Latino%20Pelicula%20Completa%20%5BhQy453pK5bk%5D.mp4",
        "backup_urls": [
            "archive://voces-inocentes-2004-hd-1080p-60fps-latino-pelicula-completa-h-qy-453p-k-5bk"
        ]
    },
    {
        "id": "lat_puente_rio_kwai_720p",
        "title": "El Puente Sobre el Río Kwai (720p HD Dual Español)",
        "genre": "Drama / Suspenso Latino",
        "language": "Español Latino HD",
        "quality": "720p HD",
        "year": "1957",
        "rating": "8.3",
        "archive_id": "2433-el-puente-sobre-el-rio-kwai-1957-720p-d-s-spa-eng-v_202402",
        "plot": "Ganadora de 7 premios Óscar. Prisioneros de guerra británicos son obligados a construir un puente ferroviario estratégico en la selva de Birmania durante la Segunda Guerra Mundial.",
        "poster": "https://archive.org/services/img/2433-el-puente-sobre-el-rio-kwai-1957-720p-d-s-spa-eng-v_202402",
        "fanart": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=1280",
        "url": "https://archive.org/download/2433-el-puente-sobre-el-rio-kwai-1957-720p-d-s-spa-eng-v_202402/2433-El%20Puente%20Sobre%20El%20Rio%20Kwai%20%281957%29%20720p%20D%20S%20spa%20eng%20v.mkv",
        "backup_urls": [
            "archive://2433-el-puente-sobre-el-rio-kwai-1957-720p-d-s-spa-eng-v_202402"
        ]
    },
    {
        "id": "lat_batalla_por_terra_720p",
        "title": "Batalla por Terra (720p HD Animación Español Latino)",
        "genre": "Animación / Familiar Latino",
        "language": "Español Latino HD",
        "quality": "720p HD",
        "year": "2007",
        "rating": "7.1",
        "archive_id": "batalla-por-terra-2007-720p",
        "plot": "Un pacífico planeta alienígena llamado Terra se ve amenazado por los últimos supervivientes de la raza humana, pero la amistad entre una joven habitante de Terra y un piloto humano cambiará el destino de ambos mundos.",
        "poster": "https://archive.org/services/img/batalla-por-terra-2007-720p",
        "fanart": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1280",
        "url": "https://archive.org/download/batalla-por-terra-2007-720p/Batalla%20Por%20Terra%20%282007%29%20720p.mp4",
        "backup_urls": [
            "archive://batalla-por-terra-2007-720p"
        ]
    },
    {
        "id": "lat_apocalypto_2006",
        "title": "Apocalypto (Español Latino HD)",
        "genre": "Acción / Aventura Latino",
        "language": "Español Latino HD",
        "quality": "720p HD",
        "year": "2006",
        "rating": "7.8",
        "archive_id": "apocalypto-2006-online-latino-castellano-y-subtitulada",
        "plot": "Antes de la llegada de los conquistadores, un joven cazador maya llamado Garra de Jaguar es capturado junto a su tribu para ser sacrificado, iniciando una implacable huida por la selva para salvar a su familia.",
        "poster": "https://archive.org/services/img/apocalypto-2006-online-latino-castellano-y-subtitulada",
        "fanart": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1280",
        "url": "https://archive.org/download/apocalypto-2006-online-latino-castellano-y-subtitulada/Apocalypto%20%282006%29%20Online%20Latino%2C%20Castellano%20y%20Subtitulada.mp4",
        "backup_urls": [
            "archive://apocalypto-2006-online-latino-castellano-y-subtitulada"
        ]
    },
    {
        "id": "lat_rambo_1982",
        "title": "Rambo: Programado Para Matar (Doblaje Español Latino)",
        "genre": "Acción / Aventura Latino",
        "language": "Español Latino",
        "year": "1982",
        "rating": "7.7",
        "archive_id": "Rambo1",
        "plot": "El veterano boina verde John Rambo (Sylvester Stallone) es arrestado injustamente por el sheriff de un pequeño pueblo y obligado a huir hacia las montañas, desatando una guerra de supervivencia. Doblaje clásico Español Latino.",
        "poster": "https://archive.org/services/img/Rambo1",
        "fanart": "https://images.unsplash.com/photo-1509248961158-e54f6934749c?w=1280",
        "url": "archive://Rambo1",
        "backup_urls": []
    },
    {
        "id": "lat_metegol_2013",
        "title": "Metegol / Futbolín (Animación Español Latino)",
        "genre": "Animación / Familiar Latino",
        "language": "Español Latino",
        "year": "2013",
        "rating": "6.6",
        "archive_id": "metegol.-2013.-dvdrip.-xvi-d.-latino.-argentino.-sbt",
        "plot": "Dirigida por Juan José Campanella. Amadeo, un chico tímido pero invencible jugando al metegol, recibe la ayuda mágica de los jugadores de plomo de su mesa cuando el campeón mundial regresa al pueblo buscando venganza.",
        "poster": "https://archive.org/services/img/metegol.-2013.-dvdrip.-xvi-d.-latino.-argentino.-sbt",
        "fanart": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=1280",
        "url": "archive://metegol.-2013.-dvdrip.-xvi-d.-latino.-argentino.-sbt",
        "backup_urls": []
    },
    {
        "id": "lat_liga_justicia_720",
        "title": "Liga de la Justicia (720p HD Español Latino)",
        "genre": "Acción / Ciencia Ficción Latino",
        "language": "Español Latino HD",
        "quality": "720p HD",
        "year": "2017",
        "rating": "6.8",
        "archive_id": "cesser-16-liga-de-la-justicia-720p",
        "plot": "Impulsado por su restaurada fe en la humanidad e inspirado por el acto desinteresado de Superman, Bruce Wayne recluta a Wonder Woman, Aquaman, Cyborg y Flash para enfrentar una amenaza catastrófica.",
        "poster": "https://archive.org/services/img/cesser-16-liga-de-la-justicia-720p",
        "fanart": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1280",
        "url": "archive://cesser-16-liga-de-la-justicia-720p",
        "backup_urls": []
    },
    {
        "id": "lat_codigo_enigma",
        "title": "El Código Enigma (Español Latino HD)",
        "genre": "Drama / Suspenso Latino",
        "language": "Español Latino HD",
        "quality": "720p HD",
        "year": "2014",
        "rating": "8.0",
        "archive_id": "ElCdigoEnigmaPelculaCompletaEnEspaolLatinoYouTube",
        "plot": "Durante la Segunda Guerra Mundial, el genio matemático Alan Turing lidera un equipo secreto en Bletchley Park con la misión de descifrar la inquebrantable máquina nazi Enigma.",
        "poster": "https://archive.org/services/img/ElCdigoEnigmaPelculaCompletaEnEspaolLatinoYouTube",
        "fanart": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=1280",
        "url": "archive://ElCdigoEnigmaPelculaCompletaEnEspaolLatinoYouTube",
        "backup_urls": []
    },
    {
        "id": "lat_el_pianista",
        "title": "El Pianista (Película Completa Español HD)",
        "genre": "Drama / Suspenso Latino",
        "language": "Español Latino HD",
        "quality": "720p HD",
        "year": "2002",
        "rating": "8.5",
        "archive_id": "el-pianista-en-espanol-pelicula-completa-en-hd-segunda-guerra-mundial-1939",
        "plot": "Wladyslaw Szpilman, un brillante pianista polaco de origen judío, lucha por sobrevivir a la destrucción del gueto de Varsovia durante la ocupación en la Segunda Guerra Mundial.",
        "poster": "https://archive.org/services/img/el-pianista-en-espanol-pelicula-completa-en-hd-segunda-guerra-mundial-1939",
        "fanart": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=1280",
        "url": "archive://el-pianista-en-espanol-pelicula-completa-en-hd-segunda-guerra-mundial-1939",
        "backup_urls": []
    },
    {
        "id": "lat_idiocracia_2006",
        "title": "Idiocracia (Comedia Sci-Fi Español 720p)",
        "genre": "Comedia / Humor Latino",
        "language": "Español 720p",
        "quality": "720p HD",
        "year": "2006",
        "rating": "6.5",
        "archive_id": "idiocracia-2006-brrip-m-720p-x-264-ac-3-es",
        "plot": "Un soldado completamente promedio participa en un experimento militar de hibernación y despierta 500 años en el futuro, descubriendo que la humanidad se ha vuelto tan absurda que él es el hombre más inteligente del planeta.",
        "poster": "https://archive.org/services/img/idiocracia-2006-brrip-m-720p-x-264-ac-3-es",
        "fanart": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=1280",
        "url": "archive://idiocracia-2006-brrip-m-720p-x-264-ac-3-es",
        "backup_urls": []
    },
    {
        "id": "lat_scary_movie",
        "title": "Scary Movie: Una Película de Miedo (Español)",
        "genre": "Comedia / Humor Latino",
        "language": "Español",
        "year": "2000",
        "rating": "6.3",
        "archive_id": "scary-movie-pelicula-completa-en-espanol",
        "plot": "Parodia irreverente de los clásicos del cine de terror adolescente donde un grupo de jóvenes intenta escapar de un asesino enmascarado tras un accidente de tráfico.",
        "poster": "https://archive.org/services/img/scary-movie-pelicula-completa-en-espanol",
        "fanart": "https://images.unsplash.com/photo-1509248961158-e54f6934749c?w=1280",
        "url": "archive://scary-movie-pelicula-completa-en-espanol",
        "backup_urls": []
    },
    {
        "id": "lat_ese_es_mi_hijo",
        "title": "Ese Es Mi Hijo (Comedia Español Latino)",
        "genre": "Comedia / Humor Latino",
        "language": "Español Latino",
        "year": "2012",
        "rating": "5.7",
        "archive_id": "darsag2",
        "plot": "Donny (Adam Sandler) tuvo a su hijo Todd siendo muy joven. Tras años sin verse, Donny reaparece sin invitación justo en la víspera de la lujosa boda de su hijo para intentar conseguir dinero urgente.",
        "poster": "https://archive.org/services/img/darsag2",
        "fanart": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=1280",
        "url": "archive://darsag2",
        "backup_urls": []
    },
    {
        "id": "lat_como_me_converti_superheroe",
        "title": "Cómo Me Convertí en Superhéroe (Español Latino)",
        "genre": "Acción / Ciencia Ficción Latino",
        "language": "Español Latino",
        "year": "2020",
        "rating": "6.0",
        "archive_id": "como-me-converti-en-superheroe",
        "plot": "En un mundo donde los humanos y los superhéroes conviven, un policía solitario une fuerzas con una brillante detective para desmantelar una red de tráfico de sustancias que otorgan superpoderes.",
        "poster": "https://archive.org/services/img/como-me-converti-en-superheroe",
        "fanart": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1280",
        "url": "archive://como-me-converti-en-superheroe",
        "backup_urls": []
    },
    {
        "id": "lat_enemigo_inmortal_jackie",
        "title": "Enemigo Inmortal - Jackie Chan (Español Latino)",
        "genre": "Acción / Aventura Latino",
        "language": "Español Latino",
        "year": "2003",
        "rating": "6.0",
        "archive_id": "peliculas-completas-en-espanol-latino-castellano-enemigo-inmortal-jackie-chan-ci",
        "plot": "Un policía de Hong Kong (Jackie Chan) sufre un accidente letal mientras persigue a un criminal, pero el poder de un medallón sagrado le devuelve la vida con habilidades sobrehumanas.",
        "poster": "https://archive.org/services/img/peliculas-completas-en-espanol-latino-castellano-enemigo-inmortal-jackie-chan-ci",
        "fanart": "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=1280",
        "url": "archive://peliculas-completas-en-espanol-latino-castellano-enemigo-inmortal-jackie-chan-ci",
        "backup_urls": []
    },
    {
        "id": "lat_tres_veces_tu",
        "title": "Tres Veces Tú (Romance Español Latino HD)",
        "genre": "Drama / Suspenso Latino",
        "language": "Español Latino HD",
        "year": "2018",
        "rating": "6.8",
        "archive_id": "VerTresVecesTuPelculaCompletaOnlineGratisDescargarl",
        "plot": "Capítulo desenlace de la célebre historia romántica de Tres Metros Sobre el Cielo, donde el pasado, el primer amor y las decisiones adultas vuelven a cruzarse.",
        "poster": "https://archive.org/services/img/VerTresVecesTuPelculaCompletaOnlineGratisDescargarl",
        "fanart": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=1280",
        "url": "https://archive.org/download/VerTresVecesTuPelculaCompletaOnlineGratisDescargarl/Ver%20Tres%20veces%20tu%20pel%C3%ADcula%20completa%20online%20gratis%20descargarl.mp4",
        "backup_urls": [
            "archive://Ver3VecesTuPeliculaCompletaOnlineEnEspanolLatino2018"
        ]
    },
    {
        "id": "lat_el_santo_2017",
        "title": "El Santo (Acción 720p Español Latino)",
        "genre": "Acción / Aventura Latino",
        "language": "Español Latino HD",
        "quality": "720p HD",
        "year": "2017",
        "rating": "6.2",
        "archive_id": "cesser-16-el-santo-2017-720p",
        "plot": "El maestro ladrón internacional Simon Templar, conocido como El Santo, es contratado por un banquero desesperado para rescatar a su hija secuestrada.",
        "poster": "https://archive.org/services/img/cesser-16-el-santo-2017-720p",
        "fanart": "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=1280",
        "url": "archive://cesser-16-el-santo-2017-720p",
        "backup_urls": []
    },
    {
        "id": "lat_el_infierno_mx",
        "title": "El Infierno (Cine Mexicano Español Latino)",
        "genre": "Cine Latinoamericano & Época de Oro",
        "language": "Español Latino",
        "year": "2010",
        "rating": "7.8",
        "archive_id": "el-infierno-pelicula-completa-latino-480-x-640",
        "plot": "Benny García regresa a su pueblo natal en México tras veinte años como migrante en Estados Unidos, encontrándose con una realidad transformada por el crimen y la sátira social. Protagonizada por Damián Alcázar y Joaquín Cosío.",
        "poster": "https://archive.org/services/img/el-infierno-pelicula-completa-latino-480-x-640",
        "fanart": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=1280",
        "url": "archive://el-infierno-pelicula-completa-latino-480-x-640",
        "backup_urls": []
    },
    {
        "id": "lat_guerrera_vengadora",
        "title": "La Guerrera Vengadora (Cine de Acción Mexicano)",
        "genre": "Cine Latinoamericano & Época de Oro",
        "language": "Español Latino",
        "year": "1988",
        "rating": "6.4",
        "archive_id": "LaGuerreraVengadora",
        "plot": "Clásico del cine de acción mexicano protagonizado por Rosa Gloria Chagoyán, donde una intrépida motociclista combate una banda criminal.",
        "poster": "https://archive.org/services/img/LaGuerreraVengadora",
        "fanart": "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=1280",
        "url": "archive://LaGuerreraVengadora",
        "backup_urls": []
    },
    {
        "id": "lat_santa_claus_1959",
        "title": "Santa Claus (Clásico del Cine Mexicano 1959)",
        "genre": "Cine Latinoamericano & Época de Oro",
        "language": "Español / Dominio Público",
        "year": "1959",
        "rating": "6.1",
        "archive_id": "santa-claus-1959",
        "plot": "Película clásica dirigida por René Cardona en los Estudios Churubusco de México. Santa Claus debe enfrentarse desde su castillo espacial a las travesuras del diablillo Precio que intenta sabotear la Navidad.",
        "poster": "https://archive.org/services/img/santa-claus-1959",
        "fanart": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=1280",
        "url": "archive://santa-claus-1959",
        "backup_urls": []
    },

    # ==========================================================
    # COLECCIONES, ANIME Y SERIES EN ESPAÑOL LATINO (MULTI-ARCHIVO)
    # ==========================================================
    {
        "id": "col_ranma_latino",
        "title": "📦 [Colección] Ranma ½ (161 Episodios Español Latino)",
        "genre": "Animación / Anime Latino",
        "language": "Español Latino",
        "year": "1993",
        "rating": "8.6",
        "is_collection": True,
        "archive_id": "ranma-nibunnoichi-espanol-latino-y-japones",
        "plot": "Colección completa en Español Latino de las aventuras de Ranma Saotome y Akane Tendo. Haz clic para explorar y reproducir cualquiera de los 161 episodios en servidor Open Source.",
        "poster": "https://archive.org/services/img/ranma-nibunnoichi-espanol-latino-y-japones",
        "fanart": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=1280",
        "url": "archive://ranma-nibunnoichi-espanol-latino-y-japones"
    },
    {
        "id": "col_sakura_latino",
        "title": "📦 [Colección] Sakura Card Captor (Español Latino)",
        "genre": "Animación / Anime Latino",
        "language": "Español Latino",
        "year": "2000",
        "rating": "8.4",
        "is_collection": True,
        "archive_id": "sakura-card-captor-en-espanol-latino",
        "plot": "Serie completa de Sakura Kinomoto y la captura de las Cartas Clow con su inolvidable doblaje al Español Latino.",
        "poster": "https://archive.org/services/img/sakura-card-captor-en-espanol-latino",
        "fanart": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=1280",
        "url": "archive://sakura-card-captor-en-espanol-latino"
    },
    {
        "id": "col_malcolm_latino",
        "title": "📦 [Colección] Malcolm el de en Medio (Español Latino)",
        "genre": "Comedia / Humor Latino",
        "language": "Español Latino",
        "year": "2000",
        "rating": "8.8",
        "is_collection": True,
        "archive_id": "malcolm-el-de-en-medio-t-01",
        "plot": "Episodios completos de Malcolm el de en Medio con su clásico doblaje en Español Latino. Haz clic para elegir episodio.",
        "poster": "https://archive.org/services/img/malcolm-el-de-en-medio-t-01",
        "fanart": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=1280",
        "url": "archive://malcolm-el-de-en-medio-t-01"
    },
    {
        "id": "col_chainsaw_latino",
        "title": "📦 [Colección] Chainsaw Man (Doblaje Español Latino 1080p HD)",
        "genre": "Animación / Anime Latino",
        "language": "Español Latino 1080p",
        "quality": "1080p Full HD",
        "year": "2022",
        "rating": "8.5",
        "is_collection": True,
        "archive_id": "chainsaw-man-latino-",
        "plot": "Temporada completa de Chainsaw Man doblada al Español Latino en alta definición.",
        "poster": "https://archive.org/services/img/chainsaw-man-latino-",
        "fanart": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=1280",
        "url": "archive://chainsaw-man-latino-"
    },
    {
        "id": "col_kaisen_latino",
        "title": "📦 [Colección] Jujutsu Kaisen (Doblaje Español Latino 1080p HD)",
        "genre": "Animación / Anime Latino",
        "language": "Español Latino 1080p",
        "quality": "1080p Full HD",
        "year": "2020",
        "rating": "8.6",
        "is_collection": True,
        "archive_id": "kaisen-1-12-latino",
        "plot": "Episodios de Jujutsu Kaisen en Español Latino alojados en servidores abiertos.",
        "poster": "https://archive.org/services/img/kaisen-1-12-latino",
        "fanart": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=1280",
        "url": "archive://kaisen-1-12-latino"
    },
    {
        "id": "col_casa_dibujos_latino",
        "title": "📦 [Colección] La Casa de los Dibujos (Español Latino)",
        "genre": "Comedia / Humor Latino",
        "language": "Español Latino",
        "year": "2004",
        "rating": "8.1",
        "is_collection": True,
        "archive_id": "lacasadelosdibujoslat_202301",
        "plot": "Colección de episodios de La Casa de los Dibujos con el doblaje clásico en Español Latino.",
        "poster": "https://archive.org/services/img/lacasadelosdibujoslat_202301",
        "fanart": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=1280",
        "url": "archive://lacasadelosdibujoslat_202301"
    },

    # ==========================================================
    # CLÁSICOS DE CULTO, TERROR & OPEN SOURCE (MULTI-SERVER HD)
    # ==========================================================
    {
        "id": "open_night_living_dead",
        "title": "La Noche de los Muertos Vivientes (1080p Remaster)",
        "genre": "Terror / Clásicos Open Source",
        "language": "Open Source 1080p",
        "quality": "1080p Full HD",
        "year": "1968",
        "rating": "7.9",
        "archive_id": "Night.Of.The.Living.Dead_1080p",
        "plot": "Un grupo de desconocidos se refugia en una casa rural de Pensilvania cuando los muertos comienzan a levantarse de sus tumbas. El clásico fundacional del cine zombi de George A. Romero.",
        "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Night_of_the_Living_Dead_theatrical_poster.jpg/440px-Night_of_the_Living_Dead_theatrical_poster.jpg",
        "fanart": "https://images.unsplash.com/photo-1509248961158-e54f6934749c?w=1280",
        "url": "https://archive.org/download/Night.Of.The.Living.Dead_1080p/NightOfTheLivingDead.mp4",
        "backup_urls": [
            "archive://Night.Of.The.Living.Dead_1080p"
        ]
    },
    {
        "id": "open_house_haunted_hill",
        "title": "House on Haunted Hill (Mansión de los Horrores)",
        "genre": "Terror / Clásicos Open Source",
        "language": "Open Source HD",
        "year": "1959",
        "rating": "6.8",
        "archive_id": "HouseOnHauntedHill1959",
        "plot": "Un millonario excéntrico (Vincent Price) invita a cinco personas a una fiesta en una casa encantada, ofreciéndoles 10.000 dólares a quien logre sobrevivir la noche entera encerrado.",
        "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/House_on_Haunted_Hill_poster.jpg/440px-House_on_Haunted_Hill_poster.jpg",
        "fanart": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1280",
        "url": "https://archive.org/download/HouseOnHauntedHill1959/House-On-Haunted-Hill.mp4",
        "backup_urls": ["archive://HouseOnHauntedHill1959"]
    },
    {
        "id": "open_last_man_earth",
        "title": "El Último Hombre Sobre la Tierra (Soy Leyenda Original)",
        "genre": "Terror / Clásicos Open Source",
        "language": "Open Source HD",
        "year": "1964",
        "rating": "6.9",
        "archive_id": "lastmanonearth-1964",
        "plot": "El Dr. Robert Morgan (Vincent Price) es el único superviviente de una plaga que convirtió a la humanidad en criaturas nocturnas. Primera adaptación de 'Soy Leyenda'.",
        "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/The_Last_Man_on_Earth_poster.jpg/440px-The_Last_Man_on_Earth_poster.jpg",
        "fanart": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1280",
        "url": "https://archive.org/download/lastmanonearth-1964/lastmanonearth-1964.mp4",
        "backup_urls": ["archive://lastmanonearth-1964"]
    },
    {
        "id": "open_nosferatu",
        "title": "Nosferatu: Una Sinfonía del Horror (Edición Restaurada)",
        "genre": "Terror / Clásicos Open Source",
        "language": "Open Source HD",
        "year": "1922",
        "rating": "7.9",
        "archive_id": "Nosferatu_DVD_quality",
        "plot": "Hutter viaja a los Cárpatos para cerrar la venta de una finca con el misterioso conde Orlok, sin sospechar que se trata de un vampiro ancestral.",
        "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Nosferatu_poster.jpg/440px-Nosferatu_poster.jpg",
        "fanart": "https://images.unsplash.com/photo-1509248961158-e54f6934749c?w=1280",
        "url": "https://archive.org/download/Nosferatu_DVD_quality/Nosferatu.mp4",
        "backup_urls": ["archive://Nosferatu_DVD_quality"]
    },
    {
        "id": "open_tears_of_steel",
        "title": "Tears of Steel (Ciencia Ficción 4K Open Movie)",
        "genre": "Acción / Ciencia Ficción Latino",
        "language": "Open Source 4K",
        "quality": "1080p Full HD",
        "year": "2012",
        "rating": "8.0",
        "plot": "En un futuro distópico en Ámsterdam, un grupo de científicos y luchadores rebeldes ejecutan una simulación para evitar la rebelión mundial de los robots.",
        "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Tears_of_Steel_poster.jpg/440px-Tears_of_Steel_poster.jpg",
        "fanart": "https://mango.blender.org/wp-content/uploads/2012/09/01_comp_00060.jpg",
        "url": "https://demo.unified-streaming.com/k8s/features/stable/video/tears-of-steel/tears-of-steel.ism/.m3u8",
        "backup_urls": [
            "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4"
        ]
    },
    {
        "id": "open_sintel_dragon",
        "title": "Sintel: El Viaje del Dragón (Fantasía Full HD)",
        "genre": "Animación / Familiar Latino",
        "language": "Open Source 1080p",
        "quality": "1080p Full HD",
        "year": "2010",
        "rating": "8.1",
        "plot": "Una joven guerrera solitaria recorre tierras peligrosas para rescatar a su pequeño amigo dragón Scales.",
        "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Sintel_poster.jpg/440px-Sintel_poster.jpg",
        "fanart": "https://durian.blender.org/wp-content/uploads/2010/09/sintel_artwork.jpg",
        "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4",
        "backup_urls": []
    },
    {
        "id": "open_big_buck_bunny",
        "title": "Big Buck Bunny (Animación 3D 1080p Open Source)",
        "genre": "Animación / Familiar Latino",
        "language": "Open Source 1080p",
        "quality": "1080p Full HD",
        "year": "2008",
        "rating": "7.9",
        "plot": "Un enorme y pacífico conejo gigante decide darle una lección inolvidable a tres roedores traviesos del bosque.",
        "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Big_buck_bunny_poster_big.jpg/440px-Big_buck_bunny_poster_big.jpg",
        "fanart": "https://peach.blender.org/wp-content/uploads/bbb-splash.png",
        "url": "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8",
        "backup_urls": [
            "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
        ]
    },
    {
        "id": "open_stranger_welles",
        "title": "El Extraño (The Stranger - Orson Welles)",
        "genre": "Drama / Suspenso Latino",
        "language": "Open Source HD",
        "year": "1946",
        "rating": "7.4",
        "archive_id": "the_stranger",
        "plot": "Dirigida y protagonizada por Orson Welles y Edward G. Robinson. Un investigador de crímenes de guerra rastrea a un alto jerarca fugitivo camuflado como un apacible profesor universitario.",
        "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/The_Stranger_1946_poster.jpg/440px-The_Stranger_1946_poster.jpg",
        "fanart": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=1280",
        "url": "https://archive.org/download/the_stranger/the_stranger.mp4",
        "backup_urls": ["archive://the_stranger"]
    },
    {
        "id": "open_general_buster",
        "title": "El Maquinista de la General (Buster Keaton)",
        "genre": "Comedia / Humor Latino",
        "language": "Open Source HD",
        "year": "1926",
        "rating": "8.1",
        "archive_id": "TheGeneral1926_BusterKeaton",
        "plot": "Considerada una de las cumbres del cine mundial. Un maquinista arriesga su vida en una locomotora a toda velocidad para rescatar su tren y al amor de su vida.",
        "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/The_General_%281926_film%29_poster.jpg/440px-The_General_%281926_film%29_poster.jpg",
        "fanart": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=1280",
        "url": "https://archive.org/download/TheGeneral1926_BusterKeaton/TheGeneral1926.mp4",
        "backup_urls": ["archive://TheGeneral1926_BusterKeaton"]
    }
]

# Categorías en Vivo para consultar directamente la API de Internet Archive en Español Latino y Alta Definición
ARCHIVE_LIVE_CATEGORIES = [
    {
        "id": "latino_1080p_hd",
        "name": "🔥 Películas Full HD (1080p & 720p) en Español Latino",
        "query": 'mediatype:(movies) AND format:(MPEG4 OR Matroska) AND ("1080p" OR "720p") AND ("espanol latino" OR "audio latino" OR "doblaje latino" OR "latino") AND item_size:[150000000 TO 18000000000]'
    },
    {
        "id": "latino_movies",
        "name": "🇲🇽 Películas en Español Latino (Doblaje Latino)",
        "query": 'mediatype:(movies) AND format:(MPEG4 OR Matroska) AND ("espanol latino" OR "audio latino" OR "doblaje latino") AND item_size:[45000000 TO 15000000000]'
    },
    {
        "id": "peliculas_completas_es",
        "name": "🎬 Películas Completas en Español (Todos los Géneros)",
        "query": 'mediatype:(movies) AND format:(MPEG4 OR Matroska) AND ("pelicula completa" AND (espanol OR latino)) AND item_size:[45000000 TO 15000000000]'
    },
    {
        "id": "cine_mexicano_oro",
        "name": "🌮 Cine Mexicano, Época de Oro y Latinoamericano",
        "query": 'mediatype:(movies) AND format:(MPEG4 OR Matroska) AND ("cine mexicano" OR "pedro infante" OR "cantinflas" OR "el santo" OR "pelicula mexicana") AND item_size:[35000000 TO 15000000000]'
    },
    {
        "id": "terror_espanol",
        "name": "👻 Cine de Terror, Suspenso y Misterio en Español",
        "query": 'mediatype:(movies) AND format:(MPEG4 OR Matroska) AND (terror OR horror OR miedo OR suspenso) AND (latino OR espanol OR doblaje) AND item_size:[45000000 TO 15000000000]'
    },
    {
        "id": "accion_scifi_es",
        "name": "💥 Acción, Ciencia Ficción y Aventura en Español HD",
        "query": 'mediatype:(movies) AND format:(MPEG4 OR Matroska) AND (accion OR aventura OR "ciencia ficcion" OR 720p OR 1080p) AND ("espanol latino" OR "audio latino") AND item_size:[45000000 TO 15000000000]'
    },
    {
        "id": "animacion_anime_latino",
        "name": "🎌 Animación, Caricaturas y Anime en Español Latino",
        "query": 'mediatype:(movies) AND format:(MPEG4 OR Matroska) AND (animacion OR anime OR dibujos OR "dragon ball" OR "latino") AND ("espanol latino" OR "doblaje latino") AND item_size:[30000000 TO 25000000000]'
    },
    {
        "id": "documentales_es",
        "name": "🌍 Documentales, Ciencia e Historia en Español",
        "query": 'mediatype:(movies) AND format:(MPEG4 OR Matroska) AND (documental OR historia OR cosmos OR naturaleza) AND (espanol OR latino) AND item_size:[30000000 TO 15000000000]'
    },
    {
        "id": "feature_films_hd",
        "name": "🏛️ Feature Films Open Source (Archivo Mundial Dominio Público)",
        "query": 'collection:(feature_films) AND mediatype:(movies) AND format:(MPEG4)'
    }
]


def get_movie_genres():
    """Retorna los géneros del catálogo curado de películas."""
    genres = sorted(list(set(m.get("genre", "Otros") for m in OPEN_MOVIES_CATALOG)))
    return genres


def get_movies_by_genre(genre_name):
    """Filtra películas del catálogo por género."""
    return [m for m in OPEN_MOVIES_CATALOG if m.get("genre") == genre_name]


def get_hd_1080p_movies():
    """Filtra únicamente las películas con calidad 1080p Full HD o 720p HD certificada."""
    return [
        m for m in OPEN_MOVIES_CATALOG
        if m.get("quality") in ("1080p Full HD", "720p HD")
        or "1080p" in m.get("title", "").lower()
        or "720p" in m.get("title", "").lower()
    ]


def get_latino_only_movies():
    """Filtra únicamente las películas y colecciones en Español Latino / Español."""
    return [m for m in OPEN_MOVIES_CATALOG if "Español" in m.get("language", "")]


def get_all_movies():
    """Retorna todas las películas curadas disponibles."""
    return OPEN_MOVIES_CATALOG


def find_movie_by_id(movie_id):
    """Busca una película por su ID o archive_id."""
    if not movie_id:
        return None
    for m in OPEN_MOVIES_CATALOG:
        if m.get("id") == movie_id or m.get("archive_id") == movie_id:
            return m
    return None


def fetch_archive_org_live(custom_query, page=1, rows=30):
    """
    Consulta en vivo la API Open Source de Internet Archive (archive.org/advancedsearch.php)
    y retorna una lista de películas listas para reproducir o explorar.
    """
    url = (
        "https://archive.org/advancedsearch.php?q="
        + urllib.parse.quote(custom_query)
        + "&fl[]=identifier,title,year,downloads,description,item_size"
        + "&sort[]=downloads+desc"
        + f"&rows={int(rows)}&page={int(page)}&output=json"
    )
    items = []
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": network_helper.DEFAULT_USER_AGENT}
        )
        with urllib.request.urlopen(req, timeout=9, context=network_helper.UNVERIFIED_SSL_CONTEXT) as r:
            data = json.loads(r.read().decode("utf-8", errors="ignore"))

        docs = data.get("response", {}).get("docs", [])
        for d in docs:
            ident = d.get("identifier")
            if not ident:
                continue
            raw_title = d.get("title") or ident
            if isinstance(raw_title, list):
                raw_title = raw_title[0]
            clean_title = str(raw_title).strip()

            raw_desc = d.get("description") or "Película alojada en servidor Open Source Internet Archive."
            if isinstance(raw_desc, list):
                raw_desc = " ".join(str(x) for x in raw_desc)
            clean_desc = str(raw_desc)[:450]

            year = str(d.get("year") or "2020")
            if not year.isdigit():
                year = "2020"

            size_mb = round(int(d.get("item_size", 0) or 0) / (1024 * 1024), 1)
            q_badge = "1080p/720p HD" if size_mb >= 600 or "1080" in clean_title.lower() or "720" in clean_title.lower() else "Español / Open Source"

            items.append({
                "id": f"ia_{ident}",
                "archive_id": ident,
                "title": clean_title,
                "genre": "Internet Archive Open Server",
                "language": q_badge,
                "year": year,
                "rating": "7.5",
                "plot": f"[Servidor Open Source: Archive.org · Tamaño total: {size_mb} MB · Descargas: {d.get('downloads', 0)}]\n\n{clean_desc}",
                "poster": f"https://archive.org/services/img/{ident}",
                "fanart": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=1280",
                "url": f"archive://{ident}",
                "backup_urls": []
            })
    except Exception:
        pass
    return items


def search_archive_org_latino(search_term, page=1, rows=30):
    """
    Busca cualquier película en vivo en los servidores de Internet Archive
    priorizando Español Latino y archivos de video reales (>35MB).
    """
    term = search_term.strip()
    if not term:
        return []
    q = f'mediatype:(movies) AND format:(MPEG4 OR Matroska) AND ({term}) AND item_size:[35000000 TO 20000000000]'
    return fetch_archive_org_live(q, page=page, rows=rows)


def search_peertube_latino(search_term, count=25):
    """
    Consulta el buscador federado Open Source SepiaSearch (PeerTube API)
    para encontrar películas y videos largos en español.
    """
    term = search_term.strip()
    if not term:
        return []
    api_url = (
        "https://sepiasearch.org/api/v1/search/videos?search="
        + urllib.parse.quote(f"{term} español")
        + f"&count={int(count)}&sort=-match"
    )
    results = []
    try:
        req = urllib.request.Request(
            api_url,
            headers={"User-Agent": network_helper.DEFAULT_USER_AGENT}
        )
        with urllib.request.urlopen(req, timeout=7, context=network_helper.UNVERIFIED_SSL_CONTEXT) as r:
            data = json.loads(r.read().decode("utf-8", errors="ignore"))

        for v in data.get("data", []):
            uuid = v.get("uuid") or v.get("shortUUID")
            host = v.get("account", {}).get("host") or v.get("channel", {}).get("host")
            if not uuid or not host:
                continue
            title = v.get("name", "Video PeerTube")
            desc = v.get("description") or "Servidor Federado Open Source PeerTube"
            thumb = v.get("thumbnailUrl") or v.get("previewUrl") or ""
            duration_min = int(v.get("duration", 0) or 0) // 60

            results.append({
                "id": f"pt_{uuid}",
                "title": f"{title} [COLOR gray]({duration_min} min)[/COLOR]",
                "genre": f"PeerTube ({host})",
                "language": "Español / PeerTube HD",
                "year": "2024",
                "rating": "7.2",
                "plot": f"[Servidor Federado PeerTube: {host}]\nDuración: {duration_min} min\n\n{desc[:400]}",
                "poster": thumb,
                "fanart": thumb or "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=1280",
                "url": f"peertube://{host}/{uuid}",
                "backup_urls": [v.get("url", "")]
            })
    except Exception:
        pass
    return results
