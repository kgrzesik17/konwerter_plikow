from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def main():
    try:
        file1 = sys.argv[1]
        file2 = sys.argv[2]

        window(file1, file2)
        
    except IndexError:
        error_window(1)

    return 0


def clicked():
    print("button clicked")


def window(file1, file2):
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(800, 400, 500, 225)
    win.setWindowTitle("File converter")

    label1 = QtWidgets.QLabel(win)
    label1.setText("Hello, world!")
    label1.move(50, 50)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("click me")
    b1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())


def error_window(error_id):
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(800, 400, 500, 225)
    win.setWindowTitle("File converter")

    match error_id:
        case 1:
            error_message = "Error: no arguments found"
            error_solution = "You have to run the file from the command line and pass it 2 arguments."
            error_example = "Example: converter.exe [file.extension] [file.expected_extension]"
        case _:
            error_message = "Error: unknown error"

    error_message_label = QtWidgets.QLabel(win)
    error_message_label.setText(error_message)
    error_message_label.move(50, 50)
    error_message_label.adjustSize()

    
    error_solution_label = QtWidgets.QLabel(win)
    error_solution_label.setText(error_solution)
    error_solution_label.move(50, 100)
    error_solution_label.adjustSize()

    error_example_label = QtWidgets.QLabel(win)
    error_example_label.setText(error_example)
    error_example_label.move(50, 150)
    error_example_label.adjustSize()

    win.show()
    sys.exit(app.exec_())


main()