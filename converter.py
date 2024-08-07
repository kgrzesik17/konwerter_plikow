from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
import sys
from pathlib import Path
import json
import xmltodict
import yaml
from dict2xml import dict2xml

def main():
    try:
        file1 = sys.argv[1]
        file2 = sys.argv[2]

        if Path(f'./{file1}.').is_file():
            print('ss')
        else:
            error_window(3)

        if Path(f'./{file2}.').is_file():
            error_window(4)

        if check_extension(file1) and check_extension(file2):
            window(file1, file2, check_extension(file1), check_extension(file2))
        else:
            error_window(2)
        
    except IndexError:
        error_window(1)

    return 0


def check_extension(file):
    supported = ['.xml', '.json', '.yml', '.yaml']

    for i in supported:
        if file.endswith(i):
            return i
    
    return False


def to_dict(file1, file2, file1_extension, file2_extension):
    file = open(file1, 'r')

    if file1_extension == '.json':
        data = json.loads(file.read())

    elif file1_extension == '.xml':
        data = xmltodict.parse(file.read())

    elif file1_extension == '.yml' or file1_extension == '.yaml':
        data = yaml.load(file, Loader=yaml.SafeLoader)

    to_file(data, file2, file2_extension)
    return False


def to_file(data, file2, file2_extension):
    file = open(file2, 'a')

    if file2_extension == '.json':
        content = json.dumps(data, indent=4)
        
    if file2_extension == '.xml':
        content = dict2xml(data)

    if file2_extension == '.yaml' or file2_extension == '.yml':
        content = yaml.dump(data, allow_unicode=True)

    file.write(content)
    file.close()



def window(file1, file2, file1_extension, file2_extension):
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(800, 400, 500, 250)
    win.setWindowTitle("File converter")

    label1 = QtWidgets.QLabel(win)
    label1.setText("Welcome to my file converter!")
    label1.move(50, 50)
    label1.adjustSize()

    file1_label = QtWidgets.QLabel(win)
    file1_label.setText(f"File found: {file1}")
    file1_label.move(50, 100)
    file1_label.adjustSize()

    file2_label = QtWidgets.QLabel(win)
    file2_label.setText(f"File after conversion: {file2}")
    file2_label.move(50, 150)
    file2_label.adjustSize()

    b1 = QtWidgets.QPushButton(win)
    b1.move(50, 200)
    b1.setText("Convert")
    b1.clicked.connect(partial(to_dict, file1, file2, file1_extension, file2_extension))

    win.show()
    sys.exit(app.exec_())


def error_window(error_id):
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(800, 400, 500, 225)
    win.setWindowTitle("File converter")

    match error_id:
        case 1:
            error_message = "Error 1: No arguments found"
            error_description = "You have to run the file from the command line and pass it 2 arguments."
            error_example = "Example: converter.exe [file.extension] [file.expected_extension]"
        case 2:
            error_message = "Error 2: Extension not supported"
            error_description = "You can only pass files that match the supported extensions"
            error_example = "Supported extensions: .xml, .json, .yml, .yaml"
        case 3:
            error_message = "Error 3: File not found"
            error_description = "Make sure you opened the program in the right path."
            error_example = ""
        case 4:
            error_message = "Error 4: File exists"
            error_description = "File you wanted to create already exsists"
            error_example = "Make sure to delete it before attempting to convert"

        case _:
            error_message = "An unknown error occured"
            error_description = "No description available."
            error_example = "No example available."

    error_message_label = QtWidgets.QLabel(win)
    error_message_label.setText(error_message)
    error_message_label.move(50, 50)
    error_message_label.adjustSize()
    
    error_description_label = QtWidgets.QLabel(win)
    error_description_label.setText(error_description)
    error_description_label.move(50, 100)
    error_description_label.adjustSize()

    error_example_label = QtWidgets.QLabel(win)
    error_example_label.setText(error_example)
    error_example_label.move(50, 150)
    error_example_label.adjustSize()

    win.show()
    sys.exit(app.exec_())


main()