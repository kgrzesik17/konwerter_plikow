from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def clicked():
    print("test")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(800, 400, 300, 300)
    win.setWindowTitle("Konwerter")

    label = QtWidgets.QLabel(win)
    label.setText("My first label")
    label.move(50, 50)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("przycisk")
    b1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())

window()