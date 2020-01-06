from sys import argv
from colors import rgb, hex

script, red, green, blue = argv

red = int(red)
green = int(green)
blue = int(blue)

rgb_color = str(rgb(red, green, blue))
hex_color = str(rgb(red, green, blue).hex).upper()

print('\n' + 'RGB Value: rgb(' + rgb_color + ')')
print('Hex Value: #' + hex_color + '\n')
