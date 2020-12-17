import numpy as np
from PIL import Image, ImageDraw, ImageOps
import sys
import os

# Create the new directory "Processed"
if not os.path.exists("Processed_crop"):
	os.mkdir("Processed_crop")
if not os.path.exists("Processed_mask"):
	os.mkdir("Processed_mask")

# Open the input image as numpy array, convert to RGB
photo0 = sys.argv[1]
print(photo0 + ".png")
plate0 = Image.open(photo0 + ".png")
img = Image.open(photo0 + ".png").convert("RGB")

# cut the photo
area = (345, 170, 331, 176)  # left, up, right, bottom
plate0 = ImageOps.crop(plate0, area)
plate0.save("Processed_crop/" + photo0 + "_crop.png")

# Mask the photo
npImage = np.array(img)
h, w = img.size
#print(img.size)

# Create same size alpha layer with circle
alpha = Image.new('L', img.size,0)
draw = ImageDraw.Draw(alpha)
draw.pieslice([350, 171, h-331, w-182], 00, 360, fill=255) # left, up, right, bottom

# Convert alpha Image to numpy array
npAlpha = np.array(alpha)

# Add alpha layer to RGB
npImage = np.dstack((npImage,npAlpha))

# Save with alpha
#Image.fromarray(npImage).save("Processed_mask/" + photo0 + "_crop_mask.png")

# Crop the masked image
plate_mask = Image.open("Processed_mask/" + photo0 + "_crop_mask.png")
cut_mask = ImageOps.crop(plate_mask, area).save("Processed_mask/" + photo0 + "_crop_mask.png")