import sys
import io

from PyQt6 import uic, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton

from random import choice, random

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QWidget" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="button">
    <property name="geometry">
     <rect>
      <x>350</x>
      <y>410</y>
      <width>131</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>Тык</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.setWindowTitle('Рисование')
        self.button: QPushButton = self.button
        self.button.clicked.connect(self.paint_circle)
        self.paint = False

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.paint:
            qp = QPainter(self)
            qp.setBrush(Qt.GlobalColor.yellow)
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