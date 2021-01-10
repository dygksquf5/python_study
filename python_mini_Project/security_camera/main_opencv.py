import cv2
import pygame

cam = cv2.VideoCapture(0)
pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
sfx1 = pygame.mixer.Sound('alert.ogg')


while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0) # 살짝 블러하게 만들어주고
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) # 샤프하게 만들어주기 노이지를 좀 제거해주기위해.
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 255), 2)
    for c in contours:
        if cv2.contourArea(c) < 5000:# 움직임이 작은 부분은 표시하지 않고 무시하기
            continue
        x, y, w, h = cv2.boundingRect(c) # 이걸로 x, v 축과 width, height 구한다음 네모의 꼭지점을 구해서 큰 사각형 나타나게하기
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        sfx1.set_volume(0.5)
        sfx1.play(0, 250)

    if cv2.waitKey(33) == ord("!"):
        break
    cv2.imshow('yosuniiiii_security', frame1)


