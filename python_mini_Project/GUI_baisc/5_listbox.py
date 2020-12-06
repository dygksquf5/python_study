from tkinter import *

root = Tk()
root.title("GUI_yosuniiiii")

root.geometry("640x480+300+100")

# selectmode 는 single 하면 하나면 선택 가능 ,height 는 0 해야 내가 넣은 애들 다 나오게 해줄 수 있음.
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박") # 사실 앞에는 인덱스 대신 END 해서 제일 뒤에 붙게 만들어도 됨
listbox.insert(END, "포도")
listbox.pack()


def btncomand():
    # listbox.delete(END) # 맨 뒤 삭제됨
    # listbox.delete(0)  # 맨 앞 삭제됨

    # 갯수확인
    # print("리스트에는", listbox.size(), "개가 있어요! ")

    # 항목확인
    # print("1번째부터 3번째까지 항목 : ", listbox.get(0, 2)) #인덱스 값으로

    # 선택된 항목 확인
    print("선택된 항목 : ", listbox.curselection()) # 인덱스값 출력해줌



btn1= Button(root, text="클릭", command=btncomand)
btn1.pack()


root.mainloop()
