# RgbToHex
## Description
A simple python program for converting rgb color values to hexadecimal color values.

## Usage
Basic Usage:
```PowerShell
RgbToHex.py [-h] red green blue
```

Example:
*convert rgb value rgb(12, 56, 99) to hex format.*
```PowerShell
PS> RgbToHex.py 12 56 99

rgb value:
 rgb(12, 56, 99)

hex value:
 #0C3863
```

To view the the help menu, use the ```-h or --help``` argument:
```PowerShell
PS> RgbToHex.py -h
usage: RgbToHex.py [-h] red green blue

convert rgb values to hexadecimal values

positional arguments:
  red         red color value (3 digit number [0-255])
  green       green color value (3 digit number [0-255])
  blue        blue color value (3 digit number [0-255])

optional arguments:
  -h, --help  show this help message and exit

related programs: HexToRgb.py
```
