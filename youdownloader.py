from pytube import YouTube

def download_video(link):
  video = YouTube(link)
  title = video.title
  video.streams.get_highest_resolution().download("./media/video", f"{title}.mp4")

def download_song(link):
  song = YouTube(link)
  title = song.title
  song.streams.get_audio_only().download("./media/audio", f"{title}.mp3")

def choose_option(link):
  print("""Selecciona una opción:
  1 - Audio
  2 - Video
  3 - Salir""")
  
  option = input()

  if option == "1":
    print("Descargando audio...")
    download_song(link)
    print("Listo!")
  elif option == "2":
    print("Descargando video...")
    download_video(link)
    print("Listo!")
  elif option == "3":
    print("Saliendo...")
    return
  else:
    print("Elija una opción correcta.")
    return choose_option(link)

def main():
  # Obtener link
  print("Pega el link del video")

  link = input()

  # Elegir opción
  choose_option(link)

if __name__ == "__main__":
  main()