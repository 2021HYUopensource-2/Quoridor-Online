# Quoridor Online

Client and server to play the strategy board game **Quoridor**. It uses [pygame](https://www.pygame.org/news).

![](https://github.com/Quentin18/Quoridor-Online/blob/master/img/capture.png)

## 설치
 Python >=3.6필요.
명령 프롬프트 열고 실행:
```bash
pip3 install quoridor
```

## 사용법
서버 열기:
```bash
python3 -m quoridor.server [HOST] [PORT] [NUM_PLAYERS]
```
- HOST: IP 주소
- PORT: 포트 번호
- NUM_PLAYERS: 플레이어  수(2, 3 또는 4)

클리이언트로 시작하기:
```bash
python3 -m quoridor.client [HOST] [PORT]
```
HOST 와 PORT는 서버와 같아야함.

## 플레이 방법
게임의 룰을 볼 수 있음 [here](https://en.wikipedia.org/wiki/Quoridor):
- 방향키를 이용해 폰을 움직일 수 있음
- 게임 보드를 클릭해 장애물을 배치할 수 있음

게임이 끝나면 "Restart"버튼을 눌러 재시작 할 수 있다.

## Pathfinding algorithm
A pathfinding algorithm is used to check if a player is blocked or not. Thanks to the [python-pathfinding](https://github.com/brean/python-pathfinding) project.

## 연락처
이름 : Quentin Deschamps / 이메일 :  quentindeschamps18@gmail.com

## 라이선스
[MIT](https://choosealicense.com/licenses/mit/)
