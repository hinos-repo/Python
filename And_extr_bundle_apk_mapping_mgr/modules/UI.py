# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bundleMgr.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(655, 582)
        Dialog.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 70, 80, 51))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.edProjectPath = QtWidgets.QLineEdit(Dialog)
        self.edProjectPath.setGeometry(QtCore.QRect(150, 80, 389, 31))
        self.edProjectPath.setMinimumSize(QtCore.QSize(0, 25))
        self.edProjectPath.setObjectName("edProjectPath")
        self.btnSearchDir = QtWidgets.QPushButton(Dialog)
        self.btnSearchDir.setGeometry(QtCore.QRect(550, 80, 91, 31))
        self.btnSearchDir.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btnSearchDir.setObjectName("btnSearchDir")
        self.cbProjectName = QtWidgets.QComboBox(Dialog)
        self.cbProjectName.setGeometry(QtCore.QRect(150, 140, 391, 31))
        self.cbProjectName.setObjectName("cbProjectName")
        self.edSavePath = QtWidgets.QLineEdit(Dialog)
        self.edSavePath.setEnabled(True)
        self.edSavePath.setGeometry(QtCore.QRect(150, 260, 391, 31))
        self.edSavePath.setMinimumSize(QtCore.QSize(0, 25))
        self.edSavePath.setObjectName("edSavePath")
        self.edVersion = QtWidgets.QLineEdit(Dialog)
        self.edVersion.setGeometry(QtCore.QRect(150, 320, 391, 31))
        self.edVersion.setMinimumSize(QtCore.QSize(0, 25))
        self.edVersion.setObjectName("edVersion")
        self.btnExtract = QtWidgets.QPushButton(Dialog)
        self.btnExtract.setGeometry(QtCore.QRect(60, 380, 499, 40))
        self.btnExtract.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btnExtract.setObjectName("btnExtract")
        self.cbCountry = QtWidgets.QComboBox(Dialog)
        self.cbCountry.setGeometry(QtCore.QRect(150, 200, 391, 31))
        self.cbCountry.setObjectName("cbCountry")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 130, 80, 51))
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 250, 80, 51))
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(40, 310, 80, 51))
        self.label_8.setMinimumSize(QtCore.QSize(0, 0))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(40, 190, 80, 51))
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(40, 10, 80, 51))
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.cbMode = QtWidgets.QComboBox(Dialog)
        self.cbMode.setGeometry(QtCore.QRect(150, 20, 391, 31))
        self.cbMode.setObjectName("cbMode")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "BundleMgr"))
        self.label.setText(_translate("Dialog", "프로젝트 경로"))
        self.btnSearchDir.setText(_translate("Dialog", "디렉토리 검색"))
        self.btnExtract.setText(_translate("Dialog", "파일 추출"))
        self.label_6.setText(_translate("Dialog", "프로젝트명"))
        self.label_7.setText(_translate("Dialog", "저장할 경로"))
        self.label_8.setText(_translate("Dialog", "버전"))
        self.label_9.setText(_translate("Dialog", "나라"))
        self.label_10.setText(_translate("Dialog", "모드"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

