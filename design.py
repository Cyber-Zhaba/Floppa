import os
import api

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("design.ui", self)
        self.pixmap = None
        self.image = None
        self.coords = '37.530887,55.703118'
        self.setWindowTitle('Map api')
        self.initUI()

    def initUI(self):
        size = f'{self.map.size().width()},{self.map.size().height()}'
        self.pixmap = QPixmap(api.getImage(size, self.coords))
        self.map.setPixmap(self.pixmap)

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
