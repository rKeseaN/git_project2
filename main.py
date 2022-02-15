from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        