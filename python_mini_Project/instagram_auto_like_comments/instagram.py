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


# def parse(page_string):
#     beautiful = BeautifulSoup(page_string, "html.parser")
#
#     get_all = beautiful.findAll("div", {"class": "v1Nh3"})
#
#     links = []
#
#     for one in get_all:
#         insta_link = "https://instagram.com/"
#         find_href = one.find("a")['href']
#         links.append(insta_link + find_href)
#
#     return links


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

# sleep(5)


# 보안문제 걸려서 ㅠㅠㅠ
# drive.find_element_by_xpath('//*[@id="react-root"]/section/div/div/div[3]/form/span/button').click()
#
# drive.find_element_by_css_selector("._1wi_F")
#
# a, b, c, d, e, f = list(map(int, input(" 암호를 입력하세요 : ").split()))
#
# action = ActionChains(drive)
# action.send_keys(a, b, c, d, e, f).perform()
#
# sleep(3)
#
# drive.find_element_by_xpath('//*[@id="react-root"]/section/div/div/div[2]/form/span/button').click()
#
# drive.implicitly_wait(10)


search_all = ["https://www.instagram.com/explore/tags/여행가고싶다/", "https://www.instagram.com/explore/tags/영국유학/",
              "https://www.instagram.com/explore/tags/세종카페/", "https://www.instagram.com/explore/tags/경주여행/"]
# a = random.randint(0, 3)
# drive.get(search_all[a])
#
# name = input(" 검색어 입력  : ")
# search_url = "https://www.instagram.com/explore/tags/" + name + "/"
# drive.get(search_url)
# sleep(5)

links = []


def start_insta():
    global links
    name = input(" 검색어 입력  : ")
    search_url = "https://www.instagram.com/explore/tags/" + name + "/"
    drive.get(search_url)
    sleep(5)

    index = 0
    for _ in range(20):
        drive.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        index += 1

    if index == 20:
        page_source = drive.page_source
        beautiful = BeautifulSoup(page_source, "html.parser")
        get_items = beautiful.findAll("div", {"class": "v1Nh3"})
        for one in get_items:
            insta_link = "https://instagram.com/"
            find_href = one.find("a")['href']
            links.append(insta_link + find_href)
        index -= index

    print("가져온 링크 :[{}] ".format(len(links)), links)

    for url in links:
        print("좋아요 누른 페이지 링크 :", url)
        drive.get(url)
        random_time = random.randint(1, 6)
        sleep(random_time)
        message = [" 우와 ㅎㅎㅎ :) ", "잘보고 가요 ! "]
        drive.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
        # drive.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form').send_keys(message)
        # sleep(2)
        # drive.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button').click()
        if url == links[-1]:
            links = []
            start_insta()

    return


start_insta()


# if new_height == last_height:
#     drive.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     sleep(2)
#     new_height = drive.execute_script("return document.body.scrollHeight")
#     sleep(2)
#     if new_height == last_height:
#         break
#     else:
#         last_height = new_height
#         continue