# 015.py
from PIL import Image
im = Image.open('../../../img/002.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')
input("end~~~")
