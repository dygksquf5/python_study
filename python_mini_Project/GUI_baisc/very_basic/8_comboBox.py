import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI_yosuniiiii")

root.geometry("640x480+300+100")

# 콤보박스는 다른 모듈에서 따로 가져와야 함. ttk 에서 가져오기!

values = [str(i) + "일" for i in range(1, 32) ]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드결제일 ") # 최초 목록 제목 설정! ( 버튼 클릭을 통한 값 설정도 가능함! )

# state 에서 readonly 주면 창에다가 아무런 값을 입력할 수 없게 만듬
readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0) # 제일처음, 0인덱스 값이 가장먼저 보이게 만들어주기
readonly_combobox.pack()





def btncomand():
    print(combobox.get()) # 선택된 값 표시
    print(readonly_combobox.get())





btn1= Button(root, text="선택 ", command=btncomand)
btn1.pack()


root.mainloop()
