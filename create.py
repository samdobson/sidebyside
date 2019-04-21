import os
import sys
from PIL import Image, ImageFont, ImageDraw

# Change this
DIR = r'C:\Users\Sam\Documents\Photos'
OUTPUT_FILENAME = 'side-by-side.png'

# Also change these if you need to
MAX_SIZE = (800, 800)
SUPPORTED_FILETYPES = ['jpg', 'png']
TEXT_COLOUR = (255,255,255)

# Main code starts here
files = [x for x in os.listdir(DIR) if x[-3:].lower() in SUPPORTED_FILETYPES]
image_pairs = list(zip(files, files[1:]))[::2]

for i, x in enumerate(image_pairs):
    imgs = [Image.open(os.path.join(DIR, image)) for image in x]
    widths, heights = zip(*(img.size for img in imgs))
    
    for im in imgs:
        im = im.thumbnail(MAX_SIZE, Image.ANTIALIAS)

    widths, heights = zip(*(img.size for img in imgs))
    new_im = Image.new('RGB', (sum(widths), max(heights)))

    x_offset = 0
    for im in imgs:
      new_im.paste(im, (x_offset, 0))
      x_offset += im.size[0]

    fnt = ImageFont.truetype('arial.ttf', 36, encoding='unic')
    d = ImageDraw.Draw(new_im)
    d.text((5,5), x[0].split('_')[1][:-4], font=fnt, fill=TEXT_COLOUR)
    d.text((MAX_SIZE[0] + 5, 5), x[1].split('_')[1][:-4], font=fnt, fill=TEXT_COLOUR)

    new_im.save(os.path.join(DIR, OUTPUT_FILENAME.replace('.png', str(i) + '.png')))
