# 파이썬으로 웹 자동화 하기! selenium 과 actionchains 사용하기!

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

drive = webdriver.Chrome("./chromedriver")
url = "https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f"
drive.get(url)
sleep(2)

# 드라이버를 열면 창 크기를 최대로 열기!
drive.maximize_window()
action = ActionChains(drive)
sleep(2)

drive.find_element_by_css_selector(".s-btn__google").click()

# 이제 로그인창이 바로 뜰테니까 아이디 입력하며 되는데, 보통 인터넷은 켜면 로그인창에 바로 커서가 깜빡이니까 로그인버튼을 찾는것 처럼
# 아이디값을 찾을 필요 없이 바로 action 으로 send key 해주면됨!

# drive.implicitly_wait(10) # 최대 10초까지 기다려주지만 그전에 다 뜨면 실행 고고
button_1 = WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".whsOnd.zHQkBf")))
button_1.click()
action.send_keys("dygksquf5@naver.com").perform()  # 꼭 perform 해줘야 실행이 됨!!!
action.reset_actions()  # 액션을 하나씩 퍼폼 해줄 때 마다 밑에다 리셋 해줘! 안그럼 액션이 중복될 수 있음 !
drive.find_element_by_css_selector(".VfPpkd-RLmnJb").click()

sleep(3)
# 선택적한 값이 나타나기전까지 최대 10초를 기다림!
button = WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".whsOnd.zHQkBf")))
button.send_keys("Wkdms123&")
# drive.find_element_by_css_selector(".whsOnd.zHQkBf").send_keys("Wkdms123&")

drive.find_element_by_css_selector(".VfPpkd-RLmnJb").click()

sleep(8)

drive.get("https://gmail.com")

# 로그인 버튼 누르기 !
# drive.find_element_by_css_selector(".VfPpkd-RLmnJb").click()

# 이메일 보내기 버튼 !!

write_email = WebDriverWait(drive, 8).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".T-I.T-I-KE.L3")))

write_email.click()
sleep(2)
send_button = drive.find_element_by_css_selector(".dC")

action = ActionChains(drive) # reset이 안먹혀서 새로 action 지정 해 주자 !

(
    action.send_keys("dygksquf5@naver.com").pause(2).key_down(Keys.TAB).pause(2).key_down(Keys.TAB)
        .send_keys("selenium 공부를 위한 이메일 입니다! ").pause(2).key_down(Keys.TAB)
        .send_keys("내용을 넣어봐야 돼용!").key_down(Keys.ENTER)
        .send_keys("abcd 이렇게 소문자를 먼저 넣은다음").key_down(Keys.ENTER).pause(2)
        .key_down(Keys.SHIFT).send_keys("abcd 저는 소문자를 쳤지만 이걸 쉬프트로 대문자로 바꿔놓은 것 이 죠 !! ").key_up(Keys.SHIFT).pause(2)
        .move_to_element(send_button).click()  # 이렇게 위에서 드라이브로 찾은 클래스 값을 move_to 로 그 위로 가상의 마우스가 이동하게 한다음 클릭하게 하기
        .perform()  # 최종적으로 이 한줄의 코드를 실행시키는 퍼폼 입력해주기!
)
