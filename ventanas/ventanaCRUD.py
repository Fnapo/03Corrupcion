# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaCRUD.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ventanaCrud(object):
    def setupUi(self, ventanaCrud):
        ventanaCrud.setObjectName("ventanaCrud")
        ventanaCrud.resize(480, 300)
        ventanaCrud.setMinimumSize(QtCore.QSize(480, 300))
        ventanaCrud.setMaximumSize(QtCore.QSize(480, 300))
        self.gridLayout = QtWidgets.QGridLayout(ventanaCrud)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.crearRegistro = QtWidgets.QPushButton(ventanaCrud)
        self.crearRegistro.setMinimumSize(QtCore.QSize(250, 40))
        self.crearRegistro.setMaximumSize(QtCore.QSize(250, 40))
        self.crearRegistro.setSizeIncrement(QtCore.QSize(4, 4))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.crearRegistro.setFont(font)
        self.crearRegistro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.crearRegistro.setObjectName("crearRegistro")
        self.horizontalLayout.addWidget(self.crearRegistro)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.editarRegistro = QtWidgets.QPushButton(ventanaCrud)
        self.editarRegistro.setMinimumSize(QtCore.QSize(250, 40))
        self.editarRegistro.setMaximumSize(QtCore.QSize(250, 40))
        self.editarRegistro.setSizeIncrement(QtCore.QSize(4, 4))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.editarRegistro.setFont(font)
        self.editarRegistro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editarRegistro.setObjectName("editarRegistro")
        self.horizontalLayout_2.addWidget(self.editarRegistro)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verRegistro = QtWidgets.QPushButton(ventanaCrud)
        self.verRegistro.setMinimumSize(QtCore.QSize(250, 40))
        self.verRegistro.setMaximumSize(QtCore.QSize(250, 40))
        self.verRegistro.setSizeIncrement(QtCore.QSize(4, 4))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.verRegistro.setFont(font)
        self.verRegistro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verRegistro.setObjectName("verRegistro")
        self.horizontalLayout_3.addWidget(self.verRegistro)
        spacerItem5 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.borrarRegistro = QtWidgets.QPushButton(ventanaCrud)
        self.borrarRegistro.setMinimumSize(QtCore.QSize(250, 40))
        self.borrarRegistro.setMaximumSize(QtCore.QSize(250, 40))
        self.borrarRegistro.setSizeIncrement(QtCore.QSize(4, 4))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.borrarRegistro.setFont(font)
        self.borrarRegistro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.borrarRegistro.setObjectName("borrarRegistro")
        self.horizontalLayout_4.addWidget(self.borrarRegistro)
        spacerItem7 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem8 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.cancelar = QtWidgets.QPushButton(ventanaCrud)
        self.cancelar.setMinimumSize(QtCore.QSize(250, 40))
        self.cancelar.setMaximumSize(QtCore.QSize(250, 40))
        self.cancelar.setSizeIncrement(QtCore.QSize(4, 4))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelar.setFont(font)
        self.cancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelar.setObjectName("cancelar")
        self.horizontalLayout_5.addWidget(self.cancelar)
        spacerItem9 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)

        self.retranslateUi(ventanaCrud)
        QtCore.QMetaObject.connectSlotsByName(ventanaCrud)

    def retranslateUi(self, ventanaCrud):
        _translate = QtCore.QCoreApplication.translate
        ventanaCrud.setWindowTitle(_translate("ventanaCrud", "Dialog"))
        self.crearRegistro.setText(_translate("ventanaCrud", "Crear un Registro Registro"))
        self.editarRegistro.setText(_translate("ventanaCrud", "Editar un Registro Registro"))
        self.verRegistro.setText(_translate("ventanaCrud", "Ver un Registro Registro"))
        self.borrarRegistro.setText(_translate("ventanaCrud", "Borrar un Registro Registro"))
        self.cancelar.setText(_translate("ventanaCrud", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventanaCrud = QtWidgets.QDialog()
    ui = Ui_ventanaCrud()
    ui.setupUi(ventanaCrud)
    ventanaCrud.show()
    sys.exit(app.exec_())

