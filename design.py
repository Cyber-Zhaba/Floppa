import os
import api

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("design.ui", self)
        self.pixmap = None
        self.image = None
        self.coords = '37.530,55.703'
        self.setWindowTitle('Map api')
        self.map_type = 'map'
        self.image_name = None
        self.size_map = f'{self.map.size().width()},{self.map.size().height()}'
        self.z_scale = 9
        self.initUI()

    def initUI(self):
        self.Update()

    def TypeMapChanger(self):
        self.map_type = self.laymap.currentText()
        if self.map_type == 'Satellite':
            self.map_type = 'sat'
        elif self.map_type == 'Scheme':
            self.map_type = 'map'
        else:
            self.map_type = 'skl'
        self.Update()

    def Update(self):
        self.image_name = api.getImage(self.size_map, self.coords, 9, self.map_type)
        self.pixmap = QPixmap(self.image_name)
        self.map.setPixmap(self.pixmap)
        self.laymap.currentIndexChanged.connect(self.TypeMapChanger)
        self.Zooml.setText(f'Zoom: {self.z_scale / 9 * 100}%')
        self.Coordsl.setText(f'Coords: {self.coords}')

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.image_name)
