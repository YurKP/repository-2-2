import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

from PyQt6.QtGui import QPainter, QColor
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        r = randint(10, 100)
        r2 = randint(10, 200)
        r3 = randint(10, 200)
        r4 = randint(10, 100)

        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(100, 100, r, r)

        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(500, 100, r2, r2)

        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(100, 300, r3, r3)

        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(500, 400, r4, r4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())