# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crypto.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 450)
        MainWindow.setMinimumSize(QtCore.QSize(380, 450))
        MainWindow.setMaximumSize(QtCore.QSize(380, 450))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(6, 253, 180, 40))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 381, 121))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(195, 253, 180, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(4, 354, 371, 91))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(21, 50, 131, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 131, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(250, 40, 51, 21))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(75)
        self.spinBox.setObjectName("spinBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(6, 303, 180, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(195, 303, 180, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(0, 125, 381, 121))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Шифр Цезаря"))
        self.pushButton.setText(_translate("MainWindow", "Конвертировать"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "Ваш оригинальный текст тут..."))
        self.pushButton_2.setText(_translate("MainWindow", "Очистить поля"))
        self.groupBox.setTitle(_translate("MainWindow", "Настройка метода шифрования               Смещение текста"))
        self.radioButton_2.setText(_translate("MainWindow", "Дешифровать"))
        self.radioButton.setText(_translate("MainWindow", "Зашифровать"))
        self.pushButton_3.setText(_translate("MainWindow", "Загрузить из файла"))
        self.pushButton_4.setText(_translate("MainWindow", "Сохранить в файл"))
        self.plainTextEdit_2.setPlaceholderText(_translate("MainWindow", "Ваш зашифрованный текст тут..."))