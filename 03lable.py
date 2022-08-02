from tkinter import *
from turtle import title 
root = Tk()
root.title('Sello와 함께하는 꿈두레')
root.geometry("640x480") #창 크기 설정 곱셈 덧셈 모두 인식 가능 (단 덧셈은 x,y 순서로 인식)
label1 = Label(root, text='안#녕^@#하세요!$@')
label1.pack()
photo=PhotoImage(file="C:\\Users\\doyou\\OneDrive\\바탕 화면\\0'c\\ing.png")
label2 = Label(root, image=photo)
label2.pack()
def change():
    label1.config(text="see you 'next' time")
    global photo2
    photo2 = PhotoImage(file="C:\\Users\\doyou\\OneDrive\\바탕 화면\\0'c\\img2.png")
    label2.config(image=photo2)
def rollback():
    label1.config(text="안#녕^@#하세요!$@")
    global photo1
    photo1 = PhotoImage(file="C:\\Users\\doyou\\OneDrive\\바탕 화면\\0'c\\ing.png")
    label2.config(image=photo1)
btn=Button(root, text="Click", command=change)
btn.pack()    
btn1 = Button(root, text="rollback", command=rollback)
btn1.pack()
#TKDocs = 명령어 알아보기
root.mainloop() #mainloop() = 무한 반복 계속 실행 장치