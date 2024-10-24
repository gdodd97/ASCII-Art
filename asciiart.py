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

    rgb_array = np.zeros((height, width, 3), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            rgb_array[y,x] = image.getpixel((x,y))
    return rgb_array

pixel_matrix = tuple_to_array(im)

print("Iterating through RGB Values")
#for x in len(pixel_matrix):
#    for y in len(pixel_matrix[x]):
#        pixel = pixel_matrix[x][y]
#        print(pixel)
for row in pixel_matrix:
    for element in row:
        print(element)