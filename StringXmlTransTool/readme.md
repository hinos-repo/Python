# StringXmlTransTool

## 소개
- 안드로이드 String.xml 파일을 선택한 나라 언어에 맞게 번역

## 사용법
- PROJECT_ID, PROJECT_SERVICE_JSON은 https://cloud.google.com/docs/authentication/getting-started 문서를 참조하여 값을 세팅하면 된다.
- MY_SELECT_COUNTRY_LIST 변수에 국가 코드를 추가한다.
- MY_SOURCE_COUNTRY 변수에 raw/strings.xml를 참고하여 번역 기준 국가 코드를 추가한다.
- 코드를 실행한다.   

## 주의
- COUNTRY_DICT 변수는 안드로이드, 구글의 국가코드를 정리해 놓은 기준표이다.
- 주석에서 이야기하는 국가 코드는 안드로이드용 국가코드를 뜻한다.
- values 폴더(안드로이드 기본 폴더)는 따로 안 만들어주니 주의해야 한다.

- python 3.8 환경에서 제작되었기 때문에 shutil의 덮어쓰기 기능과 dictionary 순서 보장이 지원된다.
3.7 이하 버전에서 사용해야 될 경우 copytree의 덮어쓰기 기능을 따로 구현해야하며, dictionary 대신 ordereddict을 사용해야 한다.

## 시연 영상
[![예제](https://user-images.githubusercontent.com/60995477/115651985-46d11a80-a367-11eb-8f14-89c881330e14.png)](https://youtu.be/bsLSPnVvUno?t=0s) 
