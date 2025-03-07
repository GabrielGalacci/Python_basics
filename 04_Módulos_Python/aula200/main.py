# Pillow: redimentionando imagens com Python
# Essa biblioteca é o Photoshop do Python

from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.JPG'
NEW_IMAGE = ROOT_FOLDER / 'new.JPG'

pil_image = Image.open(ORIGINAL)
width, height = pil_image.size
print('WIDTH: ', width)
print('HEIGHT: ', height)
exif = pil_image.info['exif']
# print(exif)

# width -> new_width
# height -> new_height
new_width = 640
new_height = round(height * new_width / width)
print('NEW WIDTH', new_width, 'NEW HEIGHT', new_height)

new_image = pil_image.resize(size=(new_width, new_height))

new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=80,
    exif=exif,
)
