# bootlegport 🎧 🎛
it's like crappy beatport

## Dependencies
- make >= 3.82
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
|Delete garbage|`make clean`|

Mp3s go to `./out`

## Demo
### `make shell`
![Example 1](https://raw.githubusercontent.com/achen88/bootlegport/master/images/ex1.gif)
### `make shell LIST=[filename]`
![Example 2](https://raw.githubusercontent.com/achen88/bootlegport/master/images/ex2.gif)
