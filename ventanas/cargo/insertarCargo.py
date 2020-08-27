# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insertarCargo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 150)
        Dialog.setMinimumSize(QtCore.QSize(400, 150))
        Dialog.setMaximumSize(QtCore.QSize(400, 150))
        font = QtGui.QFont()
        font.setPointSize(14)
        Dialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.inputCargo = QtWidgets.QLineEdit(Dialog)
        self.inputCargo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inputCargo.setObjectName("inputCargo")
        self.horizontalLayout.addWidget(self.inputCargo)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.botonAceptar = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botonAceptar.sizePolicy().hasHeightForWidth())
        self.botonAceptar.setSizePolicy(sizePolicy)
        self.botonAceptar.setMinimumSize(QtCore.QSize(150, 30))
        self.botonAceptar.setMaximumSize(QtCore.QSize(150, 16777215))
        self.botonAceptar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonAceptar.setObjectName("botonAceptar")
        self.horizontalLayout_2.addWidget(self.botonAceptar)
        self.botonResetear = QtWidgets.QPushButton(Dialog)
        self.botonResetear.setMinimumSize(QtCore.QSize(150, 30))
        self.botonResetear.setMaximumSize(QtCore.QSize(150, 16777215))
        self.botonResetear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonResetear.setObjectName("botonResetear")
        self.horizontalLayout_2.addWidget(self.botonResetear)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Insertar un Cargo"))
        self.label.setText(_translate("Dialog", "Cargo en el Partido"))
        self.botonAceptar.setText(_translate("Dialog", "Insertar Cargo"))
        self.botonResetear.setText(_translate("Dialog", "Resetear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

