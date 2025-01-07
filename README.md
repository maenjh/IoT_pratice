# IoT_pratice

## 설치 방법

### 1. Python 3.10 설치 

https://www.python.org/downloads/release/python-3100/

각 컴퓨터에 맞는 버전을 설치해주세요

### 1. 필요한 패키지 설치
```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```


# 1. YOLOv8 웹캠을 이용한 실시간 객체 감지 프로젝트

이 프로젝트는 YOLOv8을 사용하여 웹캠에서 실시간으로 객체를 감지하는 프로그램입니다.
# YOLOv8을 활용한 실시간 객체 감지

이 코드는 YOLOv8 모델을 사용하여 웹캠의 실시간 영상에서 객체를 감지하고, 그 결과를 화면에 시각화하여 표시하는 Python 스크립트입니다.

---

## 코드 설명

### 1. YOLO 모델 로드
- `YOLO('yolov8n.pt')`를 사용하여 YOLOv8의 Nano 버전을 로드합니다. Nano 버전은 경량화된 모델로, 빠르고 효율적인 객체 감지를 제공합니다.
- 사용자는 필요에 따라 다른 버전(예: `yolov8s.pt`, `yolov8m.pt`)으로 대체할 수 있습니다.

### 2. 웹캠 초기화
- `cv2.VideoCapture(0)`를 통해 기본 웹캠을 활성화합니다.
- `0`은 기본 웹캠을 의미하며, 외부 카메라를 사용하는 경우 적절한 번호로 변경 가능합니다.

### 3. 실시간 객체 감지 루프
- 웹캠에서 프레임을 반복적으로 읽어들이며, `ret`과 `frame`을 통해 성공 여부와 영상을 가져옵니다.
- YOLO 모델을 사용하여 각 프레임에서 객체를 감지하고, `results = model(frame)`으로 결과를 얻습니다.
- `results[0].plot()`를 통해 감지 결과를 프레임에 시각화하여 객체의 위치와 이름을 표시합니다.

### 4. 화면에 표시
- `cv2.imshow()`를 사용하여 시각화된 프레임을 화면에 출력합니다.
- 사용자는 실시간으로 감지된 객체를 확인할 수 있습니다.

### 5. 종료 조건
- 사용자가 'q' 키를 누르면 `cv2.waitKey(1)` 조건에 의해 루프가 종료됩니다.

### 6. 리소스 해제
- `cap.release()`로 웹캠 리소스를 해제하고, `cv2.destroyAllWindows()`를 호출하여 모든 OpenCV 창을 닫습니다.

---

