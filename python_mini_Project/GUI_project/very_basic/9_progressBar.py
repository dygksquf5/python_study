import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title("GUI_yosuniiiii")

root.geometry("640x480+300+100")

# indeterminate 는 결정되지 않은거!!!
# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) # 10ms 마다 움직임!
# progressbar.pack()
#
#
# def btncomand():
#     progressbar.stop()  # 작동중지!
#
#
# btn1= Button(root, text="중지 ", command=btncomand)
# btn1.pack()


p_var2 = DoubleVar() # 퍼센트를 실수도 반영하려고! 늘 정수가 아니니까
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncomand2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i)
        progressbar2.update() # 포문이 매번 돌 때마다 GUI 업데이트 되게 만들기!! 이거 안해주면 for 문 다 돌린다음 GUI에 적용됨

        print("현재 상태", p_var2.get() )


btn2= Button(root, text="시작 ", command=btncomand2)
btn2.pack()


root.mainloop()
