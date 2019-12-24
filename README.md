# yt2mp3 🎧 🎛
it's yet another Youtube -> mp3 converter

## Dependencies
- make >= 3.82 (optional)
- python3
- ffmpeg

## Instructions
||Command|
|---|---|
|Help|`make`|
|Install python dependencies|`make install`| 
|Run test script|`make test`|
|Run interactive downloader|`make shell`|
|Run downloader on list of urls|`make shell LIST=[filename]`|
|Specify target directory|`make shell DEST=[directory]`|
|Delete garbage|`make clean`|

### `make`-less
||Command|
|---|---|
|Install python dependencies|`pip3 install -r requirements.txt`| 
|Run test script|`python3 test.py`|
|Run interactive downloader|`python3 shell.py`|
|Run downloader on list of urls|`python3 shell.py -f [filename]`|
|Specify target directory|`python3 shell.py -d [directory]`|

Replace `pip3` and `python3` as necessary. Target directory defaults to `./out/`.

## Demo
### `make shell`
![Example 1](https://raw.githubusercontent.com/achen88/yt2mp3/master/images/ex1.gif)
### `make shell LIST=[filename]`
![Example 2](https://raw.githubusercontent.com/achen88/yt2mp3/master/images/ex2.gif)
