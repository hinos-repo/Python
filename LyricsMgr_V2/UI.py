# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_uiFiles/lyrics.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(445, 602)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.edTitle = QtWidgets.QLineEdit(Dialog)
        self.edTitle.setGeometry(QtCore.QRect(150, 30, 241, 31))
        self.edTitle.setObjectName("edTitle")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 81, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.edName = QtWidgets.QLineEdit(Dialog)
        self.edName.setGeometry(QtCore.QRect(150, 70, 241, 31))
        self.edName.setObjectName("edName")
        self.btnSearch1 = QtWidgets.QPushButton(Dialog)
        self.btnSearch1.setGeometry(QtCore.QRect(50, 122, 341, 31))
        self.btnSearch1.setObjectName("btnSearch1")
        self.tvLyrics = QtWidgets.QPlainTextEdit(Dialog)
        self.tvLyrics.setGeometry(QtCore.QRect(50, 270, 341, 211))
        self.tvLyrics.setObjectName("tvLyrics")
        self.cbBox = QtWidgets.QComboBox(Dialog)
        self.cbBox.setGeometry(QtCore.QRect(50, 170, 341, 31))
        self.cbBox.setCurrentText("")
        self.cbBox.setMaxVisibleItems(50)
        self.cbBox.setObjectName("cbBox")
        self.btnSearch2 = QtWidgets.QPushButton(Dialog)
        self.btnSearch2.setGeometry(QtCore.QRect(50, 220, 341, 31))
        self.btnSearch2.setObjectName("btnSearch2")
        self.edPath = QtWidgets.QLineEdit(Dialog)
        self.edPath.setGeometry(QtCore.QRect(150, 510, 241, 31))
        self.edPath.setObjectName("edPath")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 510, 81, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.btnExtract = QtWidgets.QPushButton(Dialog)
        self.btnExtract.setGeometry(QtCore.QRect(50, 560, 341, 31))
        self.btnExtract.setObjectName("btnExtract")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LyricsMgr"))
        self.label.setText(_translate("Dialog", "노래 제목"))
        self.label_2.setText(_translate("Dialog", "가수 이름"))
        self.btnSearch1.setText(_translate("Dialog", "가수 검색"))
        self.btnSearch2.setText(_translate("Dialog", "가사 검색"))
        self.label_3.setText(_translate("Dialog", "저장경로"))
        self.btnExtract.setText(_translate("Dialog", "가사 추출"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
