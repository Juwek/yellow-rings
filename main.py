import sys
import io

from PyQt6 import uic, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton

from random import choice, random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 800, 600)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Рисование')
        ui = Ui(self)


class Ui(QWidget):
    def __init__(self, window):
        super().__init__(window)
        self.button = QPushButton('Тык', self)
        self.button.move(350, 400)
        self.button.resize(100, 40)
        self.button.clicked.connect(self.paint_circle)
        self.paint = False

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.paint:
            qp = QPainter(self)
            r, g, b = choice(range(256)), choice(range(256)), choice(range(256))
            qp.setBrush(QColor(r, g, b))
            x = choice(range(801))
            y = choice(range(601))
            d = choice(range(301))
            qp.drawEllipse(x, y, d, d)
        self.paint = False

    def paint_circle(self):
        self.paint = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())