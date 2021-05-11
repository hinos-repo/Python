# LyricsMgr_V3

## 사용 기술
PyQt5, FFMPEG, Requests

## 기능
- 가사 검색
- lrc 파일 생성
- lrc 파일을 srt로 변환
- Mp3 파일 + 이미지 파일 + srt파일로 MP4 파일 변환

## 동작 순서
- 가사 검색
- 가사 텍스트를 lrc 파일로 저장
- ffmpeg으로 lrc 파일을 srt로 변환
- ffmpeg으로 mp3 + jpg를 mp4 파일로 변환
- ffmpeg으로 mp4 + srt로 가사 적용

[![예제](https://user-images.githubusercontent.com/60995477/115651985-46d11a80-a367-11eb-8f14-89c881330e14.png)](https://youtu.be/UJQaY9R6IgU?t=0s) 
