import design
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = design.MainWindow()
    ex.show()
    sys.exit(app.exec())
