from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree

from bs4 import BeautifulSoup
import random
from time import sleep


drive = webdriver.Chrome("./chromedriver")
url = "https://www.instagram.com"
drive.get(url)
action = ActionChains(drive)

login = WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "._9GP1n   ")))
login.click()

sleep(1)

action.send_keys("dmsdlquf5@naver.com").perform()

action = ActionChains(drive)

(
    action.key_down(Keys.TAB).pause(1)
        .send_keys("rla886400").pause(1)
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

for i in range(number):
    try:
        drive.implicitly_wait(6)
        drive.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div').click()
        sleep(1.5)
        if i == 0:
            drive.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()
            sleep(1)
        else:
            drive.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
            sleep(1)
        print("좋아요 누른 횟수 : [{}]".format(i))
    except Exception:
        try:
            drive.implicitly_wait(6)
            drive.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
            sleep(1.5)
            if i == 0:
                drive.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click()
                sleep(1)
            else:
                drive.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
                sleep(1)
            print("좋아요 누른 횟수 : [{}]".format(i))
        except Exception:
            continue




