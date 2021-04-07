import openpyxl
import shutil
import os
import xml.etree.ElementTree as ET
import re

EXECEL_PATH = "material/excel/data2.xlsx"
COCO_METERIAL_STRING_PATH = "material/coco_string"
COCO_RESULT_PATH = "material/result"
SHEET_NAME = "앱제목"
BASE_APP_NAME = "MYAPPNAME"
XML_STRING_NAME = "strings.xml"
RESOURCE_FOLDER_CONTAIN_NAME = "values"
VALUES_BASIC = "values-en"

FIRST_POS = 4

BASE_PATH = "C:/workspace/ZeroProject/A_Radio/AB/"
SRC_PATH = "/app/src/main/res"

RESOURCE_BASE_PATH = "C:/workspace/ZeroProject/A_Radio/AB/_Res/"
RESOUCE_SRC_PATH = "/res"

RESOUCE_MODE = True

def getLanguageList(sheet, language_list):  # values-ar ~ values-th
    rows = sheet['C3':'AC3']
    for row in rows:
        for cell in row:
            language_list.append(cell.value)
    return language_list


def getLangNAppNameDict(sheet, language_list, position):
    rows = sheet['C'+str(position):'AC'+str(position)]
    name_list = []
    for row in rows:
        for cell in row:
            if cell.value is None:
                return name_list
            else:
                name_list.append(cell.value)

    name_dict = {}
    i = 0
    for lang in language_list:
        name_dict[lang] = name_list[i]
        i = i + 1

    return name_dict



def getFolderNameList(sheet, folder_name_list, position):
    rows = sheet['A'+str(position):'A'+str(100000)]
    for row in rows:
        for cell in row:
            if cell.value is None:
                return folder_name_list
            else:
                folder_name_list.append(cell.value)

    return folder_name_list

def onReplaceStringFromXml(string_path, replace_string):
    print(string_path)
    f = open(string_path, 'r', encoding='UTF-8')
    xmlString = f.read()
    f.close()
    newStrings = xmlString.replace(BASE_APP_NAME, replace_string)
    os.remove(string_path)
    f2 = open(string_path, 'w', encoding='UTF-8')
    f2.write(newStrings)
    f2.close()

def errorLogAndExit(strMessage):
    print(strMessage)
    exit()


load_excel = openpyxl.load_workbook(EXECEL_PATH, data_only=True)
load_sheet = load_excel[SHEET_NAME]

language_list = []  # values-ar ~ values-th
getLanguageList(sheet=load_sheet, language_list=language_list)

folder_name_list = []  # AB01_미국 AB02_일본 AB03_캐나다 AB04_호주
getFolderNameList(sheet=load_sheet, folder_name_list=folder_name_list, position=FIRST_POS)

# for st in folder_name_list:
#     print("C:\\workspace\\ZeroProject\\A_Radio\\AB\\_Res\\"+st)
#     print("\\\\192.168.53.7\\data\\design\\AB_cocoRadio_Renew\\launcher\\all\\" + st + ".png")
#     print()
#     print()
#
# exit()


if len(language_list) != len(os.listdir(COCO_METERIAL_STRING_PATH)):
    errorLogAndExit("언어 코드 개수와 복사 폴더의 개수가 다릅니다.")

pos = FIRST_POS
for folder_name in folder_name_list:
    # country_path = COCO_RESULT_PATH + "/" + folder_name
    country_path = ""
    if RESOUCE_MODE:
        country_path = RESOURCE_BASE_PATH + folder_name + RESOUCE_SRC_PATH
    else:
        country_path = BASE_PATH + folder_name + SRC_PATH

    if folder_name == None:
        errorLogAndExit("폴더 데이터가 없습니다")

    # if os.path.exists(country_path):
    #     shutil.rmtree(country_path)
    shutil.copytree(COCO_METERIAL_STRING_PATH, country_path, dirs_exist_ok=True)

    folder_list = []
    temp = os.listdir(country_path)
    for t in temp:
        if t.__contains__(RESOURCE_FOLDER_CONTAIN_NAME):
            folder_list.append(t)

    temp.clear()

    name_dict = getLangNAppNameDict(sheet=load_sheet, language_list=language_list, position=pos)

    for folder in folder_list:
        for language in language_list:
            if folder == language:
                onReplaceStringFromXml(country_path + "/" + language + "/" + XML_STRING_NAME, name_dict[language])
                if folder == VALUES_BASIC:
                    print(country_path + "/" + language + "/" + XML_STRING_NAME)
                    print(country_path + "/" + RESOURCE_FOLDER_CONTAIN_NAME + "/" + XML_STRING_NAME)
                    shutil.copyfile(country_path + "/" + language + "/" + XML_STRING_NAME, country_path + "/" + RESOURCE_FOLDER_CONTAIN_NAME + "/" + XML_STRING_NAME)


    pos = pos + 1

# countryRows = load_sheet['C3':'AC3']
# for row in countryRows:
#     for cell in row:
#         country_folders.append(cell.value)
