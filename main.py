from PIL import Image
from colorama import Fore, Back, Style, init
import math

init(autoreset=True)

def closestColor(rgb):
    colors = {
        (0, 0, 0): Fore.BLACK,
        (0, 0, 128): Fore.BLUE,
        (0, 128, 0): Fore.GREEN,
        (0, 128, 128): Fore.CYAN,
        (128, 0, 0): Fore.RED,
        (128, 0, 128): Fore.MAGENTA,
        (128, 128, 0): Fore.YELLOW,
        (192, 192, 192): Fore.WHITE,
    }
    
    r, g, b = rgb
    closestcolors = min(colors.keys(), key=lambda color: math.sqrt((color[0] - r) ** 2 + (color[1] - g) ** 2 + (color[2] - b) ** 2))
    return colors[closestcolors]

def printImage(image):
    for y in range(image.height):
        for x in range(image.width):
            rgb = image.getpixel((x, y))
            color = closestColor(rgb)
            print(color + "██", end="")
        print()