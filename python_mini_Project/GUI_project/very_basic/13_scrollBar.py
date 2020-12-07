from tkinter import *
import tkinter.messagebox as msg


root = Tk()
root.title("GUI_yosuniiiii")
root.geometry("640x480+300+100")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
# fill 을 y 축으로 채우게 해서 위아래로 쫙 채워지게 해주기!
scrollbar.pack(side="right", fill="y")

# command에 set 이 없으면 스크롤을 내려도 다시 올라온다!
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32):
    listbox.insert(END, str(i) + "일" )


listbox.pack(side="left")

# 이렇게 스크롤바에도 리스트박스를 맵핑 해줘서 스크롤바와 리스트박스가 서로 함께 맵핑 돼서 움직이도록하기
scrollbar.config(command=listbox.yview)

root.mainloop()
