#일정 간격으로 스크린 샷 찍는 프로그램

import time 
from PIL import ImageGrab #pip install pillow

time.sleep(5)

for i in range(1, 11): #10장 찍기
    img = ImageGrab.grab()
    img.save("image{}.png".format(i))
    time.sleep(1)