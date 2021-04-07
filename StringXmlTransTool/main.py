import os
import shutil

import xml.dom.minidom as md
from data.config import PROJECT_ID
from data.config import PROJECT_SERVICE_JSON
from google.cloud import translate



COUNTRY_DICT = {
        # 안드로이드 :  # 구글
                'ar': 'ar',                 # 아랍
                'cs': 'cs',                 # 체코
                'da': 'da',                 # 덴마크
                'de': 'de',                 # 독일
                'el': 'el',                 # 그리스
                'en': 'en',                 # 영어
                'es': 'es',                 # 스페인
                'fa': 'fa',                 # 페르시아
                'fr': 'fr',                 # 프랑스
                'hr': 'hr',                 # 크로아티아
                'in': 'id',                 # 인도네시아
                'it': 'it',                 # 이탈리아
                'ja': 'ja',                 # 일본
                'ko': 'ko',                 # 한국
                'ms': 'ms',                 # 말레이시아
                'nn': 'no',                 # 노르웨이
                'pl': 'pl',                 # 폴란드
                'pt': 'pt',                 # 포르투갈
                'ru': 'ru',                 # 러시아
                'sr': 'sr',                 # 세르비아
                'th': 'th',                 # 태국
                'tl': 'tl',                 # 필리핀
                'tr-rTR': 'tr',             # 터키
                'uk': 'uk',                 # 우크라이나
                'vi': 'vi',                 # 베트남
                'zh-rCN': 'zh-cn',          # 중국어 간체
                'zh-rTW': 'zh-tw'           # 중국어 번체
}

MY_SELECT_COUNTRY_LIST = [
    'ko', 'fr'
]

MY_SOURCE_COUNTRY = "en"

# global


# function
def translate_text(dict, project_id="YOUR_PROJECT_ID", source_country="en", target_country=None):
    if len(dict) == 0:
        errorLog("딕셔너리 사이즈가 0입니다.")

    if target_country is None:
        errorLog("딕셔너리 사이즈가 0입니다.")

    client = translate.TranslationServiceClient()
    location = "global"

    parent = f"projects/{project_id}/locations/{location}"

    temp = ""

    for v in dict.values():
        temp += v + "|"

    temp = temp.replace("\\n", "[]")
    translate_contents = temp[:-1]

    print(temp)

    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [translate_contents],
            "mime_type": "text/plain",  # mime types: text/plain, text/html
            "source_language_code": source_country,
            "target_language_code": target_country,
        }
    )

    result = ""
    for translation in response.translations:
        result += translation.translated_text

    split_contents = result.split("|")
    if len(dict) == len(split_contents):
        i = 0
        for k in dict.keys():
            dict[k] = split_contents[i].strip().replace("'", "\\'").replace("[]", "\\n")
            i += 1
    else:
        errorLog("딕셔너리와 리스트 사이즈가 다릅니다.")


def errorLog(message=""):
    print(message)
    exit()
# function


# script
def main():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = PROJECT_SERVICE_JSON

    file = md.parse("raw/strings.xml")
    strings = file.getElementsByTagName('string')

    xml_dic = {}
    for s in strings:
        xml_dic[s.getAttribute('name')] = s.firstChild.nodeValue

    for country_code in MY_SELECT_COUNTRY_LIST:
        translate_dic = xml_dic.copy()
        translate_text(dict=translate_dic, project_id=PROJECT_ID, source_country=MY_SOURCE_COUNTRY,
                       target_country=COUNTRY_DICT[country_code])

        path = "copy/values-" + country_code
        shutil.copytree("raw/", path, dirs_exist_ok=True)
        f = md.parse(path + "/strings.xml")
        copy_strings = f.getElementsByTagName('string')
        for s in copy_strings:
            s.firstChild.nodeValue = translate_dic[s.getAttribute('name')]

        with open(path + "/strings.xml", "wb") as fs:
            fs.write(f.toxml(encoding='UTF-8'))
            fs.close()


main()
# script

