from pytube import YouTube
from pytube.cli import on_progress
import tkinter as tk
from tkinter import *
from tkinter import ttk

def download_video(link):
  video = YouTube(link, on_progress_callback=on_progress)
  title = video.title
  video.streams.get_highest_resolution().download("./media/video", f"{title}.mp4")

def download_song(link):
  song = YouTube(link, on_progress_callback=on_progress)
  title = song.title
  song.streams.get_audio_only().download("./media/audio", f"{title}.mp3")

def main():
  root = Tk()
  root.title("YouDownloader")
  root.geometry("600x500")
  root.resizable(FALSE, FALSE)

  input_frame = Frame(root)
  input_frame.pack(pady=30)

  url_label = Label(input_frame, text="URL del video:")
  url_label.pack(side="left", padx=7)

  input = ttk.Entry(input_frame, width=45)
  input.pack(side="left")

  buttons_frame = Frame(root)
  buttons_frame.pack(pady=10)

  download_audio_btn = tk.Button(buttons_frame, text="Descargar audio", command=download_song)
  download_audio_btn.pack(side="left", padx=20)

  download_video_btn = tk.Button(buttons_frame, text="Descargar video", command=download_video)
  download_video_btn.pack(side="left", padx=20)

  root.mainloop()

if __name__ == "__main__":
  main()