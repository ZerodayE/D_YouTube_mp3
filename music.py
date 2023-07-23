import os
import youtube_dl
import shutil

def descargar_mp3(url, destino):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        archivo_mp3 = ydl.prepare_filename(info)
        ydl.download([url])

    # Mover el archivo MP3 a la ubicación deseada
    shutil.move(archivo_mp3, destino)

if __name__ == "__main__":
    url = input("Ingrese la URL del video de YouTube: ")
    destino = input("Ingrese la ruta completa de destino para guardar el archivo MP3: ")
    descargar_mp3(url, destino)

