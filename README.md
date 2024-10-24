Digital Twin Django project

# 1. 프로젝트 구성 요소
데이터 모델링: Django의 ORM을 사용하여 물리적 객체를 표현하는 모델을 정의합니다. 센서 데이터, 장비 정보, 상태 등을 저장할 수 있는 모델을 만들 수 있습니다.

데이터 수집: IoT 기기 또는 센서에서 수집된 데이터를 Django 앱으로 전송하는 방법을 구현합니다. MQTT, HTTP API 등 사용 가능

실시간 데이터 시각화: 수집된 데이터를 시각적으로 표현하기 위해 다양한 라이브러리(예: Chart.js, D3.js)와 통합

사용자 인터페이스: 대시보드를 설계하여 사용자가 디지털 트윈의 상태를 모니터링하고, 분석하고, 의사 결정을 내릴 수 있도록 합니다.

알림 시스템: 특정 조건(예: 임계값 초과 시)에 따라 사용자에게 알림을 전송하는 기능을 추가

# 2. 기술 스택
```
Django: 웹 애플리케이션 프레임워크
Django REST Framework (DRF): API 구축을 위한 라이브러리
데이터베이스: PostgreSQL, MySQL 등
Frontend: HTML, CSS, JavaScript, React
데이터 시각화 라이브러리: Chart.js, D3.js 등
센서 통신 프로토콜: MQTT 또는 REST API.
```

# 3. 확장성
분석 및 머신러닝: 수집된 데이터를 기반으로 예측 모델을 구축하여 장비의 성능을 최적화하거나 유지보수 예측을 할 수 있습니다.

스마트폰 앱: Django REST API를 사용하여 모바일 애플리케이션을 개발하여 사용자 편의성을 높일 수 있습니다.

# 시군구별전력사용량 예측 및 비교

2024년 4월까지의 시군구별 전력 데이터를 시계열로 예측한 5월의 전력사용량을 실제 5월의 전력사용량과 비교하여
오차값을 통해 인사이트를 얻어보았다.

결과에 따른 가장 오차가 큰 시군구중 눈에 띄는 시군구는 광양, 포항, 울산남구, 평택, 당진 등
각자 대기업의 전력사용이 큰 곳으로 나타나는것을 확인할 수 있었다.

![image](https://github.com/user-attachments/assets/eb1aea19-ef11-486b-90dd-56c196945ac7)

결과에 따라 오차가 작은 시군구는 주거지역으로 연내 안정적으로 전기수요가 유지되는곳으로 보인다.

![image](https://github.com/user-attachments/assets/564b9ef8-204f-40e1-a69d-8fdefcce487c)

MAE MSE 오차를 다음과 같이 그래프로 나타내어 보았다.

![image](https://github.com/user-attachments/assets/f508db8c-d872-4b66-90e3-bef15b993671)


해당 결과뿐만이 아닌 이전 30년의 의 데이터 또한 취합하여 분석해본다면 어느 시점에 어느 지역에 전력 소모량이 늘어나는지 알 수 있을 것으로 보이며 이를 통한 전력망 관리에 자동화와 지능화에 기여할 수 있을 것으로 보인다

# 디지털 트윈 온도계 시뮬레이션
![image](https://github.com/user-attachments/assets/f03e9697-36e1-4047-89bc-e6239a22a61b)
