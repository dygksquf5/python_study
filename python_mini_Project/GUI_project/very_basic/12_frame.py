from tkinter import *
import tkinter.messagebox as msg


root = Tk()
root.title("GUI_yosuniiiii")
root.geometry("640x480+300+100")

Label(root, text="메뉴를 선택 해 주세용").pack(side="top")

Button(root,text="주문하기").pack(side="bottom")


frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()


frame_drink = LabelFrame(root, text="음료")
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()
frame_drink.pack(side="right",fill="both", expand=True)



root.mainloop()
