# 라이브러리 불러오기
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, QCheckBox
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
import os

base_path = '/media/hi/SK Gold P31/Capstone/GolfBall/Crawling_cp/golf ball in rough'

class ClickableImageLabel(QLabel):
    # 초기 세팅
    def __init__(self, pixmap, filepath):
        super().__init__()
        self.setPixmap(pixmap)
        self.filepath = filepath
        self.clicked_pos = None

    # 마우스 왼쪽 클릭 : 좌표 저장
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked_pos = event.pos()
            self.update()

    # 마우스 왼쪽 클릭 이후 : 점 그리기
    def paintEvent(self, event):
        super().paintEvent(event)
        if self.clicked_pos:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red, 5))
            painter.drawPoint(self.clicked_pos)

class ImageWindow(QWidget):
    # 초기 세팅
    def __init__(self, image_folder):
        super().__init__()

        self.image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
        self.current_image_index = 0

        self.initUI()

    def initUI(self):
        # 윈도우창 제목
        self.setWindowTitle('Label Bang')

        # 레이아웃 선언
        self.main_layout = QVBoxLayout() # 전체 틀 Plot
        self.grid_layout = QGridLayout() # 이미지 Plot
        self.button_layout = QHBoxLayout() # Button Plot

        # 이전 버튼 EventHandler
        self.prev_button = QPushButton('이전', self)
        self.prev_button.clicked.connect(self.loadPreviousImages)

        # 다음 버튼 EventHandler
        self.next_button = QPushButton('다음', self)
        self.next_button.clicked.connect(self.loadNextImages)

        # SAM 크기 설정 Checkbox
        self.small_check = QCheckBox("작음", self)
        self.medium_check = QCheckBox("중간", self)
        self.large_check = QCheckBox("큰", self)

        # 이미지 Plot Update
        self.updateImageGrid()

        # Button Layout 설정
        self.button_layout.addWidget(self.prev_button)
        self.button_layout.addWidget(self.next_button)

        # Main Layout 설정
        self.main_layout.addLayout(self.grid_layout)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addWidget(self.small_check)
        self.main_layout.addWidget(self.medium_check)
        self.main_layout.addWidget(self.large_check)

        # 최종 Layout 설정
        self.setLayout(self.main_layout)
        self.setFixedSize(1200, 900)

    # 다음 버튼 클릭 : 이미지 index 변경 + Plot Update
    def loadNextImages(self):
        self.current_image_index += 16
        if self.current_image_index >= len(self.image_files):
            self.current_image_index -= 16
        self.updateImageGrid()

    # 이전 버튼 클릭 : 이미지 index 변경 + Plot Update
    def loadPreviousImages(self):
        self.current_image_index -= 16
        if self.current_image_index < 0:
            self.current_image_index = 0
        self.updateImageGrid()

    def updateImageGrid(self):
        # 모든 이미지 Plot 제거
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            self.grid_layout.removeWidget(widget)
            widget.deleteLater()

        # 이미지 불러오기 + Resize + 클릭 좌표 & 파일명 추출 + Plot Update
        for i in range(4):
            for j in range(4):
                idx = self.current_image_index + i * 4 + j
                if idx < len(self.image_files):
                    pixmap = QPixmap(self.image_files[idx])
                    pixmap_scaled = pixmap.scaled(300, 300, Qt.KeepAspectRatio)
                    label = ClickableImageLabel(pixmap_scaled, self.image_files[idx])
                    label.mousePressEvent = lambda event, x=pixmap.width(), y=pixmap.height(), l=label: self.imageClicked(event, x, y, l)
                    self.grid_layout.addWidget(label, i, j)
                else:
                    break

        self.adjustSize()

    # 이미지 클릭 좌표 & 파일명 추출 + 클릭 좌표 저장
    def imageClicked(self, event, original_width, original_height, label):
        # 실제 사진 상에서의 마우스 위치 = (Scaled 마우스 위치) / (Scaled 전체 너비) * (실제 사진 너비)
        scaled_size = label.size()
        x_ratio = original_width / scaled_size.width()
        y_ratio = original_height / scaled_size.height()

        real_x = event.x() * x_ratio
        real_y = event.y() * y_ratio
        print(f"Image filepath: {label.filepath}")
        print(f"Actual image position: ({real_x}, {real_y})")

        label.clicked_pos = event.pos()
        label.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageWindow(base_path)
    window.show()
    sys.exit(app.exec_())