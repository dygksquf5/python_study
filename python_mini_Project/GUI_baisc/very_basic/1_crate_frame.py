from tkinter import *

root = Tk()
root.title("GUI_yosuniiiii")
# root.geometry("640x480") # 가로 x 세로
root.geometry("640x480+300+100") # 3번째 값은 x 위치, 4번째값은 y좌표, 창이 켜지는 위치설정

root.resizable(False, False) # x, y 값 변경 불가로 주기 (창 크기 변경 불가)


# 창이 꺼지지 않게 해주기
root.mainloop()