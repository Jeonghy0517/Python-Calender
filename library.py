#날짜 및 요일 계산
#datetime : 날짜와 시간 데이터를 처리하는 파이썬 내장 라이브러리
#현재 시간에 대한 정보를 가져와 원하는 형식으로 지정하여 사용할 수 있음

#날짜/시간 표현 - datetime.date/datetime.datetime
import datetime
day1 = datetime.date(2023, 2, 22)
print(day1)

day2 = datetime.datetime(2023, 2, 22, 10, 48, 30)
print(day2)

#날짜/시간 합치기 - combine
day = datetime.date(2023, 2, 22)
time = datetime.time(10, 48, 30)
dt = datetime.datetime.combine(day, time)
print(dt)

#날짜 계산 - timedelta
day1 = datetime.date(2023, 2, 22)
day2 = datetime.date(2022, 11, 10)
diff = day1 - day2
print(diff)

plus = datetime.timedelta(days=100)
add = day1 + plus
print(add)

#요일 판별 - weekday
#월(0), 화(1), 수(2), 목(3), 금(4), 토(5), 일(6)
day1 = datetime.date(2023, 2, 22)
dat2 = datetime.date(2022, 2, 24)
print(day1.weekday())
print(day2.weekday())

#--------------------------------------------------------------------------------------------------------------------
#윤년 확인
#윤년 : 4년마다 돌아오는 2월이 29일까지 인 해
#연도가 4로 나누어 떨어지고 100으로 나누어 떨어지는 연도는 제외하거나 400으로 나누어 떨어지는 연도

def isLeapYear(year) :
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(isLeapYear(2022))
print(isLeapYear(2024))

#달력 관련 라이브러리 - calendar
import calendar
print(calendar.isleap(2022))
print(calendar.isleap(2020))

print(calendar.leapdays(1990, 2022)) #윤년 횟수

print(calendar.weekday(2023,2,22)) #요일 반환
print(calendar.calendar(2022)) #달력 출력

#--------------------------------------------------------------------------------------------------------------------
#날짜 출력
#strptime - 날짜 형식 문자열을 datetime 객체로 변환 / 연(%Y), 월(%m), 일(%d), 시(%H), 분(%M), 초(%S)
#strftime - 날짜와 시간(datetime)을 문자열로 출력
import datetime

str_datetime = '2022-02-22 11:15:11' #날짜 형식 문자열
currdate = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')
print(type(currdate))
print(currdate)

now = datetime.datetime.now()
print(now)

date = now.strftime('%Y-%m-%d')
print(type(date))
print(date)

time = now.strftime('%H:%M:%S')
print(type(time))
print(time)

datetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(type(datetime))
print(datetime)

#--------------------------------------------------------------------------------------------------------------------
#시간 관련 라이브러리
#dateutil : parse 함수를 통ㄹ해 자동으로 날짜 형식을 찾아서 datetime 객체로 변환
import datetime

#strptime 활용
date = '2022-10-15'
date_parsed = datetime.datetime.strptime(date, '%Y-%m-%d')
print(type(date_parsed))

#dateutil 활용
from dateutil.parser import parse
print(parse(date))

print(parse("Oct 15, 2022 04:05:32 PM")) #자동 형식 탐지

log = 'INFO 2023-01-01T00:00:01 Happy new year, human.' #날짜 문자열 자동탐지
print(parse(log, fuzzy=True))

#time : datetime 라이브러리와 같이 파이썬에서 시간과 날짜를 다루기 위한 내장 라이브러리
#프로그램의 실행 경과 시간, 프로그램 대기 시간 등을 만들 때 주로 사용
import time

print(time.time()) #현재 시간 출력 (실수형)
print(time.ctime()) #현재 시간 출력 (문자형)

#대기 시간 생성
print('바로 출력되는 구문')
time.sleep(3)
print('3초후 출력되는 구문')

#경과 시간 출력
start_time = time.time()

for i in range(5):
    time.sleep(1)
    print('반복 횟수', i+1)

end_time = time.time()
elapsed_time = end_time - start_time

print('경과시간은 %d 초 입니다.' % elapsed_time)




