# rtsp-stream-server
플라스크를 이용해 rtsp 영상 웹소켓으로 전달

ubuntu 20.04 OS에서 시작

1. 환경 설치
---

sudo apt update<br>
sudo apt install python3-pip<br>
pip install flask flask-socketio opencv-python<br>
pip install flask-cors


2. OpneGL 설치
---

sudo apt-get update<br>
sudo apt-get install libgl1-mesa-glx libgl1-mesa-dri

3. 파이썬 실행
---

파이썬 실행 : python3 app.py <br>
백그라운드 실행 : nohup python3 app.py & 
