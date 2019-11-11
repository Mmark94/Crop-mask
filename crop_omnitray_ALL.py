import numpy as np
from PIL import Image, ImageDraw, ImageOps
import glob

# Open the input image as numpy array, convert to RGB
for filename in glob.glob("*.png"):
    photo0=filename.replace(".png","")
    print(photo0)
    plate0 = Image.open(photo0 + ".png")
    img = Image.open(photo0 + ".png").convert("RGB")

    # cut the photo
    area = (230, 200, 207, 200)  # left, up, right, bottom
    plate0 = ImageOps.crop(plate0, area)
    plate0.save(photo0 + "_crop.png")

