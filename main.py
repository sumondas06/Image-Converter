import sys
import os
from PIL import Image

input_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    img = Image.open(f'{input_folder}/{filename}')
    img.thumbnail((200, 300))
    clean_name = os.path.splitext(filename)[0]
    if not os.path.exists(f'{output_folder}/{clean_name}.png'):
        img.save(f'{output_folder}/{clean_name}.png', 'png')
    else:
        print('exists')
