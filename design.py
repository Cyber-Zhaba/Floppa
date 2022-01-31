import os
import api

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore


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
        self.pt_coords = None
        self.initUI()

    def initUI(self):
        self.Update()
        self.Backb.clicked.connect(self.reset_address)

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
        self.image_name = api.getImage(self.size_map, self.coords, self.z_scale, self.map_type,
                                       self.pt_coords)
        self.pixmap = QPixmap(self.image_name)
        self.map.setPixmap(self.pixmap)
        self.laymap.currentIndexChanged.connect(self.TypeMapChanger)
        self.Zooml.setText(f'Zoom: {int(self.z_scale / 9 * 100)}%')
        self.Coordsl.setText(f'Coords: {self.coords}')

    def keyPressEvent(self, event):
        # zoom
        if event.key() == QtCore.Qt.Key_PageUp:
            self.z_scale = min(17, self.z_scale + 1)
        if event.key() == QtCore.Qt.Key_PageDown:
            self.z_scale -= min(1, self.z_scale - 1)

        self.Update()

        # moving
        coords = list(map(float, self.coords.split(',')))
        value = 0.06 / (self.z_scale / 17)
        if event.key() in [Qt.Key_Up, Qt.Key_W]:
            coords[1] += value
        if event.key() in [Qt.Key_Left, Qt.Key_A]:
            coords[0] -= value
        if event.key() in [Qt.Key_Down, Qt.Key_S]:
            coords[1] -= value
        if event.key() in [Qt.Key_Right, Qt.Key_D]:
            coords[0] += value

        self.coords = f'{str(coords[0])[:6]},{str(coords[1])[:6]}'
        self.Update()

    def reset_address(self):
        self.pt_coords = None
        self.Addressl.text = 'Address:'

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.image_name)
