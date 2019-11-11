import numpy as np
from PIL import Image, ImageDraw, ImageOps
import sys

# Open the input image as numpy array, convert to RGB
photo0 = sys.argv[1]
print(photo0 + ".png")
plate0 = Image.open(photo0 + ".png")
img = Image.open(photo0 + ".png").convert("RGB")

# cut the photo
area = (207, 25, 207, 32)  # left, up, right, bottom
plate0 = ImageOps.crop(plate0, area)
plate0.save(photo0 + "_crop.png")

# Mask the photo
npImage = np.array(img)
h, w = img.size
#print(img.size)

# Create same size alpha layer with circle
alpha = Image.new('L', img.size,0)
draw = ImageDraw.Draw(alpha)
draw.pieslice([210, 25, h-210, w-35], 00, 360, fill=255)

# Convert alpha Image to numpy array
npAlpha = np.array(alpha)

# Add alpha layer to RGB
npImage = np.dstack((npImage,npAlpha))

# Save with alpha
Image.fromarray(npImage).save(photo0 + "_crop_mask.png")

# Crop the masked image
plate_mask = Image.open(photo0 + "_crop_mask.png")
cut_mask = ImageOps.crop(plate_mask, area).save(photo0 + "_crop_mask.png")