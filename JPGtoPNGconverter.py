import sys
import os
from PIL import Image

# Grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]


# print(image_folder, output_folder)


# Check if new folder exists or not
if not os.path.exists(output_folder):
	os.makedirs(output_folder)


# Convert Loop
for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	clean_name = os.path.splitext(filename)[0]
	img.save(f'{output_folder}{clean_name}.png','png')
	print('Converted !')