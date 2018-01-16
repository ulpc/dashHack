# dashHack
Amazon Dash를 해킹해 가지고 놀자.
이 프로그램은 같은 네트워크에 연결된 Amazon Dash를 찾고, 그 신호를 캐치해 원하는 액션을 실행합니다.

## 필요한 패키지 설치하기
```
$pip install -r requirements.txt
```

## Amazon Dash MAC주소 찾기
```
$sudo python dash_hack.py detect
Password: (패스워드 입력)
Waiting for a button press... (Amazon Dash 클릭)
Button press detected: 00:fc:8b:58:98:75
```

## 액션 config 작성하기

```
# config.yaml
# -----------
# 찾은 MAC 주소
00:fc:8b:58:98:75:
    action:
        # 이 Amazon Dash에 맵핑할 액션 function 이름
        print_message
    args:
        # 액션 function에 전달할 인자 목록
        ["hello world"]
# 두 번째 Amazon Dash부터도 똑같이 나열
```

## 액션 function 작성하기
```
# action.py
# -----------
def print_message(message):
    print message
```

## 데몬 실행하기
```
$sudo python dash_hack.py [ --config config.yml] run
Password: (패스워드 입력)
Waiting for the button press... (config에 등록한 Amazon Dash 클릭)
hello world
```
액션 config의 경우 디폴트로 `config.yml`를 사용합니다. 하지만 `--config` 파라미터를 사용해 원하는 파일로 대체할 수도 있습니다.
