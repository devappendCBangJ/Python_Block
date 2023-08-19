import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        btn = QPushButton('실행', self)
        btn.resize(120, 30)
        btn.move(10, 10)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()