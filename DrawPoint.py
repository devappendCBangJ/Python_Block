# ==============================================================
# 0. 라이브러리 불러오기
# ==============================================================
import cv2

# ==============================================================
# 0. 함수 정의
# ==============================================================
def onMouse(event, x, y, flags, param):
    # print(event, x, y, flags)
    if event == cv2.EVENT_LBUTTONDOWN:
        # 컨트롤 & 쉬프트 키를 같이 누른상태로 마우스 왼쪽버튼을 누른경우
        if flags & cv2.EVENT_FLAG_CTRLKEY and flags & cv2.EVENT_FLAG_SHIFTKEY:
            color = colors['green']

        # 쉬프트 키를 누르고 마우스를 누른상태로 마우스 왼쪽버튼을 누른경우
        elif flags & cv2.EVENT_FLAG_SHIFTKEY:
            color = colors['red']
            # 바운딩 박스

        # 컨트롤 키를 누르고 마우스를 누른상태로 마우스 왼쪽버튼을 누른경우
        elif flags & cv2.EVENT_FLAG_CTRLKEY:
            color = colors['red']
            out_coor.append([x, y])
            print(f"out_coor : {out_coor}")

        # 그 외 마우스 왼쪽버튼을 누른경우
        else:
            color = colors['blue']
            in_coor.append([x, y])
            print(f"in_coor : {in_coor}")

        # 지름 3크기의 흰색원을 해당 좌표에 그림
        radius = 3
        cv2.circle(img, (x, y), radius, color, -1)
        cv2.imshow(title, img)

# ==============================================================
# 1. DrawPoint
# ==============================================================
events = [i for i in dir(cv2) if 'EVENT' in i]
print(f"events : {events}")

title = 'mouse event'
img = cv2.imread('/media/hi/SK Gold P31/Capstone/GolfBall/Golfball_Near_Remove_Similar_FixLabel_Remove_BboxInBbox_Remove_ErrorBboxRatio/images/train/75_jpg.rf.1ec1bc4018bb4602f9ef307c96a70ccb.jpg')
cv2.imshow(title, img)

in_coor = []
out_coor = []

colors = {'white': (255, 255, 255),
          'red': (0, 0, 255),
          'blue': (255, 0, 0),
          'green': (0, 255, 0)}

cv2.setMouseCallback(title, onMouse)

while True:
    if cv2.waitKey(0) & 0xFF == 27:
        break
cv2.destroyAllWindows()
