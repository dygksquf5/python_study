import os
from tkinter import *



root = Tk()
root.title(" 제목없음 - yosuniiiii 메모장  ")
root.geometry("640x480+300+100")

# 열기 저장 대상 파일이름
filename = "mynote.txt"


def open_file():
    if os.path.isfile(filename): # 있으면 true 없으면 false
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END) # 현재 써져있는 텍스트 삭제하고!
            txt.insert(END, file.read()) # 그다음 다시 불러온 파일 입력하기


def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) # 모든내용 가져와서 저장하기!


menu = Menu(root)

# 파일 메뉴 기능!
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

# 편집 서식 보기 도움말 껍데기만 !
menu.add_cascade(label="편집", menu=menu_file)
menu.add_cascade(label="서식", menu=menu_file)
menu.add_cascade(label="보기", menu=menu_file)
menu.add_cascade(label="도움말", menu=menu_file)


# 스크롤바

scrollbar = Scrollbar(root)
scrollbar.pack(side = "right", fill="y")


# 본문영
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)

root.config(menu=menu)


# 창이 꺼지지 않게 해주기
root.mainloop()