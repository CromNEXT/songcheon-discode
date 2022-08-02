from tkinter import *
from turtle import title 

root = Tk()
root.title('Sello와 함께하는 꿈두레')
root.geometry("640x480") #창 크기 설정 곱셈 덧셈 모두 인식 가능 (단 덧셈은 x,y 순서로 인식)
root.resizable(True, False) # 가로세로 고정

Label(root, text="select a menu").pack()
burger_var = IntVar() #변수 덕에 음료와 혼선 안됨.
btn_burger1 = Radiobutton(root, text="불고기버거", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="기네스와퍼", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="스태커4 버거", value=3, variable=burger_var)
btn_burger4 = Radiobutton(root, text="스태커3 버거", value=4, variable=burger_var)
btn_burger5 = Radiobutton(root, text="스태커2 버거", value=5, variable=burger_var)
btn_burger6 = Radiobutton(root, text="스태커1 버거", value=6, variable=burger_var)


btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()
btn_burger4.pack()
btn_burger5.pack()
btn_burger6.pack()

Label(root, text="select a drink").pack()
drink_var = StringVar()

btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink2 = Radiobutton(root, text="칠성사이다", value="칠성사이다", variable=drink_var)
btn_drink3 = Radiobutton(root, text="스프라이트", value="스프라이트", variable=drink_var)
btn_drink4 = Radiobutton(root, text="제로콜라", value="제로콜라", variable=drink_var)
btn_drink5 = Radiobutton(root, text="오렌지쥬스", value="오렌지쥬스", variable=drink_var)
btn_drink6 = Radiobutton(root, text="물", value="물", variable=drink_var)
btn_drink7 = Radiobutton(root, text="선택안함", value="선택안함", variable=drink_var)


btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()
btn_drink4.pack()
btn_drink5.pack()
btn_drink6.pack()
btn_drink7.pack()


def cmd():
    print(burger_var.get())
    print(drink_var.get())
    
btn=Button(root, text="Order", command=cmd)

btn.pack()   

root.mainloop() #mainloop() = 무한 반복 계속 실행 장치

#TKDocs = 명령어 알아보기