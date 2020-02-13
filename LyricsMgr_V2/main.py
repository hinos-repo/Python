# -*- coding: utf-8 -*-

import sys, UI

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


import requests
import re
import xml.etree.ElementTree as ET

from searchTitleInfo import searchTitleInfo


CONST_LYRICID = "\<lyricID\>(.*?)\<\/lyricID\>"
CONST_TITLE = "\<title\>(.*?)\<\/title\>"
CONST_ARTIST = "\<artist\>(.*?)\<\/artist\>"
CONST_ALBUM = "\<album\>(.*?)\<\/album\>"

TEMPLATE_SEARCH_TITLE_NAME = """\
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:ns2="ALSongWebServer/Service1Soap"
xmlns:ns1="ALSongWebServer"
xmlns:ns3="ALSongWebServer/Service1Soap12">
<SOAP-ENV:Body>
<ns1:GetResembleLyricList2>
<ns1:encData>7c2d15b8f51ac2f3b2a37d7a445c3158455defb8a58d621eb77a3ff8ae4921318e49cefe24e515f79892a4c29c9a3e204358698c1cfe79c151c04f9561e945096ccd1d1c0a8d8f265a2f3fa7995939b21d8f663b246bbc433c7589da7e68047524b80e16f9671b6ea0faaf9d6cde1b7dbcf1b89aa8a1d67a8bbc566664342e12</ns1:encData>
<ns1:title>{title}</ns1:title>
<ns1:artist>{artist_name}</ns1:artist>
<ns1:pageNo>{page}</ns1:pageNo>
</ns1:GetResembleLyricList2>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>
"""


TEMPLATE_SEARCH_SONG_SEQ = """\
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
    xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
    xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:ns2="ALSongWebServer/Service1Soap"
    xmlns:ns1="ALSongWebServer"
    xmlns:ns3="ALSongWebServer/Service1Soap12">
    <SOAP-ENV:Body>
        <ns1:GetLyricByID2>
            <ns1:encData>7c2d15b8f51ac2f3b2a37d7a445c3158455defb8a58d621eb77a3ff8ae4921318e49cefe24e515f79892a4c29c9a3e204358698c1cfe79c151c04f9561e945096ccd1d1c0a8d8f265a2f3fa7995939b21d8f663b246bbc433c7589da7e68047524b80e16f9671b6ea0faaf9d6cde1b7dbcf1b89aa8a1d67a8bbc566664342e12</ns1:encData>
            <ns1:lyricID>{soung_seq}</ns1:lyricID>
        </ns1:GetLyricByID2>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
"""

url = 'http://lyrics.alsong.co.kr/alsongwebservice/service1.asmx'

arrResInfo = []

class MainDialog(QDialog, UI.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self, None)
        self.setupUi(self)
        self.cbBox.addItem("먼저 노래와 가수 이름을 입력 후 검색해주세요.")
        self.btnSearch1.clicked.connect(self.SearchTitle)
        self.btnSearch2.clicked.connect(self.SearchLyric)
        self.btnExtract.clicked.connect(self.ExtractLyric)

    def SearchTitle(self):
        title = self.edTitle.text()
        name = self.edName.text()
        if not title:
            self.ShowErrorDlg("제목을 입력해주세요.")
            return
        if not name:
            self.ShowErrorDlg("가수 이름을 입력해주세요,")
            return

        self.cbBox.clear()
        arrResInfo.clear()

        resp = requests.post(
            url,
            data=TEMPLATE_SEARCH_TITLE_NAME.format(
                title=title,
                artist_name=name,
                page=0,
            ).encode(),
            headers={
                'content-type': 'application/soap+xml',
            },
        )


        arrLyricID = re.findall(CONST_LYRICID, str(resp.text))
        arrTitle = re.findall(CONST_TITLE, str(resp.text))
        arrArTist = re.findall(CONST_ARTIST, str(resp.text))
        arrAlbum = re.findall(CONST_ALBUM, str(resp.text))

        length = len(arrLyricID)

        for i in range(length):
            arrResInfo.append(searchTitleInfo(arrLyricID[i], arrTitle[i], arrArTist[i], arrAlbum[i]))

        for i in arrResInfo:
            self.cbBox.addItem(i.lyricID + " / " + i.title + " / " + i.artist + " / " + i.albun)
            print(i.lyricID, i.title , i.artist, i.albun)

    def SearchLyric(self):
        title = self.edTitle.text()
        name = self.edName.text()
        index = self.cbBox.currentIndex()
        if index == -1:
            self.ShowErrorDlg("가수와 제목을 다시 검색해주세요.")
            return
        if not title:
            self.ShowErrorDlg("제목을 입력해주세요.")
            return
        if not name:
            self.ShowErrorDlg("가수 이름을 입력해주세요,")
            return

        resp2 = requests.post(
            url,
            data=TEMPLATE_SEARCH_SONG_SEQ.format(
                soung_seq=arrResInfo[index].lyricID,
            ).encode(),
            headers={
                'content-type': 'application/soap+xml',
            },
        )

        tree = ET.fromstring(resp2.text)
        arr = list(tree.iter())

        for model in arr :
            tag = re.sub('\{(.*?)\}', '', str(model.tag))
            text = model.text
            if tag == 'lyric':
                self.tvLyrics.setPlainText(text)
                break

    def ExtractLyric(self):
        strPutPath = self.edPath.text()
        strPutLyrics = self.tvLyrics.toPlainText()
        if not strPutPath:
            self.ShowErrorDlg("저장 경로를 입력해주세요.")
            return
        if not strPutLyrics:
            self.ShowErrorDlg("먼저 가사를 검색해주세요.")
            return

        print("zz" + strPutPath)

        file = open(strPutPath + '/' + 'lyric.lrc', 'w', encoding='utf8')
        file.write(strPutLyrics)
        file.close()

        lrc_file = open(strPutPath + '/' + 'lyric.lrc', encoding='utf8')
        lrc_string = ''.join(lrc_file.readlines())
        lrc_file.close()

        subs = pylrc.parse(lrc_string)
        srt = subs.toSRT()
        srt_file = open(strPutPath + '/' + 'lyric.srt', 'w', encoding='utf8')
        srt_file.write(srt)
        srt_file.close()

    def ShowErrorDlg(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.exec_()

# 기본적으로 프로그램을 실행시키는 역할
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

# 프로그램을 이벤트 루프로 진입시켜주는 코드
app.exec_()

# edTitle
# edName
# btnSearch1
# listView
# btnSearch2
# tvLyrics
