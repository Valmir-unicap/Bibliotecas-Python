# pip install youtube-dl

# !apt-get update && apt-get install ffmpeg -y

import yt_dlp as youtube_dl
import shutil

# Check if FFmpeg is installed and get its path
ffmpeg_path = shutil.which('ffmpeg')  

# If FFmpeg is found, update ydl_opts
if ffmpeg_path:
    # Configuração do yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': ffmpeg_path,  # Use the detected FFmpeg path
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Changed key to 'FFmpegExtractAudio'
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    url = 'https://youtube.com/clip/UgkxjDmTChpZHdKbZLp2CY91cuU1Q6HDMDRr?si=L_Ad799SS023nRH-'  # Substitua pelo seu URL

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
else:
    print("FFmpeg not found. Please install FFmpeg.")
