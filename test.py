from pytube import YouTube
from tqdm import tqdm

yt = YouTube('https://www.youtube.com/watch?v=TADQbywYNmU')
audio = yt.streams.filter(only_audio=False).first()

pbar = tqdm(total=audio.filesize)

def progress_fn(self, chunk, *_):
  pbar.update(len(chunk))

yt.register_on_progress_callback(progress_fn)

audio = yt.streams.filter(only_audio=False).first()
audio.download()
