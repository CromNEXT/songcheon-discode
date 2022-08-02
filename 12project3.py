from tkinter import*
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msgbox
import os
from PIL import Image

root=Tk()
root.title('NEXT.Project')

#파일추가
def add_file():
    files=filedialog.askopenfilenames(title = "이미지 파일을 선택하세요.", filetypes = (("PNG파일","*.PNG"),("모든 파일", ".")), initialdir = r"C:\Users\doyou\OneDrive\바탕 화면\0'c")
    for file in files:
        list_file.insert(END, file)
#선택 삭제
def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

#저장 경로
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected is None:
        return
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(0, folder_selected)
#시작
def start():
    print("가로너비:",cmb_width.get())
    print("간격:",cmb_space.get())
    print("포멧:",cmb_format.get())
    
    if list_file.size() == 0: #이미지 파일이 없는 경우
        msgbox.showwarning("경고","이미지 파일을 추가하세요")
        return
    if len(txt_dest_path.get()) == 0: #저장 경로가 없는 경우
        msgbox.showwarning("경고","저장 경로를 선택하세요")
        return
    #이미지 통합
    merge_image()
    
#이미지 통합(merge)
def merge_image(): 
    images = [Image.open(x) for x in list_file.get(0,END)]
    #print(images[0].size)
    widths, heights = zip(*(x.size for x in images))    
    
    max_width = max(widths)
    total_height = sum(heights)
    
    result_img = Image.new("RGB", (max_width, total_height), (255,255,255)) #RGB계열, (가로, 세로), 배경색(흰)
    y_offset = 0 #이미지 y위치
    
    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))
        y_offset = y_offset+img.size[1]
    dest_path = os.path.join(txt_dest_path.get(),"project.png")
    result_img.save(dest_path)
    msgbox.showinfo("알림", "작업이 완료되었습니다")    
            
#파일 프레임
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)
btn_add_file = Button(file_frame, padx= 5, pady= 5, width=12, text="파일추가",  command=add_file)
btn_add_file.pack(side="left")
btn_del_file = Button(file_frame, padx= 5, pady= 5, width=12, text="파일삭제", command=del_file)
btn_del_file.pack(side="right")

list_frame = Frame(root)#리스트 프레임
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extanded", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

#경로 프레임
path_frame = LabelFrame(root, text='저장경로')
path_frame.pack(fill="x", padx= 5, pady= 5, ipady=5)
txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side = "left", fill="x", expand = True, padx=5, pady=5)
btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx= 5, pady=5)

#프레임 옵션
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

#frame_option 가로 넓이
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

opt_width = ["없음","1024","800","640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

#frame_option 간격
lbl_space=Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

opt_space = ["없음","좁게","보통","넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

#frame_option 포멧
lbl_format=Label(frame_option, text="포멧", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

opt_format = ["PNG","JPG","BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)


#실행 프레임
run_frame = Frame(root)
run_frame.pack(fill="x", padx=5, pady=5)
 #닫기 버튼
btn_close = Button(run_frame, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

 #시작 버튼
btn_start = Button(run_frame, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()