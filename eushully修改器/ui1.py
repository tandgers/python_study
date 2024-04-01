import sys

from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("untitled.ui")

window.show()

app.exec()