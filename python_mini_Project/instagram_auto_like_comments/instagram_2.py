from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random
from time import sleep
import time


# class CheckTime:
#     start = 0
#
#     @staticmethod
#     def start():
#         CheckTime.start = time.time()
#         return CheckTime.start
#
#     @staticmethod
#     def finish():
#         return time.time() - CheckTime.start


drive = webdriver.Chrome("./chromedriver")
url = "https://www.instagram.com"
drive.get(url)
action = ActionChains(drive)

login = WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "._9GP1n   ")))
login.click()

sleep(1)

action.send_keys("dmsdlquf5@naver.com").perform()
# action.send_keys("ga___nu").perform()

action = ActionChains(drive)

# 비 번 !

(
    action.key_down(Keys.TAB).pause(1)
    .send_keys("1q2w3e4r5t%%").pause(1)
    # .send_keys("Ghkddbfl123&").pause(1)
    # .send_keys("rksnWkdWkd@").pause(1)
    .perform()
)
drive.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()

drive.implicitly_wait(10)

drive.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
drive.implicitly_wait(10)

name = input(" 검색어 입력  : ")
number = int(input(" 좋아요를 몇번 누르시겠습니까 ? : "))
search_url = "https://www.instagram.com/explore/tags/" + name + "/"
drive.get(search_url)
sleep(5)

drive.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div').click()
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


for i in range(1, number):
    time_ori = 0
    time_for_like = random.randint(1, 10)
    if i % 300 == 0:
        print("자동화 deny 에 대한 예방을 위해 5분간 멈추겠습니다.")
        sleep(300)
        print("5분이 끝났습니다. 다시 시작하겠습니다. ")
    try:
        start = time.time()
        time_ori += start

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
