from tkinter import *

root = Tk()
root.title("GUI_yosuniiiii")

root.geometry("640x480+300+100")

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")


# 입력할 때 엔터가 안됨!! 이건 아이디같이 한줄만 입력받을 때 !
e = Entry(root, width=30)
e.pack()
e.insert(0, "한줄만 입력해요")


def btncomand():
    # 1.0 의 의미, 1 은 line 1 부터 가져와라, 0 은 컬럼기준으로 0번째 위치(index)부터 가져오기., END까지 가져오기 제일 마지막.
    # Text 는 이렇게 가져와야하고
    print(txt.get("1.0", END))
    # Entry 는 get()만 해주면 됨, 왜냐면 어자피 한줄이라
    print(e.get())

    # 내용삭제
    txt.delete("1.0", END)
    # 0 부터 마지막까지
    e.delete(0,END)

btn1= Button(root, text="클릭", command=btncomand)
btn1.pack()

root.mainloop()
