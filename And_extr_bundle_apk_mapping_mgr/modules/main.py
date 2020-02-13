# -*- coding: utf-8 -*-
import sys, UI
import os
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from datetime import datetime
from pathlib import Path
import shutil
AND_BUNDLE_NAME = "app"
AND_MAPPING_NAME = "mapping"
AND_APK_NAME = "app-release"

AND_BUNDLE_EXTENSION = ".aab"
AND_MAPPING_EXTENSION = ".txt"
AND_APK_EXTENSION = ".apk"

AND_APK_PATH = "/app/release/" + AND_APK_NAME + AND_APK_EXTENSION
AND_BUNDLE_PATH = "/app/release/" + AND_BUNDLE_NAME + AND_BUNDLE_EXTENSION
AND_MAPPING_PATH = "/app/build/outputs/mapping/release/" + AND_MAPPING_NAME + AND_MAPPING_EXTENSION

DEBURG = False

arrCountry = ["ko", "jp"]
arrMode = ["Bundle + Mapping", "APK + Mapping", "Only Bundle", "Only APK"]

class MainDialog(QDialog, UI.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self, None)
        self.setupUi(self)
        if DEBURG:
            self.edProjectPath.setText("C:\workspace\GitProject\DM")
            self.edSavePath.setText("D:\DM")
            self.edVersion.setText("3")

        for mode in arrMode:
            self.cbMode.addItem(mode)

        for country in arrCountry:
            self.cbCountry.addItem(country)

        self.cbProjectName.addItem("프로젝트 경로 검색 ㄱㄱ")
        self.btnExtract.clicked.connect(self.ExtractLyric)
        self.btnSearchDir.clicked.connect(self.SearchDir)

    def ExtractLyric(self):
        nMode = self.cbMode.currentIndex()
        edProjectPath = self.edProjectPath.text().replace('\\', "/")
        edSavePath = self.edSavePath.text().replace("\\", "/")
        edVersion = self.edVersion.text()
        nProject = self.cbProjectName.currentIndex()

        if not edProjectPath:
            self.edProjectPath.setFocus()
            self.ShowErrorDlg("프로젝트 경로를 확인해주세요.")
            return
        if not edSavePath:
            self.edSavePath.setFocus()
            self.ShowErrorDlg("저장할 경로를 확인해주세요.")
            return
        if not edVersion:
            self.edVersion.setFocus()
            self.ShowErrorDlg("버전을 선택해주세요.")
            return
        if not edVersion:
            self.edVersion.setFocus()
            self.ShowErrorDlg("버전을 선택해주세요.")
            return
        if nProject == 0:
            self.ShowErrorDlg("디렉토리를 먼저 검색해주세요.")
            return

        if nMode == 0:
            self.CopyBundleAndMapping(edProjectPath, edSavePath, edVersion)
        elif nMode == 1:
            self.CopyAPKAndMapping(edProjectPath, edSavePath, edVersion)
        elif nMode == 2:
            self.CopyOnlyBundle(edProjectPath, edSavePath, edVersion)
        elif nMode == 3:
            self.CopyOnlyAPK(edProjectPath, edSavePath, edVersion)

        # print("edProjectPath : {}".format(edProjectPath))
        # print("edSavePath : {}".format(edSavePath))
        # print("edVersion : {}".format(edVersion))
        # print("projectName : {}".format(projectName))
        # print("bundlePath : {}".format(bundlePath))
        # print("mappingPath : {}".format(mappingPath))
        # print("copyBundlePath : {}".format(copyBundlePath))
        # print("copyMappingPath : {}".format(copyMappingPath))
        # print("bFileName : {}".format(bundleName))

    def CopyBundleAndMapping(self, edProjectPath, edSavePath, edVersion):
        projectName = str(self.cbProjectName.currentText())
        bundlePath = edProjectPath + "/" + projectName + AND_BUNDLE_PATH
        mappingPath = edProjectPath + "/" + projectName + AND_MAPPING_PATH
        country = str(self.cbCountry.currentText())
        bResult = self.CheckPath(bundlePath)
        if not bResult:
            self.ShowErrorDlg("해당 경로에 {}파일이 없습니다.".format(AND_BUNDLE_NAME + AND_BUNDLE_EXTENSION))
            return
        bResult = self.CheckPath(mappingPath)
        if not bResult:
            self.ShowErrorDlg("해당 경로에 {}파일이 없습니다.".format(AND_MAPPING_NAME + AND_MAPPING_EXTENSION))
            return
        copyBundlePath = "{}/{}/Bundle/V{}/".format(edSavePath, country, edVersion)
        self.MakeDir(copyBundlePath)

        copyMappingPath = "{}/{}/Mapping/V{}/".format(edSavePath, country, edVersion)
        self.MakeDir(copyMappingPath)

        bundleName = "{}_Bundle_V{}_{}{}".format(projectName, edVersion, datetime.today().strftime("%Y%m%d"),
                                                 AND_BUNDLE_EXTENSION)
        bResult1 = shutil.copy(bundlePath, copyBundlePath + bundleName)
        mappingName = "{}_MAPPING_V{}_{}{}".format(projectName, edVersion, datetime.today().strftime("%Y%m%d"),
                                                   AND_MAPPING_EXTENSION)
        bResult2 = shutil.copy(mappingPath, copyMappingPath + mappingName)

        if not bResult1:
            self.ShowErrorDlg("번들 파일 생성 실패")

        if not bResult2:
            self.ShowErrorDlg("매핑 파일 생성 실패")

        if bResult1 and bResult2:
            self.ShowOKDlg("완료되었습니다.")

    def CopyAPKAndMapping(self, edProjectPath, edSavePath, edVersion):
        projectName = str(self.cbProjectName.currentText())
        apkPath = edProjectPath + "/" + projectName + AND_APK_PATH
        mappingPath = edProjectPath + "/" + projectName + AND_MAPPING_PATH
        country = str(self.cbCountry.currentText())
        bResult = self.CheckPath(apkPath)
        if not bResult:
            self.ShowErrorDlg("해당 경로에 {}파일이 없습니다.".format(AND_APK_NAME + AND_APK_EXTENSION))
            return
        bResult = self.CheckPath(mappingPath)
        if not bResult:
            self.ShowErrorDlg("해당 경로에 {}파일이 없습니다.".format(AND_MAPPING_NAME + AND_MAPPING_EXTENSION))
            return
        copyAPKPath = "{}/{}/APK/V{}/".format(edSavePath, country, edVersion)
        self.MakeDir(copyAPKPath)

        copyMappingPath = "{}/{}/MAPPING/V{}/".format(edSavePath, country, edVersion)
        self.MakeDir(copyMappingPath)

        bundleName = "{}_APK_V{}_{}{}".format(projectName, edVersion, datetime.today().strftime("%Y%m%d"),
                                              AND_APK_EXTENSION)
        bResult1 = shutil.copy(apkPath, copyAPKPath + bundleName)
        mappingName = "{}_MAPPING_V{}_{}{}".format(projectName, edVersion, datetime.today().strftime("%Y%m%d"),
                                                   AND_MAPPING_EXTENSION)
        bResult2 = shutil.copy(mappingPath, copyMappingPath + mappingName)

        if not bResult1:
            self.ShowErrorDlg("APK 파일 생성 실패")
        if not bResult2:
            self.ShowErrorDlg("매핑 파일 생성 실패")
        if bResult1 and bResult2:
            self.ShowOKDlg("완료되었습니다.")

    def CopyOnlyBundle(self, edProjectPath, edSavePath, edVersion):
        projectName = str(self.cbProjectName.currentText())
        bundlePath = edProjectPath + "/" + projectName + AND_BUNDLE_PATH
        country = str(self.cbCountry.currentText())
        bResult = self.CheckPath(bundlePath)
        if not bResult:
            self.ShowErrorDlg("해당 경로에 {}파일이 없습니다.".format(AND_BUNDLE_NAME + AND_BUNDLE_EXTENSION))
            return

        copyBundlePath = "{}/{}/Bundle/V{}/".format(edSavePath, country, edVersion)
        self.MakeDir(copyBundlePath)

        bundleName = "{}_Bundle_V{}_{}{}".format(projectName, edVersion, datetime.today().strftime("%Y%m%d"),
                                                 AND_BUNDLE_EXTENSION)
        bResult1 = shutil.copy(bundlePath, copyBundlePath + bundleName)

        if not bResult1:
            self.ShowErrorDlg("번들 파일 생성 실패")
        else:
            self.ShowOKDlg("완료되었습니다.")

    def CopyOnlyAPK(self, edProjectPath, edSavePath, edVersion):
        projectName = str(self.cbProjectName.currentText())
        apkPath = edProjectPath + "/" + projectName + AND_APK_PATH

        country = str(self.cbCountry.currentText())
        bResult = self.CheckPath(apkPath)
        if not bResult:
            self.ShowErrorDlg("해당 경로에 {}파일이 없습니다.".format(AND_APK_NAME + AND_APK_EXTENSION))
            return

        copyAPKPath = "{}/{}/APK/V{}/".format(edSavePath, country, edVersion)
        self.MakeDir(copyAPKPath)

        copyMappingPath = "{}/{}/APK/V{}/".format(edSavePath, country, edVersion)
        self.MakeDir(copyMappingPath)

        bundleName = "{}_APK_V{}_{}{}".format(projectName, edVersion, datetime.today().strftime("%Y%m%d"),
                                              AND_APK_EXTENSION)
        bResult1 = shutil.copy(apkPath, copyAPKPath + bundleName)

        if not bResult1:
            self.ShowErrorDlg("APK 파일 생성 실패")
        else:
            self.ShowOKDlg("완료되었습니다.")

    def SearchDir(self):
        edProjectPath = self.edProjectPath.text()
        if not edProjectPath:
            self.edProjectPath.setFocus()
            self.ShowErrorDlg("프로젝트 경로를 확인해주세요.")
            return
        self.cbProjectName.clear()
        self.cbProjectName.addItem("프로젝트 경로 검색 ㄱㄱ")

        filenames = os.listdir(edProjectPath)
        for filename in filenames:
            if filename == "_Res":
                continue
            if filename == "_KEY":
                continue
            self.cbProjectName.addItem(filename)

    def ShowErrorDlg(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.exec_()

    def ShowOKDlg(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("OK")
        msg.setInformativeText(message)
        msg.exec_()

    def CheckPath(self, path):
        if Path(path).is_file():
            return True
        else:
            return False


    def MakeDir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

# 기본적으로 프로그램을 실행시키는 역할
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

# 프로그램을 이벤트 루프로 진입시켜주는 코드
app.exec_()
