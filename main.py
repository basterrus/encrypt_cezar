import os, sys
from PyQt5 import QtWidgets, QtGui, QtCore
from des import *
from datetime import datetime

alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890'
# alphabetEng = 'ABCDEFGHIGKLMNOPQRSTUVYXWZabcdefghigklmnopqrstuvyxwz1234567890'
max_key_size = len(alphabet)


class Crypto(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.encrypt)
        self.ui.pushButton_2.clicked.connect(self.clear_all)
        self.ui.pushButton_3.clicked.connect(self.open_file)
        self.ui.pushButton_4.clicked.connect(self.save_file)

    def encrypt(self):
        text = self.ui.plainTextEdit.toPlainText()
        key = self.ui.spinBox.value()
        result = ''

        if self.ui.radioButton.isChecked():
            key = key
        elif self.ui.radioButton_2.isChecked():
            key = -key
        else:
            QtWidgets.QMessageBox.information(self, 'Ошибка!', 'Пожалуйста выберите нужное действие')

        for symbol in text:
            index = alphabet.find(symbol)

            if index == -1:
                result += symbol
            else:
                index += key

                if index >= max_key_size:
                    index -= max_key_size
                elif index <= 0:
                    index += max_key_size

                result += alphabet[index]

        self.ui.plainTextEdit_2.setPlainText(result)

    def clear_all(self):

        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.spinBox.setValue(1)
        result = ''

    def open_file(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Открыть файл...', '', 'Текстовый файл *.txt')
        with open(path, 'r', encoding='utf-8') as r:
            rawtext = r.read()
            self.path = sys.path
            self.ui.plainTextEdit.setPlainText(rawtext)
            self.setWindowTitle(f'{os.path.basename(path) if self.path else "Untitled"}')

    def save_file(self):
        result = self.ui.plainTextEdit_2.toPlainText()
        with open('translated.txt', 'a', encoding='utf-8') as f:
            if result:
                f.write(f'{datetime.now()}\n{result}\n\f')
                QtWidgets.QMessageBox.information(self, 'Файл сохранен!', 'Файл сохранен в translated.txt!')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = Crypto()
    myapp.show()
    sys.exit(app.exec_())
