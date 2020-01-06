import argparse
from colors import rgb, hex
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(
    prog='RgbToHex.py',
    description='convert rgb values to hexadecimal values',
    epilog='related programs: HexToRgb.py',
    formatter_class=RawTextHelpFormatter
)

parser.add_argument(
    'red',
    help='red color value (3 digit number [0-255])',
    type=int
)

parser.add_argument(
    'green',
    help='green color value (3 digit number [0-255])',
    type=int
)

parser.add_argument(
    'blue',
    help='blue color value (3 digit number [0-255])',
    type=int
)

args = parser.parse_args()

red = args.red
green = args.green
blue = args.blue

rgb_color = str(rgb(red, green, blue))
hex_color = str(rgb(red, green, blue).hex).upper()

print('\n' + 'rgb value:', '\n rgb(' + rgb_color + ')\n')
print('hex value:', '\n #' + hex_color, '\n')
