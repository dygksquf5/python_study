from __future__ import unicode_literals
import youtube_dl

from tkinter import *
import tkinter.messagebox as message
import tkinter.ttk as ttk
from tkinter import filedialog
from PIL import Image
import os


root = Tk()
root.title("mp3_download_yosuniiiii")
# root.geometry("640x480+300+100")


# 저장경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '': # 사용자가 취소 눌렀을때 그냥 리턴
        return
    txt_dest_path.delete(0, END) # 엔트리로 만들어서 0 END 라고 하면됨
    txt_dest_path.insert(0, folder_selected)


# 시작
def start():

    class Download(object):
        def __init__(self, url):
            self.url = url
            self.save_path = txt_dest_path.get()
            self.song()
            print(txt_dest_path.get())

        def song(self):
            opts = {
                'verbose': True,
                'fixup': 'detect_or_warn',
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '1411',
                }],
                'extractaudio': True,
                'outtmpl': self.save_path + '/%(title)s.%(ext)s',
                'noplaylist': True,
                'nocheckcertificate': True,  # ssl 문제가 떠서 ca 체크 안하게 하기.
            }
            ydl = youtube_dl.YoutubeDL(opts)
            try:
                message.showinfo("다운로드시작", "잠시만 기다려주세용")
                ydl.download([self.url])
                message.showinfo("알림", "작업이 완료되었습니다! ")
            except:
                message.showinfo("경고", "작업이 완료되지 못했습니다. 잠시후 다시 시도 해 주세용! ")


    # 저장경로  확인하는 구간
    if len(txt_dest_path.get()) == 0:
        message.showwarning("경고 !", "저장경로를 선하택세요! ")

    print(txt_url.get())
    Download(txt_url.get())


# 리스트 프레임
list_frame = LabelFrame(root, text='다운받을 url을 복붙 하세요오')
list_frame.pack(fill="both", padx=5, pady=5)

txt_url = Entry(list_frame)
txt_url.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=2)



# 저장경로 프레임!
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x" , padx=5, pady=5, ipady=3)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=2) # i pad y , 즉 i = inner pad의 길이를 늘린다 y 축 길이를 늘릴거야!
btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right",padx=5, pady=5)


# 실행프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)


btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right",padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right",padx=5, pady=5)



root.resizable(False, False)
root.mainloop()