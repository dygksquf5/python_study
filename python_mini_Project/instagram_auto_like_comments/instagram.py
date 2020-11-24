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


def parse(page_string):
    beautiful = BeautifulSoup(page_string, "html.parser")
    # get = beautiful.find("div", {"class": "Nnq7C weEfm"})

    get_all = beautiful.findAll("div", {"class": "v1Nh3"})

    links = []

    for one in get_all:
        insta_link = "https://instagram.com/"
        find_href = one.find("a")['href']
        links.append(insta_link + find_href)

    return links


drive = webdriver.Chrome("./chromedriver")
url = "https://www.instagram.com"
drive.get(url)
action = ActionChains(drive)

login = WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "._9GP1n   ")))
login.click()

sleep(1)

action.send_keys("dygksquf5@naver.com").perform()

action = ActionChains(drive)

(
    action.key_down(Keys.TAB).pause(1)
        .send_keys("Wkdms123&").pause(3)
        .perform()
)
drive.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()

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

input(" 잠만 멈춰 ㅠㅠ흑 : ")

search_all = ["https://www.instagram.com/explore/tags/서울맛집/", "https://www.instagram.com/explore/tags/제주도여행/",
              "https://www.instagram.com/explore/tags/세종카페/","https://www.instagram.com/explore/tags/대전카페/"]
a = random.randint(1,5)
drive.get(search_all[a])

# drive.implicitly_wait(10)
sleep(5)


def start_insta():

    # max_height = drive.execute_script("return document.body.scrollHeight")

    drive.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)
    drive.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(4)
    
    page_source = drive.page_source

    beautiful = BeautifulSoup(page_source, "html.parser")

    get_all = beautiful.findAll("div", {"class": "v1Nh3"})

    links = []

    for one in get_all:
        insta_link = "https://instagram.com/"
        find_href = one.find("a")['href']
        links.append(insta_link + find_href)

    print("가져온 링크 : ", links)
    drive.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(4)

    for url in links:
        print("좋아요 누른 페이지 링크 :", url)
        drive.get(url)
        random_time = random.randint(1, 8)
        sleep(random_time)

        message = " 우와 ㅎㅎㅎ :) "

        drive.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
        # drive.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form').send_keys(message)
        # sleep(2)
        # drive.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button').click()

    drive.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(4)

    start_insta()


start_insta()
