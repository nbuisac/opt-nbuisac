# https://github.com/yt-dlp/yt-dlp
from yt_dlp import YoutubeDL
link="https://www.youtube.com/watch?v=pdgFqPbw64g"  # Qué es el ESP32 y porque deberías tener esta placa
URLS = [link]

with YoutubeDL() as ydl:
    ydl.download(URLS)

# Altres opcions

import json
with YoutubeDL() as ydl:
    info = ydl.extract_info(link, download=False)
    print(json.dumps(ydl.sanitize_info(info)))