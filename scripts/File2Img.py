from PIL import Image
import math
import os
import sys

def file_to_image(input_file_path, output_image_path):
    try:
        with open(input_file_path, "rb") as f:
            byte_data = f.read()

        pixels = []
        for i in range(0, len(byte_data), 3):
            chunk = byte_data[i:i+3]
            if len(chunk) < 3:
                chunk += b'\x00' * (3 - len(chunk))
            pixels.append(tuple(chunk))

        width = math.ceil(math.sqrt(len(pixels)))
        height = math.ceil(len(pixels) / width)
        pixels += [(0, 0, 0)] * (width * height - len(pixels))

        img = Image.new("RGB", (width, height))
        img.putdata(pixels)
        img.save(output_image_path)
        return output_image_path

    except Exception as e:
        return str(e)

def select_file(file):
    file_path = file
    
    if file_path:
        output_path = os.path.splitext(file_path)[0] + ".png"
        result = file_to_image(file_path, output_path)
        if os.path.exists(result):
            print("Success", f"Image saved to:\n{result}")
        else:
            print("Error", f"Failed to create image:\n{result}")

try:
    select_file(sys.argv[1])
except Exception as e:
    print(e)