## 실행 방법
1. YOLOv8 모델 파일(`yolov8n.pt`)이 로컬 환경에 있어야 합니다. [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)를 참고하여 모델 파일을 다운로드하십시오.
2. Python 환경에서 필요한 라이브러리(OpenCV, Ultralytics)를 설치합니다:
   ```bash
   pip install opencv-python ultralytics


##  실행 방법

1. 프로그램 실행하기
    ```bash
   python yolo.py 
    ```

ultralytics 패키지에 대해 자세히 알고싶다면
아래 사이트에서 참고하세요
https://docs.ultralytics.com/ko/


---
# 2. Kaggle 데이터분석


- 이 프로젝트는 IoT 센서를 통해 수집된 실내외 온도 데이터를 분석하여 시간적, 공간적 온도 패턴을 이해하고 데이터 품질 문제를 식별하는 데 초점을 맞추고 있습니다. 데이터는 1년치 기록으로 보이나 실제로는 86일 동안만 측정된 것으로 확인되었으며, 실외 온도는 73%, 실내 온도는 27%를 차지했습니다. 데이터 전처리 과정을 통해 중복 제거, 열 이름 변경 및 날짜별 분석을 수행하였으며, 박스플롯과 산점도를 활용해 빈도 분포 및 실내외 온도 변화를 시각화하였습니다. 결과적으로, 월별 온도 특성과 데이터의 불균형 문제를 파악하고, 향후 데이터 수집 주기의 일관성과 품질 개선 필요성을 제시하였습니다.

## 2.1 사용한 코드 출처
- 데이터는 Kaggle의 [IOT Temperature Readings - Data Health Checkup
](https://www.kaggle.com/code/infernop/iot-temperature-readings-data-health-checkup)에서 코드를 가져와 사용하였습니다.


---
# 3. IoT_건강_예측_학습

- 이 코드는 IoT 데이터를 기반으로 다양한 머신러닝 모델(Naive Bayes, Decision Tree, Logistic Regression, SVM, Random Forest, KNN, Gradient Boosting)을 학습 및 평가하여, 정확도가 가장 높은 모델을 선정하고, GridSearchCV를 통해 Random Forest 모델의 하이퍼파라미터를 최적화하여 최종 모델을 완성합니다. 최종 모델은 테스트 데이터에서 높은 정확도를 기록했으며, 예제 데이터를 입력받아 "Low", "Medium", "High"로 상태를 예측할 수 있는 시스템을 제공합니다.
## 3.1 사용한 데이터 출처
- 데이터는https://github.com/Ramyadeveloper59/Health-Monitoring-system-by-using-Machine-Learning 레포에서 가져온뒤 임의로 증강하여 사용하였습니다.
  
## 3.2 데이터 메타데이터
### 3.2.1. 데이터 크기 (Shape):

- 총 1149개의 행과 7개의 열로 구성.

### 3.2.2. 열 정보 (Columns):

- Unnamed: 0: 인덱스 열 (자동 생성된 것으로 보임).
- Sl.No: 순번 열.
- Patient ID: 환자 ID.
- Temperature Data: 온도 데이터.
- ECG Data: 심전도 데이터.
- Pressure Data: 압력 데이터.
- T- arget: 타겟 값 (환자의 상태, 0, 1, 2로 분류).
- 
### 3.2.3. 데이터 타입 (Data Types):
- 모든 열이 int64 형식으로 구성.
### 3.2.4. 결측치 (Missing Values):
- 모든 열에 결측치 없음.

# 4. MQTT를 활용한 IoT 센서 데이터 수집 예제

## 시작전 세팅 사항
-  Mosquitto MQTT 브로커 설치
Windows에서 Mosquitto MQTT 브로커 설치 방법
### 1. Mosquitto 다운로드
Mosquitto 공식 다운로드 페이지 방문
- Windows 인스톨러 다운로드
- mosquitto-2.x.x-install-windows-x64.exe 파일 선택



### 2. 필수 구성 요소 설치
- Visual C++ redistributable 설치
다운로드 페이지의 "Visual C++ 2015 redistributable" 링크를 통해 설치
이미 설치되어 있다면 이 단계 건너뛰기



### 3. Mosquitto 설치
다운로드한 mosquitto-2.x.x-install-windows-x64.exe 실행
설치 마법사의 안내에 따라 진행
기본 설치 경로 사용 (C:\Program Files\mosquitto)

### 4. 설정 파일 수정

C:\Program Files\mosquitto\mosquitto.conf 파일을 메모장으로 열기
파일 끝에 다음 내용 추가:
```
listener 1883
allow_anonymous true
``` 
### 5. 서비스 실행
방법 1: 서비스 관리자 사용
- services.msc 실행 (Windows + R 키를 누르고 입력)
- "Mosquitto Broker" 서비스 찾기
- 서비스 선택 후 "시작" 클릭

방법 2: 명령 프롬프트 사용

관리자 권한으로 명령 프롬프트 실행
서비스 시작:
```cmd
net start mosquitto
```
서비스 상태 확인:
```cmd
sc query mosquitto
```

### 6. 설치 확인

서비스가 정상적으로 실행되면 localhost:1883에서 MQTT 브로커가 동작
테스트를 위해 MQTT 클라이언트 도구 사용 가능

### 주의사항

방화벽 설정에서 1883 포트 허용 필요할 수 있음
설치 중 오류 발생 시 관리자 권한으로 실행 필요
서비스가 시작되지 않을 경우 Windows 이벤트 로그 확인