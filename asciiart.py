from PIL import Image
import numpy as np
im = Image.open("cat.jpg")

r,g,b = im.getpixel((0,0))

width = im.size[0]
height = im.size[1]
print("Successfully loaded image!")
print("Image size:",width, "x",height)

def tuple_to_array(image):
    image = image.convert('RGB')

    width, height = image.size

    rgb_array = np.zeros((height, width, 3), dtype=np.uint64)

    for y in range(height):
        for x in range(width):
            rgb_array[y,x] = image.getpixel((x,y))
    return rgb_array

def array_to_brightness(image):
    image = image.convert('RGB')
    width, height = image.size
    pixel_matrix = tuple_to_array(image)
    
    brightness_matrix = np.zeros((height, width, 1), dtype=np.uint64)

    for y in range(height):
        for x in range(width):
            brightness_matrix[y,x] = round(np.sum(pixel_matrix[y,x])/3)

    return brightness_matrix

pixel_matrix = tuple_to_array(im)
brightness_matrix = array_to_brightness(im)

print("Iterating through Brightness")
print(brightness_matrix)