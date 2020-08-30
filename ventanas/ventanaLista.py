# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaLista.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ventanaLista(object):
    def setupUi(self, ventanaLista):
        ventanaLista.setObjectName("ventanaLista")
        ventanaLista.resize(450, 200)
        ventanaLista.setMinimumSize(QtCore.QSize(450, 200))
        ventanaLista.setMaximumSize(QtCore.QSize(450, 200))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        ventanaLista.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(ventanaLista)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ventanaLista)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboLista = QtWidgets.QComboBox(ventanaLista)
        self.comboLista.setMinimumSize(QtCore.QSize(0, 30))
        self.comboLista.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboLista.setObjectName("comboLista")
        self.verticalLayout.addWidget(self.comboLista)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(61, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.botonAceptar = QtWidgets.QPushButton(ventanaLista)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botonAceptar.sizePolicy().hasHeightForWidth())
        self.botonAceptar.setSizePolicy(sizePolicy)
        self.botonAceptar.setMinimumSize(QtCore.QSize(150, 0))
        self.botonAceptar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonAceptar.setObjectName("botonAceptar")
        self.horizontalLayout.addWidget(self.botonAceptar)
        spacerItem1 = QtWidgets.QSpacerItem(61, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.botonCancelar = QtWidgets.QPushButton(ventanaLista)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botonCancelar.sizePolicy().hasHeightForWidth())
        self.botonCancelar.setSizePolicy(sizePolicy)
        self.botonCancelar.setMinimumSize(QtCore.QSize(150, 0))
        self.botonCancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonCancelar.setObjectName("botonCancelar")
        self.horizontalLayout.addWidget(self.botonCancelar)
        spacerItem2 = QtWidgets.QSpacerItem(61, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(ventanaLista)
        QtCore.QMetaObject.connectSlotsByName(ventanaLista)

    def retranslateUi(self, ventanaLista):
        _translate = QtCore.QCoreApplication.translate
        ventanaLista.setWindowTitle(_translate("ventanaLista", "Elegir un Registro"))
        self.label.setText(_translate("ventanaLista", "Selecciona un Registro"))
        self.botonAceptar.setText(_translate("ventanaLista", "Aceptar"))
        self.botonCancelar.setText(_translate("ventanaLista", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventanaLista = QtWidgets.QDialog()
    ui = Ui_ventanaLista()
    ui.setupUi(ventanaLista)
    ventanaLista.show()
    sys.exit(app.exec_())

