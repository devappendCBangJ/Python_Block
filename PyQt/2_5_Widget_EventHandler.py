"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

def btn_slot():
    print("실행 버튼 클릭")

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        btn = QPushButton('실행', self)
        btn.resize(120, 30)
        btn.move(10, 10)

        btn.clicked.connect(btn_slot)   # clicked 시그널과 btn_slot 함수 연결

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        btn = QPushButton('실행', self)
        btn.resize(120, 30)
        btn.move(10, 10)

        btn.clicked.connect(self.btn_slot)   # clicked 시그널과 btn_slot 함수 연결

    def btn_slot(self):
        print("실행 버튼 클릭")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()