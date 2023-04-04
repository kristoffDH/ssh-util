# ssh-util

* 내장 ssh 설정파일 편집 및 ssh 연결 툴 

* window에서 사용하려고 만들었지만 linux에서도 동작 가능(다만 pyinstaller 대신 다른 모듈 사용)



## version

* python3
* python package : requirenments.txt 참조



## command

* exit (q, Q)
  * 종료
* add (a, A)
  * 설정 추가
* delete (d, D)
  * 설정 삭제
* update (u, U)
  * 설정 업데이트
* list (l, L)
  * 설정 목록
* connect (c, C)
  * ssh 연결



## package install

script 폴더 내의 스크립트 확인

``` 
(win)
virtualenv.exe venv
.\venv\Scripts\activate
pip install -r .\requirenments.txt
$env:PYTHONPATH = pwd | select-string "C"
pyinstaller.exe -F .\bin\ssh_util.py

(linux)
python3 -m venv venv
source venv/bin/activate
export PYTHONPATH=$(pwd)
pyinstaller -D -F -n ssh-util -c ./bin/ssh_util.py
```



