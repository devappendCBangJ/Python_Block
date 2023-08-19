import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)    # QApplication 객체 생성
window = QWidget()              # QWidget 객체 생성
window.show()                   # show 메서드 호출
app.exec_()                     # 이벤트 루프 시작