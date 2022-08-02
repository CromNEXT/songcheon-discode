from tkinter import *
from turtle import title 

root = Tk()
root.title('Sello와 함께하는 꿈두레')
root.geometry("640x480") #창 크기 설정 곱셈 덧셈 모두 인식 가능 (단 덧셈은 x,y 순서로 인식)
root.resizable(True, False) # 가로세로 고정

chkvar = IntVar()
chkbox = Checkbutton(root, text="8번은 내일부터", variable=chkvar)
chkbox.selects() #자동 선택
#chkbox.deselect()# 선택 해지

chkbox.pack()
chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="넥스트 가입여부", variable=chkvar2)
chkbox2.pack()

def cmd():
    print(chkvar.get())
    chkbox.deselect()
btn=Button(root, text="Click", command=cmd)
btn.pack()   
root.mainloop() #mainloop() = 무한 반복 계속 실행 장치
#TKDocs = 명령어 알아보기