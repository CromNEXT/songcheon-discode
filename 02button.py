from tkinter import *
from turtle import title 

root = Tk()
root.title('Sello와 함께하는 꿈두레')
root.geometry('300x250')

btn1 = Button(root, text = '버튼1')
btn1.pack() #생성과 위젯 세부사항 설정
btn2 = Button(root, padx=5, pady = 10, text = '버튼2') #padx,pady = 여백 크기 조절
btn2.pack()
btn3 = Button(root, padx=10, pady = 5, text = '버튼3') 
btn3.pack()
btn4 = Button(root, width=10, height=3, text = '버튼4') #padx,pady = 전체 크기 조절
btn4.pack()
btn5 = Button(root, fg='red', bg='yellow', text = '버튼5') #폰트 조절
btn5.pack()

photo=PhotoImage(file="C:\\Users\\doyou\\OneDrive\\바탕 화면\\0'c\\ing.png")
btn6 = Button(root,image=photo)
btn6.pack()
root.mainloop() #mainloop() = 무한 반복 계속 실행 장치
