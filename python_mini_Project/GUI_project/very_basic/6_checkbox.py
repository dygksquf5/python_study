from tkinter import *

root = Tk()
root.title("GUI_yosuniiiii")

root.geometry("640x480+300+100")

chkvar = IntVar() # chkvar 에 int 형으로 값을 저장한다
chkbox = Checkbutton(root, text ="오늘하루 보지않기 ", variable=chkvar)
# chkbox.select() # 자동선택처리
# chkbox.deselect() # 선택된걸 다시 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지않기", variable=chkvar2)
chkbox2.pack()


def btncomand():
    # 인트로 저장한 값을 가져오기 !
    print(chkvar.get()) # 만약 숫자가 0 일땐 해제, 1일땐 체크가 된 상태임
    print(chkvar2.get())


btn1= Button(root, text="클릭", command=btncomand)
btn1.pack()


root.mainloop()
