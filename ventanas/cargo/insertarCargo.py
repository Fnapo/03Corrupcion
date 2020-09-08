# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insertarCargo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_insertarCargo(object):
    def setupUi(self, insertarCargo):
        insertarCargo.setObjectName("insertarCargo")
        insertarCargo.resize(500, 150)
        insertarCargo.setMinimumSize(QtCore.QSize(500, 150))
        insertarCargo.setMaximumSize(QtCore.QSize(500, 150))
        font = QtGui.QFont()
        font.setPointSize(14)
        insertarCargo.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(insertarCargo)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(insertarCargo)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.inputCargo = QtWidgets.QLineEdit(insertarCargo)
        self.inputCargo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inputCargo.setObjectName("inputCargo")
        self.horizontalLayout.addWidget(self.inputCargo)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.botonAceptar = QtWidgets.QPushButton(insertarCargo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botonAceptar.sizePolicy().hasHeightForWidth())
        self.botonAceptar.setSizePolicy(sizePolicy)
        self.botonAceptar.setMinimumSize(QtCore.QSize(150, 40))
        self.botonAceptar.setMaximumSize(QtCore.QSize(150, 40))
        self.botonAceptar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonAceptar.setObjectName("botonAceptar")
        self.horizontalLayout_2.addWidget(self.botonAceptar)
        self.botonCancelar = QtWidgets.QPushButton(insertarCargo)
        self.botonCancelar.setMinimumSize(QtCore.QSize(100, 40))
        self.botonCancelar.setMaximumSize(QtCore.QSize(100, 40))
        self.botonCancelar.setObjectName("botonCancelar")
        self.horizontalLayout_2.addWidget(self.botonCancelar)
        self.botonResetear = QtWidgets.QPushButton(insertarCargo)
        self.botonResetear.setMinimumSize(QtCore.QSize(150, 40))
        self.botonResetear.setMaximumSize(QtCore.QSize(150, 40))
        self.botonResetear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonResetear.setObjectName("botonResetear")
        self.horizontalLayout_2.addWidget(self.botonResetear)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.retranslateUi(insertarCargo)
        QtCore.QMetaObject.connectSlotsByName(insertarCargo)

    def retranslateUi(self, insertarCargo):
        _translate = QtCore.QCoreApplication.translate
        insertarCargo.setWindowTitle(_translate("insertarCargo", "Insertar un Cargo"))
        self.label.setText(_translate("insertarCargo", "Cargo en el Partido"))
        self.botonAceptar.setText(_translate("insertarCargo", "Insertar Cargo"))
        self.botonCancelar.setText(_translate("insertarCargo", "Cancelar"))
        self.botonResetear.setText(_translate("insertarCargo", "Resetear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    insertarCargo = QtWidgets.QDialog()
    ui = Ui_insertarCargo()
    ui.setupUi(insertarCargo)
    insertarCargo.show()
    sys.exit(app.exec_())

