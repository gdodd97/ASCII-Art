from PIL import Image
im = Image.open("cat.jpg")

r,g,b = im.getpixel((0,0))

width = im.size[0]
height = im.size[1]
print("Successfully loaded image!")
print("Image size:",width, "x",height)
print("RGB Values in pixel 1:",r, g, b)

#todo add rgb values for all pixels into 2D array