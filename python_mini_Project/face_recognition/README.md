# This is a face recognition mini personal project for study


# shape_predictor_68_face_landmarks.dat로 학습된 모델 데이터를 사용함 

<img width="959" alt="Screenshot 2020-11-27 at 1 31 10 PM" src="https://user-images.githubusercontent.com/66229916/100411389-fa81f700-30b4-11eb-9c49-c5964b737c3b.png">

총 68개의 점으로 cv2 위에 face detect 하기. 

₩₩₩c

# 최대 최소 구한 값을 cv2로 그려보기! 파란점 !
    cv2.circle(img, center=tuple(top_left), radius=2, color=[255, 0, 0], thickness=2, lineType=cv2.LINE_AA)
    cv2.circle(img, center=tuple(bottom_right), radius=2, color=[255, 0, 0], thickness=2, lineType=cv2.LINE_AA)
