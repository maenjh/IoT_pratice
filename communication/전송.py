# publisher.py
import paho.mqtt.client as mqtt
import pandas as pd
import json
import time

class MQTTPublisher:
    def __init__(self, broker="localhost", port=1883):
        self.broker = broker
        self.port = port
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("브로커에 연결되었습니다.")
        else:
            print(f"연결 실패, 에러 코드: {rc}")

    def connect(self):
        try:
            self.client.connect(self.broker, self.port, 60)
            self.client.loop_start()
        except Exception as e:
            print(f"연결 중 에러 발생: {e}")

    def publish_csv(self, csv_path, topic="csv/data"):
        try:
            # CSV 파일 읽기
            df = pd.read_csv(csv_path)
            
            # DataFrame을 JSON 문자열로 변환
            json_data = df.to_json(orient='records')
            
            # 데이터 발행
            result = self.client.publish(topic, json_data)
            
            if result.rc == mqtt.MQTT_ERR_SUCCESS:
                print(f"데이터가 성공적으로 전송되었습니다. 토픽: {topic}")
            else:
                print("데이터 전송 실패")
                
        except FileNotFoundError:
            print(f"CSV 파일을 찾을 수 없습니다: {csv_path}")
        except Exception as e:
            print(f"에러 발생: {e}")

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        print("브로커 연결이 종료되었습니다.")

# 사용 예제
if __name__ == "__main__":
    # MQTT 발행자 생성
    publisher = MQTTPublisher()
    
    # 브로커에 연결
    publisher.connect()
    
    # 잠시 대기 (연결 설정을 위해)
    time.sleep(1)
    
    # CSV 파일 전송
    publisher.publish_csv("communication/IOT-temp.csv")
    
    # 잠시 대기 (메시지 전송을 위해)
    time.sleep(1)
    
    # 연결 종료
    publisher.disconnect()