from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter

inx = str(input("Hey! What is the path of the file you would like to use?\nJPG or PNG only! (eg: Users\\you\\image.png) ")).replace('\\', '/')

image = Image.open(inx)

converter = ImageEnhance.Color(image)
img2 = converter.enhance(2.5)

for i in range(int(input("How many times would you like the sharpen filter applied? ")) + 1):
    img2 = img2.filter(ImageFilter.SHARPEN)

img2 = ImageEnhance.Contrast(img2).enhance(2.5)

img2.save(f"{input('Output file name? ')}.{inx[-3::]}")
