from tkinter import *
import os

root = Tk()
root.title("No title - Windows Textfile")
root.geometry("640x480")

#열기와 저장 파일 이름
filename = 'memo.txt'

def open_file():
    #파일이 있다면
    if os.path.isfile(filename):
        #filename파일을 file이라고 호출
        with open(filename,"r", encoding='utf8' )as file:
            txt.delete("1.0",END)
            txt.insert(END, file.read())

def save_file(): #r = 읽기모드(수정 안됨), w = 쓰기모드(수정 가능)
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))
#menu
menu1 = Menu(root) 
menu_file = Menu(menu1, tearoff=0) #파일 밑에 옵션 설정
menu_file.add_command(label="새로 만들기(N)                 Ctrl+N")
menu_file.add_command(label="새 창(W)                Ctrl+Shift+N")
menu_file.add_command(label="열기(O)...                       Ctrl+O", command = open_file)
menu_file.add_command(label="저장(S)                          Ctrl+S", command= save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기(X)", command = root.quit)

menu1.add_cascade(label = 'File(F)', menu=menu_file) #cascade 서식, 보기, 파일같이 칸 나누기
menu1.add_cascade(label = 'edit(E)')
menu1.add_cascade(label = 'option(O)')
menu1.add_cascade(label = 'view(V)')
menu1.add_cascade(label = 'help(H)')

#스크롤바
scrollbar = Scrollbar()
scrollbar.pack(side="right", fill="y")


#본문
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=txt.yview)

root.config(menu=menu1)
root.mainloop() 