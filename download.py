import youtube_dl
import ffmpeg
import html

def download(link, dest):
  ydl = youtube_dl.YoutubeDL({'outtmpl': 'tmp/tmp.%(ext)s', 'merge_output_format': 'mkv'})
  title = None
  with ydl:
    result = ydl.extract_info(
      link,
      download=True
    )
    if 'entries' in result:
      title = result['entries'][0]['title']
    else:
      title = result['title']

    return (
      ffmpeg
      .input("./tmp/tmp.mkv")
      .audio
      .output(dest + html.unescape(title) + ".mp3")
      .run_async()
      .wait()
    )

