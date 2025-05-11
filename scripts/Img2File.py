import os
import sys
from PIL import Image


def image_to_file(input_image_path, output_file_path):
    try:
        img = Image.open(input_image_path)
        pixels = list(img.getdata())

        byte_array = bytearray()
        for pixel in pixels:
            byte_array.extend(pixel[:3])  # Only R, G, B
        output_text = byte_array.decode().replace("\x00","").replace("\r","")

        with open(output_file_path, "w") as f:
            f.write(output_text)

        return output_file_path
    except Exception as e:
        return str(e)

def select_image(file):
    image_path = file
    if image_path:
        output_path = os.path.splitext(image_path)[0] + "_recovered"
        result = image_to_file(image_path, output_path)
        if os.path.exists(result):
            print(f"Success - File recovered and saved to: {result}")
        else:
            print(f"Error - Failed to recover file: {result}")

try:
    select_image(sys.argv[1])
except Exception as e:
    print(e)
