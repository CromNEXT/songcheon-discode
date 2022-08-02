from tkinter import *
from turtle import title 

root = Tk()
root.title('Sello와 함께하는 꿈두레')
root.geometry("640x480") #창 크기 설정 곱셈 덧셈 모두 인식 가능 (단 덧셈은 x,y 순서로 인식)
root.resizable(True, False) # 가로세로 고정

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0,"딸기")
listbox.insert(1,"사과")
listbox.insert(2,"바나나")  
listbox.insert(END,"수박")
listbox.insert(END,"배")
listbox.pack()

def btncmd():
    print("selected items:", listbox.curselection())
    print("selected items:", listbox.get(listbox.curselection()))
    print("number:", listbox.size())
    listbox.delete(listbox.curselection())
btn = Button(root, text = 'click', command = btncmd) 
btn.pack()   
root.mainloop() #mainloop() = 무한 반복 계속 실행 장치
#TKDocs = 명령어 알아보기