# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaInicial.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ventanaInicial(object):
    def setupUi(self, ventanaInicial):
        ventanaInicial.setObjectName("ventanaInicial")
        ventanaInicial.resize(400, 330)
        ventanaInicial.setMinimumSize(QtCore.QSize(400, 330))
        ventanaInicial.setMaximumSize(QtCore.QSize(400, 330))
        font = QtGui.QFont()
        font.setPointSize(14)
        ventanaInicial.setFont(font)
        self.gridLayout_2 = QtWidgets.QGridLayout(ventanaInicial)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(ventanaInicial)
        self.groupBox.setMinimumSize(QtCore.QSize(380, 250))
        self.groupBox.setMaximumSize(QtCore.QSize(380, 250))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.botonCasos = QtWidgets.QPushButton(self.groupBox)
        self.botonCasos.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.botonCasos.setFont(font)
        self.botonCasos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonCasos.setAutoFillBackground(False)
        self.botonCasos.setStyleSheet(":hover{\n"
"background-color: rgb(172, 172, 172);\n"
"}")
        self.botonCasos.setObjectName("botonCasos")
        self.gridLayout.addWidget(self.botonCasos, 0, 0, 1, 1)
        self.botonImputados = QtWidgets.QPushButton(self.groupBox)
        self.botonImputados.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.botonImputados.setFont(font)
        self.botonImputados.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonImputados.setAutoFillBackground(False)
        self.botonImputados.setStyleSheet(":hover{\n"
"background-color: rgb(172, 172, 172);\n"
"}")
        self.botonImputados.setObjectName("botonImputados")
        self.gridLayout.addWidget(self.botonImputados, 1, 0, 1, 1)
        self.botonCargos = QtWidgets.QPushButton(self.groupBox)
        self.botonCargos.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.botonCargos.setFont(font)
        self.botonCargos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonCargos.setAutoFillBackground(False)
        self.botonCargos.setStyleSheet(":hover{\n"
"background-color: rgb(172, 172, 172);\n"
"}")
        self.botonCargos.setObjectName("botonCargos")
        self.gridLayout.addWidget(self.botonCargos, 2, 0, 1, 1)
        self.botonPartidos = QtWidgets.QPushButton(self.groupBox)
        self.botonPartidos.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.botonPartidos.setFont(font)
        self.botonPartidos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonPartidos.setAutoFillBackground(False)
        self.botonPartidos.setStyleSheet(":hover{\n"
"background-color: rgb(172, 172, 172);\n"
"}")
        self.botonPartidos.setObjectName("botonPartidos")
        self.gridLayout.addWidget(self.botonPartidos, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.botonCancelar = QtWidgets.QPushButton(ventanaInicial)
        self.botonCancelar.setMinimumSize(QtCore.QSize(200, 40))
        self.botonCancelar.setObjectName("botonCancelar")
        self.horizontalLayout.addWidget(self.botonCancelar)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(ventanaInicial)
        QtCore.QMetaObject.connectSlotsByName(ventanaInicial)

    def retranslateUi(self, ventanaInicial):
        _translate = QtCore.QCoreApplication.translate
        ventanaInicial.setWindowTitle(_translate("ventanaInicial", "Ventana Inicial"))
        self.groupBox.setTitle(_translate("ventanaInicial", "Elige La Entidad"))
        self.botonCasos.setText(_translate("ventanaInicial", "Casos Jurídicos"))
        self.botonImputados.setText(_translate("ventanaInicial", "Imputados Políticos"))
        self.botonCargos.setText(_translate("ventanaInicial", "Cargos Políticos"))
        self.botonPartidos.setText(_translate("ventanaInicial", "Partidos Políticos"))
        self.botonCancelar.setText(_translate("ventanaInicial", "Cerrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventanaInicial = QtWidgets.QDialog()
    ui = Ui_ventanaInicial()
    ui.setupUi(ventanaInicial)
    ventanaInicial.show()
    sys.exit(app.exec_())

