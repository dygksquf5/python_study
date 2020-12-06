from tkinter import *

root = Tk()
root.title("GUI_yosuniiiii")

root.geometry("640x480+300+100")

Label(root, text="메뉴를 선택하세요").pack()


burger_var = IntVar() # Int 값으로 값저장 !
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select() # 미리 선택해놓고 시작하기!
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


Label(root, text="음료를 선택하세용").pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncomand():
    print(burger_var.get()) # 선택된 radio 항목의 값을 반환합니당 ! int로!
    print(drink_var.get()) # 음료중 선택된 값 출력


btn1= Button(root, text="주문", command=btncomand)
btn1.pack()


root.mainloop()
