import youtube_dl
import ffmpeg
import html

# insert test link here!
link = 'https://www.youtube.com/watch?v=2A3iZGQd0G4'
ydl = youtube_dl.YoutubeDL({'outtmpl': 'tmp/tmp'})
with ydl:
  result = ydl.extract_info(
    link,
    download=True
  )
  if 'entries' in result:
    title = result['entries'][0]['title']
  else:
    title = result['title']

  (
    ffmpeg
    .input("./tmp/tmp.mkv")
    .audio
    .output('out/' + html.unescape(title) + ".mp3")
    .run_async()
    .wait()
  )

