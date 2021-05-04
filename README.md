## dc6 to png enhance

### Requirements
- python https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe  (check the 'add to path' box when installing)

- dc6con.exe from the phrozen keep http://phrozenkeep.blob.core.windows.net/public/files/tools/image/dc6con.zip. dc6con is included in this github repo

- imagemagick for windows (linux, mac works too)  https://download.imagemagick.org/ImageMagick/download/binaries/ImageMagick-7.0.11-10-Q16-HDRI-x64-dll.exe (check the 'convert legacy' feature box when installing)


### Usage
Open a terminal (shift + right click in your folder and select 'Open Powershell window here') then run `python dc6_png_enhance.py`

`python dc6_png_enhance.py` takes `*.dc6` files in `./dc6/` and makes 4x ai upsampled pngs in `./png-hd/`
(If there is an error about the python requests package, then in a CMD/powershell window do `pip install requests`)

Up sampling / super resolution is done with https://deepai.org/ 's [API](https://deepai.org/machine-learning-model/torch-srgan)

The output upsampled `.png` feeds right into [SpriteEdit](https://github.com/eezstreet/D2RModding-SpriteEdit/tree/master/D2RModding-SpriteEdit) and when converted to a `.sprite` can go into the D2R data folder `data/hd/global/ui/items, panels, etc`


### Other Ideas
Image upsampling can be done with shaders from libretro, and other upsampling algorithms

for example https://docs.libretro.com/shader/scalefx/ ,and  xbrz is popular https://docs.libretro.com/shader/xbrz/


### Image Comparisons

LoD:  jewel
LoD enhanced:  jewel

D2R: jewel

kinem awl sword


### Credits and Tools
- https://github.com/eezstreet/D2RModding-SpriteEdit/tree/master/D2RModding-SpriteEdit
- https://d2mods.info/forum/downloadsystemcat?id=14&sid=c82d745c9dfee8c09369f78120475a39
- https://github.com/dschu012/dc6png
