from PIL import Image
import ffmpeg

def decode_text_from_image(image_path):
    image = Image.open(image_path)
    binary_text = ""
    width, height = image.size

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            for n in range(3):
                binary_text += str(pixel[n] & 1)

    all_bytes = [binary_text[i: i+8] for i in range(0, len(binary_text), 8)]

    decoded_text = ""
    found_message = False  
    for byte in all_bytes:
        decoded_text += chr(int(byte, 2))
        if decoded_text[-5:] == "#####":
            found_message = True
            break

    return decoded_text[:-5], found_message  
