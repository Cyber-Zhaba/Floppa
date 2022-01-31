import os
import api

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("design.ui", self)
        self.pixmap = None
        self.image = None
        self.coords = '37.530887,55.703118'
        self.setWindowTitle('Map api')
        self.image_name = None
        self.initUI()

    def initUI(self):
        size = f'{self.map.size().width()},{self.map.size().height()}'
        self.image_name = api.getImage(size, self.coords)
        self.pixmap = QPixmap(self.image_name)
        self.map.setPixmap(self.pixmap)

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.image_name)
