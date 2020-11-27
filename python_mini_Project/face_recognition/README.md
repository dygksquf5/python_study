# This is a face recognition mini personal project for study





# shape_predictor_68_face_landmarks.dat로 학습된 모델 데이터를 사용함 

- 총 68개의 점으로 cv2 위에 face detect 하기. 

<img width="959" alt="Screenshot 2020-11-27 at 1 31 10 PM" src="https://user-images.githubusercontent.com/66229916/100411389-fa81f700-30b4-11eb-9c49-c5964b737c3b.png">




# 최대 최소 구한 값을 cv2 위에 파란점으로 표시하기

    cv2.circle(img, center=tuple(top_left), radius=2, color=[255, 0, 0], thickness=2, lineType=cv2.LINE_AA)
    cv2.circle(img, center=tuple(bottom_right), radius=2, color=[255, 0, 0], thickness=2, lineType=cv2.LINE_AA)


# 센터 평균 구한 값을 cv2 위에 다시 빨간점으로 표시하기
    cv2.circle(img, center=tuple((center_x, center_y)), radius=2, color=[0, 0, 255], thickness=2, lineType=cv2.LINE_AA)
    
    
    
# 빨간점, 즉 중심점을 기준으로 위에 overlay 할 이미지를 올림. 
<img width="962" alt="Screenshot 2020-11-27 at 1 41 25 PM" src="https://user-images.githubusercontent.com/66229916/100411887-4f723d00-30b6-11eb-9438-476870680f3f.png">


    result = overlay_transparent(img, overlay, center_x, center_y - 25, overlay_size=(face_size, face_size))

