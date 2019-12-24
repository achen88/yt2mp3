from pytube import YouTube
from tqdm import tqdm
import ffmpeg
import html

def download(link, dest):
  pbar = tqdm()
  yt = YouTube(link)
  video = yt.streams.filter().first()

  pbar.reset(total=video.filesize)

  def progress_fn(self, chunk, *_):
    pbar.update(len(chunk))

  yt.register_on_progress_callback(progress_fn)

  video = yt.streams.filter().first()
  video.download(output_path="./tmp", filename="tmp")

  return (
    ffmpeg
    .input("./tmp/tmp.mp4")
    .audio
    .output(dest + html.unescape(video.title) + ".mp3")
    .run_async()
    .wait()
  )

