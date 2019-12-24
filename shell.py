import sys
from download import download
import argparse
import os

def valid_dir(path): 
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError('{} is not an existing directory'.format(path))
    if not path.endswith(os.sep): path += os.sep
    return path

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='specify a file to read from')
parser.add_argument('-d', '--dest', default='./out/', type=valid_dir, help='specify a destination, defaults to ./out/')
args = parser.parse_args()

print()

fd = sys.stdin
if args.file:
  print("Reading from file...")
  fd = open(args.file, 'r')
else:
  print("Enter a youtube link and press enter, mp3s go to " + args.dest)
  print("This shell can also batch download from a list")
  print("  Control+C exits")
print("\n> ", end="", flush=True)

try:
  buff = ''
  while True:
    chunk = fd.read(1)
    buff += chunk
    if buff.endswith('\n'):
      download(buff[:-1], args.dest)
      buff = ''
      print("\n> ", end="")
      sys.stdout.flush()
    if not chunk:
      break
except KeyboardInterrupt:
  sys.stdout.flush()
  pass

