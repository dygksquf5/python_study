from tkinter import *
import tkinter.messagebox as msg


root = Tk()
root.title("GUI_yosuniiiii")
root.geometry("640x480+300+100")


# btn1 = Button(root, text="버튼1")
#
# btn2 = Button(root, text="버튼2")
# # btn1.pack(side="left")
# # btn2.pack(side="left")
#
# # 이렇게 grid 쓰면 2차원적 배열 에 x,y인덱스값에 넣는 느낌으로!
# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)


# 키보드를 grid로 구현해보기!!

# 가장먼저, 맨 윗줄

# 글자기준으로 pad x,y를 늘리기!
btn_f16 = Button(root, text="F16", width=5, height=2)
btn_f17 = Button(root, text="F17", width=5, height=2)
btn_f18 = Button(root, text="F18", width=5, height=2)
btn_f19 = Button(root, text="F19", width=5, height=2)

# 이렇게 grid 에다가 pad 주면 해당 버튼이 위치하는 곳에서 서로의 간격을 넓히게 됨 pad x, y 만큼!!
btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3) # 내가 지정한 방향으로 쫙 늘리는거임 sticky
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)


# clear 줄 !
btn_clear = Button(root, text="clear", width=5, height=2)
btn_equal = Button(root, text="equal", width=5, height=2)
btn_div = Button(root, text="div", width=5, height=2)
btn_mut = Button(root, text="mut", width=5, height=2)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mut.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 7 시작줄

btn_7 = Button(root, text="7", width=5, height=2)
btn_8 = Button(root, text="8", width=5, height=2)
btn_9 = Button(root, text="9", width=5, height=2)
btn_sub = Button(root, text="-", width=5, height=2)

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 4 시작줄

btn_4 = Button(root, text="4", width=5, height=2)
btn_5 = Button(root, text="5", width=5, height=2)
btn_6 = Button(root, text="6", width=5, height=2)
btn_add = Button(root, text="+", width=5, height=2)

btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)


# 1 시작줄

btn_1 = Button(root, text="1", width=5, height=2)
btn_2 = Button(root, text="2", width=5, height=2)
btn_3 = Button(root, text="3", width=5, height=2)
btn_enter = Button(root, text="enter", width=5, height=2) # 세로로 합쳐져야 함 !

btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) # rowspand 은 row 두개를 합치는거


# 0 시작줄

btn_0 = Button(root, text="0", width=5, height=2) # 가로로 합쳐지기
btn_point = Button(root, text=".", width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3) # 현재위치로부터 오른쪽으로 몇칸 더함
btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop()
