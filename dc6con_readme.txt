Readme for DC6CON Version 1.0 8/31/00

This is a utility for converting the .dc6 images in the Diablo II data files
to and from pcx format.  Most .dc6 files can be found in the d2data.mpq, to get
at them, you'll need an mpq extraction utility.  I personally recommend mpq2k.  

usage: dc6con <filename>

Optional Parameters
-transcol <value>       Specifies transparent color for dc6/pcx creation
-pal <palette file>     Specify Palette for pcx creation
-?         This help message

If the specified file has .dc6 extension, dc6con will create a pcx with the
same filename, otherwise, it will attempt to convert the specified file to dc6.

Dc6con can extract transparent and animated dc6 files, but cannot yet create
animated dc6s.  When creating a transparent dc6 image (item files) it is
necessary to specify the transparent color of the image.  This is typically
0.  You can also specify transcol for the background when extracting a
transparent dc6 (for better contrast).

Normally, the image is generated with dc6con's own internal palette, this is
typically good for most images. Some images, however, use special palettes.
These palettes are 768 byte files with the extension of .dat in the Diablo
II mpq. To use a different palette, use the -pal parameter. An example
commandline might look like:

dc6con creditsbckg.dc6 -pal pal.dat -transcol 0

This program is copyright (c)2000 by Ryan Smith and Forest Hale and is
distributed under the GNU General Public License (Version 2).  The source
to this program is included with this archive.  Please see the gnu.txt
for further details.

For questions or comments (or heaven forbid, bug reports) please e-mail kryten@adelphia.net

