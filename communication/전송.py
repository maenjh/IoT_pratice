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
        self.connected = False

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("브로커에 연결되었습니다.")
            self.connected = True
        else:
            print(f"연결 실패, 에러 코드: {rc}")
            self.connected = False

    def connect(self):
        try:
            print(f"브로커 {self.broker}:{self.port}에 연결을 시도합니다...")
            self.client.connect(self.broker, self.port, 60)
            self.client.loop_start()
            time.sleep(1)  # 연결 대기
            return True
        except Exception as e:
            print(f"연결 중 에러 발생: {e}")
            return False

    def publish_csv(self, csv_path, topic="csv/data"):
        try:
            # CSV 파일 읽기
            df = pd.read_csv(csv_path)
            print("CSV 파일을 읽었습니다.")
            print(f"데이터 미리보기:\n{df.head()}")
            
            # DataFrame을 JSON 문자열로 변환
            json_data = df.to_json(orient='records')
            
            # 데이터 발행
            print(f"'{topic}' 토픽으로 데이터를 전송합니다...")
            result = self.client.publish(topic, json_data, qos=1)
            result.wait_for_publish()
            
            if result.rc == mqtt.MQTT_ERR_SUCCESS:
                print(f"데이터가 성공적으로 전송되었습니다.")
                return True
            else:
                print("데이터 전송 실패")
                return False
                
        except FileNotFoundError:
            print(f"CSV 파일을 찾을 수 없습니다: {csv_path}")
        except Exception as e:
            print(f"에러 발생: {e}")
        return False

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        print("브로커 연결이 종료되었습니다.")

if __name__ == "__main__":
    # CSV 파일 경로 설정
    csv_file = "communication/IOT-temp.csv"  # 실제 CSV 파일 경로로 변경하세요
    
    try:
        publisher = MQTTPublisher()
        if publisher.connect():
            while True:
                print("\n1. CSV 파일 전송")
                print("2. 프로그램 종료")
                choice = input("선택하세요 (1 또는 2): ")
                
                if choice == '1':
                    publisher.publish_csv(csv_file)
                    print("\n다음 작업을 선택하세요...")
                elif choice == '2':
                    break
                else:
                    print("잘못된 선택입니다. 다시 선택하세요.")
    
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")
    except Exception as e:
        print(f"예외 발생: {e}")
    finally:
        publisher.disconnect()