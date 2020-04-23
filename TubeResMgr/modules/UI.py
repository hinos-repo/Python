# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TubeResMgr.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(610, 458)
        Dialog.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 40, 511, 301))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(35)
        self.formLayout.setObjectName("formLayout")
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.edSavePath = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.edSavePath.setEnabled(True)
        self.edSavePath.setMinimumSize(QtCore.QSize(0, 25))
        self.edSavePath.setObjectName("edSavePath")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edSavePath)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_13.setMinimumSize(QtCore.QSize(0, 0))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.edIconPath = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.edIconPath.setEnabled(True)
        self.edIconPath.setMinimumSize(QtCore.QSize(0, 25))
        self.edIconPath.setObjectName("edIconPath")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.edIconPath)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_12.setMinimumSize(QtCore.QSize(0, 0))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.edSplashPath = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.edSplashPath.setEnabled(True)
        self.edSplashPath.setMinimumSize(QtCore.QSize(0, 25))
        self.edSplashPath.setObjectName("edSplashPath")
        self.horizontalLayout_4.addWidget(self.edSplashPath)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.edGooglePath = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.edGooglePath.setEnabled(True)
        self.edGooglePath.setMinimumSize(QtCore.QSize(0, 25))
        self.edGooglePath.setObjectName("edGooglePath")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.edGooglePath)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_14.setMinimumSize(QtCore.QSize(0, 0))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.edStringPath = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.edStringPath.setEnabled(True)
        self.edStringPath.setMinimumSize(QtCore.QSize(0, 25))
        self.edStringPath.setObjectName("edStringPath")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.edStringPath)
        self.btnOK = QtWidgets.QPushButton(Dialog)
        self.btnOK.setGeometry(QtCore.QRect(130, 370, 341, 31))
        self.btnOK.setObjectName("btnOK")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TubeResMgr"))
        self.label_9.setText(_translate("Dialog", "저장할 경로"))
        self.label_13.setText(_translate("Dialog", "아이콘 이미지 경로"))
        self.label_12.setText(_translate("Dialog", "스플래쉬 경로"))
        self.label_11.setText(_translate("Dialog", "구글 서비스 경로"))
        self.label_14.setText(_translate("Dialog", "스트링 경로"))
        self.btnOK.setText(_translate("Dialog", "Res만들기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
