from PIL import Image
import numpy as np
im = Image.open("cat.jpg")

ascii = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

r,g,b = im.getpixel((0,0))

width = im.size[0]
height = im.size[1]
print("Successfully loaded image!")
print("Image size:",width, "x",height)

def get_pixel_matrix(im, height):
    im.thumbnail((height, 200))
    pixels = list(im.getdata())
    return [pixels[i:i+im.width] for i in range(0, len(pixels), im.width)]



def array_to_brightness(pixel_matrix):
    brightness_matrix = []
    for row in pixel_matrix:
        brightness_row = []
        for pixel in row:
            brightness = round(pixel[0] + pixel[1] + pixel[2] / 3.0)
            brightness_row.append(brightness)
        brightness_matrix.append(brightness_row)
    
    return brightness_matrix

def normalize_brightness_matrix(brightness_matrix):
    normal_brightness_array = []
    max_pixel = max(map(max, brightness_matrix))
    min_pixel = min(map(min, brightness_matrix))
    for row in brightness_matrix:
        rescaled_row = []
        for p in row:
            r = 255 * (p - min_pixel) / float(max_pixel - min_pixel)
            rescaled_row.append(r)
        normal_brightness_array.append(rescaled_row)

    return normal_brightness_array

def brightness_to_ascii(brightness_matrix, ascii):

    ascii_matrix = []
    for row in brightness_matrix:
        ascii_row = []
        for pixel in row:
            ascii_row.append(ascii[int(pixel/255 * len(ascii)) - 1])
        ascii_matrix.append(ascii_row)

    return ascii_matrix

def print_ascii_matrix(ascii_matrix):
    for row in ascii_matrix:
        line = [p+p+p for p in row]
        print(line)

pixels = get_pixel_matrix(im,1000)
brightness_matrix = array_to_brightness(pixels)
brightness_matrix = normalize_brightness_matrix(brightness_matrix)
ascii_matrix = brightness_to_ascii(brightness_matrix, ascii)

print_ascii_matrix(ascii_matrix)
