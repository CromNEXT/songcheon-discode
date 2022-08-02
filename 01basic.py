# tkinter 패키지 사용
#import tkinter = > tkinter.Tk()
#from import => TK()
# * = all
from tkinter import *
from turtle import title 

root = Tk()
root.title('Sello와 함께하는 꿈두레')
root.geometry("640x480") #창 크기 설정 곱셈 덧셈 모두 인식 가능 (단 덧셈은 x,y 순서로 인식)
root.resizable(True, False) # 가로세로 고정

root.mainloop() #mainloop() = 무한 반복 계속 실행 장치

#TKDocs = 명령어 알아보기