from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

action.send_keys("dygksquf5@naver.com").perform()

action = ActionChains(drive)

(
    action.key_down(Keys.TAB).pause(1)
        .send_keys("Wkdms123&").pause(1)
        .perform()
)
drive.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()

# drive.implicitly_wait(10)

sleep(3)

search_1 = "https://www.instagram.com/explore/tags/서울맛집/"
drive.get(search_1)


print(drive.page_source)

