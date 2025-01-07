# subscriber.py
import paho.mqtt.client as mqtt
import pandas as pd
import json
from datetime import datetime

class MQTTSubscriber:
    def __init__(self, broker="localhost", port=1883):
        self.broker = broker
        self.port = port
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("브로커에 연결되었습니다.")
            # csv/data 토픽 구독
            client.subscribe("csv/data")
            print("'csv/data' 토픽 구독을 시작합니다.")
        else:
            print(f"연결 실패, 에러 코드: {rc}")

    def on_message(self, client, userdata, msg):
        try:
            print(f"메시지 수신: {msg.topic}")
            
            # JSON 문자열을 파이썬 객체로 변환
            data = json.loads(msg.payload.decode())
            
            # JSON 데이터를 DataFrame으로 변환
            df = pd.DataFrame(data)
            
            # 현재 시간을 파일명에 포함하여 저장
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"received_data_{timestamp}.csv"
            
            # CSV 파일로 저장
            df.to_csv(output_filename, index=False)
            print(f"데이터가 {output_filename}로 저장되었습니다.")
            
            # 데이터 내용 출력
            print("\n수신된 데이터 미리보기:")
            print(df.head())
            
        except Exception as e:
            print(f"데이터 처리 중 에러 발생: {e}")

    def connect(self):
        try:
            self.client.connect(self.broker, self.port, 60)
            print(f"브로커 {self.broker}:{self.port}에 연결을 시도합니다...")
        except Exception as e:
            print(f"연결 중 에러 발생: {e}")

    def start(self):
        # 메시지 수신 루프 시작
        self.client.loop_forever()

    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()
        print("브로커 연결이 종료되었습니다.")

# 사용 예제
if __name__ == "__main__":
    # MQTT 구독자 생성
    subscriber = MQTTSubscriber()
    
    try:
        # 브로커에 연결
        subscriber.connect()
        
        # 메시지 수신 시작
        print("메시지 수신 대기 중... (종료하려면 Ctrl+C를 누르세요)")
        subscriber.start()
        
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")
        subscriber.stop()