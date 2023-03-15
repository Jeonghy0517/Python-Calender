# Python-Calender
## Datetime 라이브러리를 활용한 캘린더 프로그램
---
### 사용한 Python 라이브러리

+ **datetime**

  * 날짜와 시간 데이터를 처리하는 파이썬 내장 라이브러리

  * 현재 시간에 대한 정보를 가져와 원하는 형식으로 지정하여 사용할 수 있음
  
+ **strptime/strftime**
  
  * strptime : 날짜 형식 문자열을 datetime 객체로 변환 / 연(%Y), 월(%m), 일(%d), 시(%H), 분(%M), 초(%S)
  
  * strftime : 날짜와 시간 (datetime)을 문자열로 출력
  
+ **dateutil**
  
  * parse 함수를 통해 자동으로 날짜 형식을 찾아서 datetime 객체로 변환

+ **time**
  
  * datetime 라이브러리와 같이 파이썬에서 시간과 날짜를 다루기 위한 내장 라이브러리
  
  * 프로그램의 실행 경과 시간, 프로그램 대기 시간 등을 만들 때 주로 사용 
