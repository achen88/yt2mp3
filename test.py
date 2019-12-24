from pytube import YouTube
from tqdm import tqdm
import ffmpeg
import html

# insert test link here!
yt = YouTube('https://www.youtube.com/watch?v=2A3iZGQd0G4')
audio = yt.streams.filter().first()

pbar = tqdm(total=audio.filesize)

def progress_fn(self, chunk, *_):
  pbar.update(len(chunk))

yt.register_on_progress_callback(progress_fn)

audio = yt.streams.filter().first()
audio.download(output_path="./tmp", filename="tmp")

(
  ffmpeg
  .input("./tmp/tmp.mp4")
  .audio
  .output('./out/' + html.unescape(audio.title) + ".mp3")
  .run_async()
  .wait()
)

