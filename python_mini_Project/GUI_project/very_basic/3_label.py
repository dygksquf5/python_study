from tkinter import *

root = Tk()
root.title("GUI_yosuniiiii")

root.geometry("640x480+300+100")

label1 = Label(root, text="안녕하세요 ")
label1.pack()

photo = PhotoImage(file="image.gif")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="또만나요")
    # 함수안에서 이미지 바꾸거나 할때, 변수를 전역으로 선언 해줘야 컴터가 안버린당
    global photo2
    photo2 = PhotoImage(file="image_2.png")
    label2.config(image=photo2)



btn1 = Button(root, text="클릭", command=change)
btn1.pack()
root.mainloop()
