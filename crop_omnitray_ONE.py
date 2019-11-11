import numpy as np
from PIL import Image, ImageDraw, ImageOps
import sys

# Open the input image as numpy array, convert to RGB
photo0 = sys.argv[1]
print(photo0 + ".png")
plate0 = Image.open(photo0 + ".png")
img = Image.open(photo0 + ".png").convert("RGB")

# cut the photo
area = (230, 200, 207, 200)  # left, up, right, bottom
plate0 = ImageOps.crop(plate0, area)
plate0.save(photo0 + "_crop.png")

