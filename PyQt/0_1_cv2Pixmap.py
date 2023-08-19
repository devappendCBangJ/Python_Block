import sys
import cv2
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap


class ImageViewer(QMainWindow):
    def __init__(self, image_path):
        super().__init__()

        # OpenCV로 이미지 불러오기
        self.image = cv2.imread(image_path)

        if self.image is None:
            raise ValueError("Could not open the image!")

        # OpenCV BGR 이미지를 RGB로 변환
        rgb_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

        # QImage로 변환
        height, width, channel = rgb_image.shape
        bytes_per_line = 3 * width
        q_image = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # QImage를 QPixmap으로 변환
        pixmap = QPixmap.fromImage(q_image)

        # QLabel 위젯에 이미지 표시
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)
        self.setWindowTitle('ImageViewer')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer('/media/hi/SK Gold P31/Capstone/GolfBall/Crawling_cp/golf ball in rough/golf ball in rough1_com.jpg')  # 이미지 경로를 변경하세요
    sys.exit(app.exec_())