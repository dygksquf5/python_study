from tkinter import *
import tkinter.messagebox as message
import tkinter.ttk as ttk
from tkinter import filedialog
from PIL import Image
import os


root = Tk()
root.title("GUI_yosuniiiii")
# root.geometry("640x480+300+100")


# 파일추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",
                                        filetypes=(("PNG 파일", "*.png"),
                                                   ("모든파일", "*.*")),
                                        initialdir="/Users/yosuniiiii/python_study/python_mini_Project/GUI_project"
                                                   "/GUI_for_images_project")

    for file in files:
        list_file.insert(END, file)


# 선택삭제
def del_file():
    # print(list_file.curselection()) # 어떤 인덱스 뽑아오나ㅏㅏ~

    # 리스트를 뒤에서부터 지우려고! 앞에 지우면 앞 인덱스가
    # 지워지면서 전체 뒤에 인덱스 다바뀌니까 그냥 뒤에서부터 지우기 ㅠㅠ
    for index in reversed(list_file.curselection()):
        list_file.delete(index)


# 저장경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected is None: # 사용자가 취소 눌렀을때 그냥 리턴
        return
    txt_dest_path.delete(0, END) # 엔트리로 만들어서 0 END 라고 하면됨
    txt_dest_path.insert(0, folder_selected)


# 이미지 통합
def merge_image():
    # print(list_file.get(0, END)) # 모든 파일목록 가져올 수 있음
    images = [Image.open(x) for x in list_file.get(0, END)]
    # size -> size[0] : width, size[1] : height기

    # 리스트 컴프리핸션도 가능하고
    # widths = [x.size[0] for x in images] # 넓이 각각 마다 가져오기
    # heights = [x.size[1] for x in images] # 각각 높이 다 가져오기!
    # 이렇게로도 가능!
    widths, heights = zip(*(x.size for x in images)) # unzip 해서 바로 넣


    # 최대 넓이,전체 높이 구해봄 !
    max_widths, total_heights = max(widths), sum(heights)

    # 스케치북 준비 !
    result_img = Image.new("RGB", (max_widths, total_heights), (255,255,255,255)) # 배경흰색
    y_offset = 0  # y 위치정보!!! 위치 계속 업뎃 해줘야 함
    # for img in images:
    #     result_img.paste(img, (0, y_offset))
    #     y_offset += img.size[1] # height 만큼 리셋 !!! 1 이 height 였음! 0 은 width

    # 인덱스 가지고 progress bar 랑 연동시켜서 퍼센트별로 progress  바 움직이게 하기!
    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1]

        progress = (idx + 1) / len(images) * 100 # 실제 퍼센트 정보를 계산하기!
        p_bar.set(progress)
        progress_bar.update()

    dest_path = os.path.join(txt_dest_path.get(), "yosuniiiii.jpg")
    result_img.save(dest_path)
    message.showinfo("알림", "작업이 완료되었습니다! ")


# 시작
def start():
    # 각 옵션들 값을 확인하기
    print("가로넓이:", cmb_width.get())
    print("간격:", cmb_space.get())
    print("포맷:", cmb_format.get())

    # 파일목록 확인하는 구간
    if list_file.size() == 0:
        message.showwarning("경고 !", "이미지 파일을 추가하세요! ")
        return

    # 저장경로  확인하는 구간
    if len(txt_dest_path.get()) == 0:
        message.showwarning("경고 !", "저장경로를 선하택세요! ")

    # 이미지 통합! 함수 길어질거같으니ㅣㅣ
    merge_image()


# 파일 프레임 (파일추가, 선택삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5) # pad 로 간격주기

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택 삭제", command=del_file)
btn_del_file.pack(side="right")


# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")


list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)


# 저장경로 프레임!
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x" , padx=5, pady=5, ipady=3)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=2) # i pad y , 즉 i = inner pad의 길이를 늘린다 y 축 길이를 늘릴거야!
btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right",padx=5, pady=5)



# 옵션 프레임
frame_option = LabelFrame(root, text="옵션 ")
frame_option.pack(padx=5, pady=5, ipady=3)

# 1.가로넓이 옵션

# - 가로넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left",padx=5, pady=5)
# - 가로넓이 콤보
opt_width = ["원본유지", "1024","800","640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left",padx=5, pady=5)



# 2.간격옵션
# - 간격옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left",padx=5, pady=5)

# - 간격옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left")



# 3.파일포맷 옵션
# - 파일포맷옵션 레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left",padx=5, pady=5)

# - 파일포맷옵션 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left",padx=5, pady=5)


# 진행상황 progress bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=3)

p_bar = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_bar)
progress_bar.pack(fill="x",padx=5, pady=5)

# 실행프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)


btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right",padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right",padx=5, pady=5)




root.resizable(False, False)
root.mainloop()