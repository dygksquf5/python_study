from tkinter import *
import tkinter.messagebox as msg


root = Tk()
root.title("GUI_yosuniiiii")

root.geometry("640x480+300+100")


# 기차 예매 시스템이라고 가정하고 메세지 팝업
def info():
    msg.showinfo("알림", "정상적으로 예매 완료되었습니다.")


def warn():
    msg.showwarning("경고", "해당좌석은 매진되었습니다.")


def error():
    msg.showerror("에러", "결제 오류가 발생했습니다.")


def okcancel():
    msg.askokcancel("확인 / 취소", "해당좌석은 유아동반석입니다. 예매하시겠습니까?")


def trycancel():
    msg.askretrycancel("재시도 / 취소 ", "일시적인 오류입니다. 다시시도하시겠습니까 ? ")


def yesno():
    msg.askyesno("예 / 아니오 ", "해당 좌석은 역방향입니다. 예매하시겠습니까? ")



def yesnocancel():
    msg.askyesnocancel(title=None, message="예매내역이 저장되지 않았습니다. \n 저장후  예매하시겠습니까? ")


Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=trycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()


root.mainloop()
