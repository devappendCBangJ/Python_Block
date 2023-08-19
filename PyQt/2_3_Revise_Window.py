import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My GUI Program")
        self.setGeometry(100, 100, 300, 200)
        self.resize(600, 800)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()