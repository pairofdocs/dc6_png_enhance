## dc6 to png Enhance
A tool to convert from .dc6 (D2 images) to upsampled .png images

### Requirements
- python https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe  (check the 'add to path' box when installing)

- dc6con.exe from the phrozen keep http://phrozenkeep.blob.core.windows.net/public/files/tools/image/dc6con.zip. dc6con is included in this github repo

- imagemagick for windows (linux, mac works too) [7.1.0 from here](https://download.imagemagick.org/ImageMagick/download/binaries/ImageMagick-7.1.0-0-Q16-HDRI-x64-dll.exe) or the newest release [here](https://imagemagick.org/script/download.php#windows) (check the 'convert legacy' feature box when installing)


### Usage
[Download the files from this repository](https://github.com/pairofdocs/dc6_png_enhance/archive/refs/heads/master.zip) and unzip

Open a terminal (shift + right click in your folder and select 'Open Powershell window here') then run `python dc6_png_enhance.py`

`python dc6_png_enhance.py` takes `*.dc6` files in `./dc6/` and makes 4x ai upsampled pngs in `./png-hd/`
(If there is an error about the python requests package, then in a CMD/powershell window do `pip install requests`)

Up sampling / super resolution is done with https://deepai.org/ 's [API](https://deepai.org/machine-learning-model/torch-srgan)

The output upsampled `.png` feeds right into [SpriteEdit](https://github.com/eezstreet/D2RModding-SpriteEdit/tree/master/D2RModding-SpriteEdit) and when converted to a `.sprite` can go into the D2R data folder `data/hd/global/ui/items, panels, etc`


### Note: Trial API Key
`dc6_png_enhance.py` uses a trial API key from https://deepai.org.  
If you need to convert more than 10 dc6 images then sign up to get an API key for free with https://deepai.org/.  
Then enter your API key on [line 15 of dc6_png_enhance.py](https://github.com/pairofdocs/dc6_png_enhance/blob/master/dc6_png_enhance.py#L15) after `"api-key":"`.


### Other Ideas
Image upsampling can be done with shaders from libretro, and other upsampling algorithms

for example https://docs.libretro.com/shader/scalefx/ ,and  xbrz is popular https://docs.libretro.com/shader/xbrz/


### Image Comparisons

Jewel: LoD, LoD enhanced, and D2R
- ![LoD orig](https://i.imgur.com/sZZYJG0.png)

- ![LoD enhanced](https://i.imgur.com/TPtO6YU.jpg)

- ![d2r](https://i.imgur.com/w07qn8D.png)

Kinemil's Awl sword: LoD, LoD enhanced, and D2R
- ![LoD orig](./dc6/invgisu.png)

- ![LoD enhanced](./png-hd/invgisu-hd.png)

- ![d2r](https://i.imgur.com/yRicRuy.png)


### Credits and Tools
- https://github.com/eezstreet/D2RModding-SpriteEdit/tree/master/D2RModding-SpriteEdit
- https://d2mods.info/forum/downloadsystemcat?id=14&sid=c82d745c9dfee8c09369f78120475a39
- https://github.com/dschu012/dc6png
- https://imagemagick.org/index.php
