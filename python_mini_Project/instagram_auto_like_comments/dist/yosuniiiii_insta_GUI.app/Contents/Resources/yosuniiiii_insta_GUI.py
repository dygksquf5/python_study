import os

from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as message

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import random
from time import sleep
import time





root = Tk()
root.title("GUI_yosuniiiii")
# root.geometry("640x480") # 가로 x 세로
root.geometry("300x500+300+100")  # 3번째 값은 x 위치, 4번째값은 y좌표, 창이 켜지는 위치설정


def resource_path(relative_path):
    try:
        base_path = sys.MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



def start():
    try:
        if len(id_insta.get()) == 0:
            message.showerror("어어어ㅓㅓ", "아이디 입력하기!!! 제대로!")
            return

        if len(pw_insta.get()) == 0:
            message.showerror("에러!!", "비번 빼먹었어!!!")
            return

        if len(search_insta.get()) == 0:
            message.showerror("에러에러!!", "검색어 입력해야 검색을하지요!!!")
            return

        # drive = webdriver.Chrome(resource_path(r"./chromedriver"))
        drive = webdriver.Chrome(ChromeDriverManager().install())
        url = "https://www.instagram.com"
        drive.get(url)
        action = ActionChains(drive)

        login = WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "._9GP1n   ")))
        login.click()

        sleep(1)

        action.send_keys(id_insta.get()).perform()

        action = ActionChains(drive)

        # 비 번 !

        (
            action.key_down(Keys.TAB).pause(1)
                .send_keys(pw_insta.get()).pause(1)
                .perform()
        )
        drive.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()

        drive.implicitly_wait(10)

        drive.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
        drive.implicitly_wait(10)

        sleep(4)
        search_url = "https://www.instagram.com/explore/tags/" + search_insta.get()
        drive.get(search_url)
        sleep(5)

        drive.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div').click()
        sleep(1)

        # 인스타가 두가지 형식의 xpath를 가지고 있어서, 어떤 xpath 인지 알아보기 위함.
        try:
            drive.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a')
            xpath = '/html/body/div[5]/div[1]/div/div/a'
            button = '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div'
            print(" 5번 div")

        except Exception:
            drive.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
            xpath = '/html/body/div[4]/div[1]/div/div/a'
            button = '/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button'

            print(" 4번 div ")

        for i in range(1, int(like_times.get()) + 1):
            # 퍼센트 !
            progress = (i + 1) / int(like_times.get()) * 100 # 실제 퍼센트 정보를 계산하기!
            p_bar.set(progress)
            progress_bar.update()

            time_ori = 0
            time_for_like = random.randint(1, 10)
            if i % 300 == 0:
                print("자동화 deny 에 대한 예방을 위해 5분간 멈추겠습니다.")
                sleep(300)
                print("5분이 끝났습니다. 다시 시작하겠습니다. ")
            if i == int(like_times.get()):
                message.showinfo("완료!", "좋아요 입력한만큼 다 돌렸습니당! \n {} 번 ".format(i))
                break

            try:
                start_time = time.time()
                time_ori += start_time

                drive.implicitly_wait(10)
                # 좋아요 누르는 path
                sleep(time_for_like)
                drive.find_element_by_xpath(button).click()
                sleep(1.5)
                if i == 1:
                    drive.find_element_by_xpath(xpath).click()
                    sleep(1)
                else:
                    drive.find_element_by_xpath(xpath + '[2]').click()
                    sleep(1)
                print("좋아요 누른 횟수 : [{}]".format(i))
            except Exception:
                try:
                    finish = time.time() - time_ori
                    if finish >= 10:
                        print("시간초과")
                        print("시간초과로 인해 다음페이지로 넘기겠습니다.: [{}]".format(finish))
                        drive.find_element_by_xpath(xpath + '[2]').click()
                        sleep(1)
                except Exception:
                    print("time to rest due to an error")
                    sleep(300)
                    drive.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/button[2]').click()
                    continue

    except Exception as err:
        message.showerror("에러", err)


# 아이디 !
id_frame = LabelFrame(root, text="ID 입력하기!")
id_frame.pack(fill="x", padx=5, pady=5, ipady=3)

id_insta = Entry(id_frame)
id_insta.pack(side="left", fill="x", expand=True, padx=5, pady=5,
              ipady=2)  # i pad y , 즉 i = inner pad의 길이를 늘린다 y 축 길이를 늘릴거야!

# 비밀번호
pw_frame = LabelFrame(root, text="비번 입력하기!")
pw_frame.pack(fill="x", padx=5, pady=5, ipady=3)

pw_insta = Entry(pw_frame)
pw_insta.pack(side="left", fill="x", expand=True, padx=5, pady=5,
              ipady=2)

# 검색어
search_frame = LabelFrame(root, text="검색어 입력하기!")
search_frame.pack(padx=5, pady=5, ipady=3)

search_insta = Entry(search_frame)
search_insta.pack(side="left", fill="x", expand=True, padx=5, pady=5,
                  ipady=2)

# 좋아요 횟수
like_frame = LabelFrame(root, text=" 좋아요 몇번할지 정하기!!")
like_frame.pack(padx=5, pady=5, ipady=3)

like = Label(like_frame, text="좋아요 몇번할까용??", width=15)
like.pack(side="left", padx=5, pady=5)
# - 가로넓이 콤보
num_of_like = [5, 200, 500, 700, 1000, 1500]
like_times = ttk.Combobox(like_frame, state="readonly", values=num_of_like, width=5)
like_times.current(0)
like_times.pack(side="left", padx=5, pady=5)

# 진행상황 progress bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=3)

p_bar = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_bar)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="그만하기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)

root.mainloop()
