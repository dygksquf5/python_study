import keyboard
from PIL import ImageGrab
import time


def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))


keyboard.add_hotkey("F9", screenshot)  # 사용자가 F9 누르면 스크린샷 저장
keyboard.wait("esc")  # 사용자가 esc 누를 때 까지 프로그램 수행

# 근데 이거 맥북에서는 터미널창에서 sudo로 관리자모드로 실행시켜야 가능합니다아ㅏㅏ !