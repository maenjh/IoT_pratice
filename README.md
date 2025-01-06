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


웹캠을 연결한 후 프로그램을 실행해주세요

## 1.1 실행 방법

1. 프로그램 실행하기
   ```bash
   python yolo.py
   ```

ultralytics 패키지에 대해 자세히 알고싶다면
아래 사이트에서 참고하세요
https://docs.ultralytics.com/ko/



# 2. Kaggle 데이터분석



# 3. IoT_건강_예측_학습

## 3.1 데이터 출처
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