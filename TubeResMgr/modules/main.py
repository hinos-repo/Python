# -*- coding: utf-8 -*-
import sys, UI
import os
from PyQt5.QtWidgets import *

from pathlib import Path
from PIL import Image
import shutil

DEBURG = True

EXTENSION_JSON = ".json"
EXTENSION_XML = ".xml"
EXTENSION_PNG = ".png"

DIR_RES = "res"
DIR_DRAWABLE = "drawable-xhdpi"
DIR_MIPMAP_HDPI = "mipmap-hdpi"
DIR_MIPMAP_XHDPI = "mipmap-xhdpi"
DIR_MIPMAP_XXHDPI = "mipmap-xxhdpi"
DIR_MIPMAP_XXXHDPI = "mipmap-xxxhdpi"
DIR_VALUES = "values"

FILE_DEFAULT_GOOGLE_SERVICE_NAME = "google-services" + EXTENSION_JSON
FILE_DEFAULT_ICON_NAME = "ic_launcher" + EXTENSION_PNG
FILE_DEFAULT_SPLASH_NAME = "yk_splash" + EXTENSION_PNG
FILE_DEFAULT_STRING_NAME = "strings" + EXTENSION_XML

ICON_SIZE = [72, 96, 144, 192]

class MainDialog(QDialog, UI.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self, None)
        self.setupUi(self)
        if DEBURG:
            self.edSavePath.setText("C:\workspace\GitProject\DO\_Res\DO000_Player")
            self.edIconPath.setText("D:\org\DO000_Player\launcher.png")
            self.edSplashPath.setText("D:\org\DO000_Player\splash.png")
            self.edGooglePath.setText("C:\workspace\GitProject\DO\_Res\DO000_Player\google-services.json")
            self.edStringPath.setText("C:\\Users\ZeroSoft\Desktop\DNStringFactory\strings.xml")

        self.btnOK.clicked.connect(self.makeRes)

    def makeRes(self):
        strSavePath = self.edSavePath.text()  # 저장경로
        strIconPath = self.edIconPath.text()  # 아이콘경로
        strSplashPath = self.edSplashPath.text()  # 스플래쉬경로
        strGooglePath = self.edGooglePath.text()  # 구글서비스 경로
        strStringPath = self.edStringPath.text()  # 스트링 경로

        if not self.CheckPath(strSavePath, ""):
            self.ShowErrorDlg(strSavePath + "경로를 확인해주세요.")
            return

        if not self.CheckPath(strIconPath, EXTENSION_PNG):
            self.ShowErrorDlg(strIconPath + "확장자와 경로를 확인해주세요. (지원 확장자" + EXTENSION_PNG + ")")
            print(strIconPath)
            return

        if not self.PassParam(strSplashPath):
            if not self.CheckPath(strSplashPath, EXTENSION_PNG):
                self.ShowErrorDlg(strSplashPath + "확장자와 경로를 확인해주세요. (지원 확장자" + EXTENSION_PNG + ")")
                return

        if not self.PassParam(strGooglePath):
            if not self.CheckPath(strGooglePath, EXTENSION_JSON):
                self.ShowErrorDlg(strGooglePath + "확장자와 경로를 확인해주세요. (지원 확장자" + EXTENSION_JSON + ")")
                return

        if not self.PassParam(strStringPath):
            if not self.CheckPath(strStringPath, EXTENSION_XML):
                self.ShowErrorDlg(strStringPath + "확장자와 경로를 확인해주세요. (지원 확장자" + EXTENSION_XML + ")")
                return

        strResDir = strSavePath + "/" + DIR_RES #D:\TEST\res
        bResult = self.MakeDir(strResDir)
        if not bResult:
            self.ShowErrorDlg(strResDir + "디렉토리 만들기 실패")
            return

        if not self.PassParam(strGooglePath):
            bResult = shutil.copy(strGooglePath, strSavePath + "/" + FILE_DEFAULT_GOOGLE_SERVICE_NAME)
            if not bResult:
                self.ShowErrorDlg(FILE_DEFAULT_GOOGLE_SERVICE_NAME + "복사 실패")
                return

        arrMipPath = []

        str_Mip_HDPI_Dir = strResDir + "/" + DIR_MIPMAP_HDPI
        arrMipPath.append(str_Mip_HDPI_Dir)
        bResult = self.MakeDir(str_Mip_HDPI_Dir)
        if not bResult:
            self.ShowErrorDlg(str_Mip_HDPI_Dir + "디렉토리 만들기 실패")
            return

        str_Mip_XHDPI_Dir = strResDir + "/" + DIR_MIPMAP_XHDPI
        arrMipPath.append(str_Mip_XHDPI_Dir)
        bResult = self.MakeDir(str_Mip_XHDPI_Dir)
        if not bResult:
            self.ShowErrorDlg(str_Mip_XHDPI_Dir + "디렉토리 만들기 실패")
            return

        str_Mip_XXHDPI_Dir = strResDir + "/" + DIR_MIPMAP_XXHDPI
        arrMipPath.append(str_Mip_XXHDPI_Dir)
        bResult = self.MakeDir(str_Mip_XXHDPI_Dir)
        if not bResult:
            self.ShowErrorDlg(str_Mip_XXHDPI_Dir + "디렉토리 만들기 실패")
            return

        str_Mip_XXXHDPI_Dir = strResDir + "/" + DIR_MIPMAP_XXXHDPI
        arrMipPath.append(str_Mip_XXXHDPI_Dir)
        bResult = self.MakeDir(str_Mip_XXXHDPI_Dir)
        if not bResult:
            self.ShowErrorDlg(str_Mip_XXXHDPI_Dir + "디렉토리 만들기 실패")
            return

        if not self.PassParam(strSplashPath):
            str_DRAWABLE_Dir = strResDir + "/" + DIR_DRAWABLE
            bResult = self.MakeDir(str_DRAWABLE_Dir)
            if not bResult:
                self.ShowErrorDlg(str_DRAWABLE_Dir + "디렉토리 만들기 실패")
                return

            bResult = shutil.copy(strSplashPath, str_DRAWABLE_Dir + "/" + FILE_DEFAULT_SPLASH_NAME)
            if not bResult:
                self.ShowErrorDlg(FILE_DEFAULT_SPLASH_NAME + "복사 실패")
                return

        if not self.PassParam(strStringPath) :
            str_VALUES_Dir = strResDir + "/" + DIR_VALUES
            bResult = self.MakeDir(str_VALUES_Dir)
            if not bResult:
                self.ShowErrorDlg(str_VALUES_Dir + "디렉토리 만들기 실패")
                return

            bResult = shutil.copy(strStringPath, str_VALUES_Dir + "/" + FILE_DEFAULT_STRING_NAME)
            if not bResult:
                self.ShowErrorDlg(FILE_DEFAULT_STRING_NAME + "복사 실패")
                return

        im = Image.open(strIconPath)
        nSize = im.size
        height = nSize[0]
        width = nSize[1]

        if not height == 512:
            self.ShowErrorDlg(strIconPath + "512 사이즈가 아닙니다.")
            return

        if not width == 512:
            self.ShowErrorDlg(strIconPath + "512 사이즈가 아닙니다.")
            return

        for idx, val in enumerate(ICON_SIZE, 0):
            im = Image.open(strIconPath)
            im.thumbnail([val, val], Image.ANTIALIAS)
            im.save(arrMipPath[idx] + "/" + FILE_DEFAULT_ICON_NAME, "PNG", quality=100)
            if not bResult:
                self.ShowErrorDlg(arrMipPath[idx] + "이미지 생성 실패")
                return
        self.ShowOKDlg("완료")


    def ShowErrorDlg(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.foregroundRole()
        msg.exec_()

    def ShowOKDlg(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("OK")
        msg.setInformativeText(message)
        msg.foregroundRole()
        msg.exec_()

    def CheckPath(self, path, extension):
        if extension == "":
            if Path(path).is_dir():
                return True
            else:
                return False

        if Path(path).is_file():
            if extension != "":
                name = Path(path).name.lower()
                result = name.find(extension)
                if result == -1:
                    return False
            return True
        else:
            return False

    def PassParam(self, path):
        if path == "3dh":
            return True
        else:
            return False

    def MakeDir(self, directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
            return True
        except:
            return False


# 기본적으로 프로그램을 실행시키는 역할
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

# 프로그램을 이벤트 루프로 진입시켜주는 코드
app.exec_()
