from tkinter import *

root = Tk()
root.title("GUI_yosuniiiii")

root.geometry("640x480+300+100")


def creade_new_file():
    print(" 새 파일을 만듭니다")



menu = Menu(root)

# File 메뉴 !!
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=creade_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()  # 구분짓기!
menu_file.add_command(label="Open file...")
menu_file.add_separator()  # 구분짓기!
menu_file.add_command(label="Save all", state="disable") # 해당부분 비활성화
menu_file.add_command(label="Exit", command=root.quit) # 루트 큇 함으로써 종료!

# 메뉴에다가 메뉴파일 넣어주기!
menu.add_cascade(label="File", menu=menu_file)


# Edit 메뉴 !
menu.add_cascade(label="Edit")


# Language 버튼 추가! Radio 버튼으로 택 1 가능하게!
menu_lang = Menu(menu, tearoff=0 )
menu_lang.add_radiobutton(label = "Python")
menu_lang.add_radiobutton(label = "Java")
menu_lang.add_radiobutton(label = "C++")
menu.add_cascade(label="Language", menu=menu_lang)


# 체크박스 메뉴!
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(labe="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)


root.config(menu=menu)
root.mainloop()
