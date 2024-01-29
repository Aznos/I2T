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
        (128, 128, 128): Fore.LIGHTBLACK_EX,
        (0, 0, 255): Fore.LIGHTBLUE_EX,
        (0, 255, 0): Fore.LIGHTGREEN_EX,
        (0, 255, 255): Fore.LIGHTCYAN_EX,
        (255, 0, 0): Fore.LIGHTRED_EX,
        (255, 0, 255): Fore.LIGHTMAGENTA_EX,
        (255, 255, 0): Fore.LIGHTYELLOW_EX,
        (255, 255, 255): Fore.LIGHTWHITE_EX,
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
        
def loadAndResize(imagePath, newWidth=100):
    with Image.open(imagePath) as img:
        aspectRatio = img.height / img.width
        newHeight = int(aspectRatio * newWidth)
        resizedImg = img.resize((newWidth, newHeight))
        return resizedImg
    
imagePath = "test.jpg"
resizedImage = loadAndResize(imagePath)
printImage(resizedImage)