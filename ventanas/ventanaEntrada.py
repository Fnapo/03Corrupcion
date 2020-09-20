# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaEntrada.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaEntrada(object):
    def setupUi(self, VentanaEntrada):
        VentanaEntrada.setObjectName("VentanaEntrada")
        VentanaEntrada.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(14)
        VentanaEntrada.setFont(font)
        self.gridLayout_2 = QtWidgets.QGridLayout(VentanaEntrada)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(VentanaEntrada)
        self.groupBox.setMinimumSize(QtCore.QSize(350, 200))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setStyleSheet("font: 14pt \"Rockwell\";")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(250, 35))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.inputUsuario = QtWidgets.QLineEdit(self.groupBox)
        self.inputUsuario.setMinimumSize(QtCore.QSize(250, 35))
        self.inputUsuario.setObjectName("inputUsuario")
        self.gridLayout.addWidget(self.inputUsuario, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(250, 35))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.inputPassword = QtWidgets.QLineEdit(self.groupBox)
        self.inputPassword.setMinimumSize(QtCore.QSize(250, 35))
        self.inputPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassword.setObjectName("inputPassword")
        self.gridLayout.addWidget(self.inputPassword, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.botonAceptar = QtWidgets.QPushButton(VentanaEntrada)
        self.botonAceptar.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.botonAceptar.setFont(font)
        self.botonAceptar.setObjectName("botonAceptar")
        self.horizontalLayout.addWidget(self.botonAceptar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(VentanaEntrada)
        QtCore.QMetaObject.connectSlotsByName(VentanaEntrada)

    def retranslateUi(self, VentanaEntrada):
        _translate = QtCore.QCoreApplication.translate
        VentanaEntrada.setWindowTitle(_translate("VentanaEntrada", "Ventrada de Entrada de un Usuario"))
        self.groupBox.setTitle(_translate("VentanaEntrada", "Datos del Usuario"))
        self.label.setText(_translate("VentanaEntrada", "Nombre del Usuario"))
        self.label_2.setText(_translate("VentanaEntrada", "Password del Usuario"))
        self.botonAceptar.setText(_translate("VentanaEntrada", "Aceptar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaEntrada = QtWidgets.QDialog()
    ui = Ui_VentanaEntrada()
    ui.setupUi(VentanaEntrada)
    VentanaEntrada.show()
    sys.exit(app.exec_())

