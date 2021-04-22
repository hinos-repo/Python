import os
import shutil
from datetime import datetime
from pathlib import Path

AND_BUNDLE_NAME = "app-release"
AND_BUNDLE_NAME2 = "app"
AND_MAPPING_NAME = "mapping"
AND_APK_NAME = "app-release"

AND_BUNDLE_EXTENSION = ".aab"
AND_MAPPING_EXTENSION = ".txt"
AND_APK_EXTENSION = ".apk"

AND_APK_PATH = "/app/release/" + AND_APK_NAME + AND_APK_EXTENSION
AND_BUNDLE_PATH = "/app/release/" + AND_BUNDLE_NAME + AND_BUNDLE_EXTENSION
AND_AUTO_BUNDLE_PATH = "/app/build/outputs/bundle/release/" + AND_BUNDLE_NAME + AND_BUNDLE_EXTENSION
AND_AUTO_BUNDLE_PATH2 = "/app/build/outputs/bundle/release/" + AND_BUNDLE_NAME2 + AND_BUNDLE_EXTENSION
AND_AUTO_APK_PATH = "/app/build/outputs/apk/release/" + AND_APK_NAME + AND_APK_EXTENSION
AND_MAPPING_PATH = "/app/build/outputs/mapping/release/" + AND_MAPPING_NAME + AND_MAPPING_EXTENSION


def CheckPath(path):
    if Path(path).is_file():
        return True
    else:
        return False


def MakeDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def AutoCopyBundleAndMapping(projectName, base_path, save_path, version, country):
    bundlePath = base_path + "/" + projectName + AND_AUTO_BUNDLE_PATH
    mappingPath = base_path + "/" + projectName + AND_MAPPING_PATH
    country = str(country)
    bResult = CheckPath(bundlePath)
    if not bResult:
        bundlePath = base_path + "/" + projectName + AND_AUTO_BUNDLE_PATH2
        bResult = CheckPath(bundlePath)
        if not bResult:
            print("해당 경로에 {}파일이 없습니다.".format(bundlePath))
            return
    bResult = CheckPath(mappingPath)
    if not bResult:
        print("해당 경로에 {}파일이 없습니다.".format(AND_MAPPING_NAME + AND_MAPPING_EXTENSION))
        return
    copyBundlePath = "{}/{}/Bundle/V{}/".format(save_path, country, version)
    MakeDir(copyBundlePath)

    copyMappingPath = "{}/{}/Mapping/V{}/".format(save_path, country, version)
    MakeDir(copyMappingPath)

    bundleName = "{}_Bundle_V{}_{}{}".format(projectName, version, datetime.today().strftime("%Y%m%d"),
                                             AND_BUNDLE_EXTENSION)
    bResult1 = shutil.copy(bundlePath, copyBundlePath + bundleName)
    mappingName = "{}_MAPPING_V{}_{}{}".format(projectName, version, datetime.today().strftime("%Y%m%d"),
                                               AND_MAPPING_EXTENSION)
    bResult2 = shutil.copy(mappingPath, copyMappingPath + mappingName)

    if not bResult1:
        print("번들 파일 생성 실패")

    if not bResult2:
        print("매핑 파일 생성 실패")

    if bResult1 and bResult2:
        print("완료되었습니다.")


def AutoCopyAPKAndMapping(projectName, base_path, save_path, version, country):
    apkPath = base_path + "/" + projectName + AND_AUTO_APK_PATH
    country = str(country)
    bResult = CheckPath(apkPath)
    if not bResult:
        print("해당 경로에 {}파일이 없습니다.".format(apkPath))

    copyAPKPath = "{}/{}/APK/V{}/".format(save_path, country, version)
    MakeDir(copyAPKPath)

    bundleName = "{}_APK_V{}_{}{}".format(projectName, version, datetime.today().strftime("%Y%m%d"),
                                          AND_APK_EXTENSION)
    bResult1 = shutil.copy(apkPath, copyAPKPath + bundleName)

    if not bResult1:
        print("번들 파일 생성 실패")

    if bResult1:
        print("완료되었습니다.")


base_path = "C:\workspace/ZeroProject/A_Radio/AB"

temp = os.listdir(base_path)
for t in temp:
    if CheckPath(base_path + "/" + t + AND_AUTO_BUNDLE_PATH2):
        AutoCopyBundleAndMapping(
            t,
            base_path,
            "\\\\192.168.53.7/data/bundle/AB",
            "21",
            "multi"
        )

# base_path = "C:\workspace\ZeroProject\A_Radio\AB_TEST"
#
# temp = os.listdir(base_path)
# for t in temp:
#     if CheckPath(base_path + "/" + t + AND_AUTO_APK_PATH):
#         AutoCopyAPKAndMapping(
#             t,
#             base_path,
#             "\\\\192.168.53.7\data\\APK\AB_TEST",
#             "20",
#             "multi"
#         )
