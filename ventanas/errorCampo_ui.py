# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'errorCampo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_errorCampo(object):
    def setupUi(self, errorCampo):
        errorCampo.setObjectName("errorCampo")
        errorCampo.setWindowModality(QtCore.Qt.ApplicationModal)
        errorCampo.resize(400, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(errorCampo.sizePolicy().hasHeightForWidth())
        errorCampo.setSizePolicy(sizePolicy)
        errorCampo.setMinimumSize(QtCore.QSize(400, 250))
        errorCampo.setMaximumSize(QtCore.QSize(400, 250))
        font = QtGui.QFont()
        font.setPointSize(13)
        errorCampo.setFont(font)
        errorCampo.setAutoFillBackground(False)
        errorCampo.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(errorCampo)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(42, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label01 = QtWidgets.QLabel(errorCampo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label01.sizePolicy().hasHeightForWidth())
        self.label01.setSizePolicy(sizePolicy)
        self.label01.setMinimumSize(QtCore.QSize(280, 120))
        self.label01.setMaximumSize(QtCore.QSize(280, 120))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label01.setFont(font)
        self.label01.setAutoFillBackground(False)
        self.label01.setStyleSheet("background-color:rgb(181, 121, 0);\n"
"border-color: rgb(255, 0, 0);\n"
"border: 5 solid rgb(255, 0, 0);\n"
"color: rgb(217, 217, 217);\n"
"padding: 5;")
        self.label01.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label01.setLineWidth(5)
        self.label01.setAlignment(QtCore.Qt.AlignCenter)
        self.label01.setWordWrap(True)
        self.label01.setObjectName("label01")
        self.gridLayout.addWidget(self.label01, 0, 1, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(42, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(117, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 2)
        self.botonAceptar = QtWidgets.QPushButton(errorCampo)
        self.botonAceptar.setMinimumSize(QtCore.QSize(130, 60))
        self.botonAceptar.setMaximumSize(QtCore.QSize(130, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.botonAceptar.setFont(font)
        self.botonAceptar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonAceptar.setObjectName("botonAceptar")
        self.gridLayout.addWidget(self.botonAceptar, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(117, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 2)

        self.retranslateUi(errorCampo)
        QtCore.QMetaObject.connectSlotsByName(errorCampo)

    def retranslateUi(self, errorCampo):
        _translate = QtCore.QCoreApplication.translate
        errorCampo.setWindowTitle(_translate("errorCampo", "Error en un Campo"))
        self.label01.setText(_translate("errorCampo", "Error en el campo"))
        self.botonAceptar.setText(_translate("errorCampo", "Aceptar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    errorCampo = QtWidgets.QDialog()
    ui = Ui_errorCampo()
    ui.setupUi(errorCampo)
    errorCampo.show()
    sys.exit(app.exec_())

