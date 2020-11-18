import cv2, dlib, sys
import numpy as np

scales = 0.5

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture('children.mp4')

# load overlay image
overlay = cv2.imread("kakao.png", cv2.IMREAD_UNCHANGED)


# overlay function
def overlay_transparent(background_img, img_to_overlay_t, x, y, overlay_size=None):
    try:
        bg_img = background_img.copy()
        # convert 3 channels to 4 channels
        if bg_img.shape[2] == 3:
            bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2BGRA)

        if overlay_size is not None:
            img_to_overlay_t = cv2.resize(img_to_overlay_t.copy(), overlay_size)

        b, g, r, a = cv2.split(img_to_overlay_t)

        mask = cv2.medianBlur(a, 5)

        h, w, _ = img_to_overlay_t.shape
        roi = bg_img[int(y - h / 2):int(y + h / 2), int(x - w / 2):int(x + w / 2)]

        img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))
        img2_fg = cv2.bitwise_and(img_to_overlay_t, img_to_overlay_t, mask=mask)

        bg_img[int(y - h / 2):int(y + h / 2), int(x - w / 2):int(x + w / 2)] = cv2.add(img1_bg, img2_fg)

        # convert 4 channels to 4 channels
        bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGRA2BGR)

        return bg_img
    # 만약 화면 밖으로 얼굴 이미지가 벗어나거나 해서 인식을 하지 못할 땐, 오버레이 된 이미지 없애고 그냥 원래 백그라운드 이미지 리턴!
    except Exception:
        return background_img


while True:
    # 프레임 단위로 끊어 읽기! 비디오 끝날 때 까지 계속 재생 시키고,.
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.resize(img, (int(img.shape[1] * scales), int(img.shape[0] * scales)))
    ori = img.copy()

    # detect faces
    faces = detector(img)
    # 0 번 인덱스 (얼굴하나) 만 지정!
    face = faces[0]

    dlib_shape = predictor(img, face)
    # 연산을 위해 dlib 으로 받은 객체를 numpy 배열로 !
    shape_2d = np.array([[p.x, p.y] for p in dlib_shape.parts()])

    # numpy 로 min, max 로 최소 최대 구하기!
    top_left = np.min(shape_2d, axis=0)
    bottom_right = np.max(shape_2d, axis=0)

    # 얼굴크기! 이 크기만큼 overlay 하기 위해!
    face_size = int(max(bottom_right - top_left) * 3.4)
    # 평균값으로 xy의 평균 구해서 센터를 구하자!
    center_x, center_y = np.mean(shape_2d, axis=0).astype(np.int)

    result = overlay_transparent(img, overlay, center_x, center_y - 25, overlay_size=(face_size, face_size))

    # visualise
    img = cv2.rectangle(img, pt1=(face.left(), face.top()), pt2=(face.right(), face.bottom()), color=(255, 255, 255),
                        thickness=2, lineType=cv2.LINE_AA)

    # for문으로 shape_2d 에 있는 총 68개의 점 ( dlib 모듈에서 제공 총 68개의 점으로 ) 을 cv2를 통해 그리기!
    for i in shape_2d:
        cv2.circle(img, center=tuple(i), radius=1, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)

    # 최대 최소 구한 값을 cv2로 그려보기! 파란점 !
    cv2.circle(img, center=tuple(top_left), radius=2, color=[255, 0, 0], thickness=2, lineType=cv2.LINE_AA)
    cv2.circle(img, center=tuple(bottom_right), radius=2, color=[255, 0, 0], thickness=2, lineType=cv2.LINE_AA)

    # 센터 평균 구한걸 다시 그려보기! 빨간점!
    cv2.circle(img, center=tuple((center_x, center_y)), radius=2, color=[0, 0, 255], thickness=2, lineType=cv2.LINE_AA)

    # cv2.imshow("img", img)
    cv2.imshow("result", result)
    cv2.waitKey(1)
