import numpy as np
import matplotlib.pyplot as plt
import time

class TemperatureSensor:
    def __init__(self):
        self.temperature = 20.0  # 초기 온도 설정 (도시)

    def read_temperature(self):
        # 랜덤하게 온도를 변경
        self.temperature += np.random.normal(0, 0.5)  # 평균 0, 표준편차 0.5
        return self.temperature

class DigitalTwin:
    def __init__(self, sensor):
        self.sensor = sensor
        self.history = []

    def update(self):
        # 센서에서 온도 읽기
        temp = self.sensor.read_temperature()
        self.history.append(temp)
        self.display()

    def display(self):
        plt.clf()  # 이전 플롯을 지움
        plt.plot(self.history, label='Real-time Temperature')
        plt.xlabel('Time')
        plt.ylabel('Temperature (°C)')
        plt.title('Digital Twin of Temperature Sensor')
        plt.legend()
        plt.pause(0.5)  # 플롯 갱신 대기

if __name__ == "__main__":
    sensor = TemperatureSensor()
    digital_twin = DigitalTwin(sensor)

    plt.ion()  # 인터랙티브 모드 시작
    plt.figure()

    try:
        while True:
            digital_twin.update()
            time.sleep(1)  # 1초 대기
    except KeyboardInterrupt:
        print("디지털 트윈 시뮬레이션 종료.")
