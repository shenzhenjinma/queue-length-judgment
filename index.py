# -*- coding: utf-8 -*-
from PIL import Image, ImageEnhance
import requests
# url = "http://127.0.0.1/esp32_camera/online.jpg"
# response = requests.get(url)
# with open("image-2.jpg", "wb") as f:
#     f.write(response.content)
noticeval=5000
noticeurl= "https://api.day.app/my_brak_token/现在人少赶紧做核酸"
imgbrightess=200
imgcontrast=3
im1 = Image.open("image-0.jpg")
im2 = Image.open("image-2.jpg")

enhancer = ImageEnhance.Contrast(im1)
im1 = enhancer.enhance(imgcontrast)
im1.save("im1-1.jpg")

im1 = im1.convert("L")
im1.save("im1-2.jpg")

enhancer = ImageEnhance.Brightness(im1)
im1 = enhancer.enhance(imgbrightess)
im1.save("im1-3.jpg")

enhancer = ImageEnhance.Contrast(im2)
im2 = enhancer.enhance(imgcontrast)
im2.save("im2-1.jpg")

im2 = im2.convert("L")
im2.save("im2-2.jpg")

enhancer = ImageEnhance.Brightness(im2)
im2 = enhancer.enhance(imgbrightess)
im2.save("im2-3.jpg")



 
distance = 0
for i in range(300):
    for j in range(1161):
        if im1.getpixel((i, j)) != im2.getpixel((i, j)):
            distance += 1

 
if distance<noticeval:
    requests.get(noticeurl)
print(distance)
