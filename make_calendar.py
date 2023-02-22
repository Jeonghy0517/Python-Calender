##달력 프로젝트##
#진행 순서
#1. 윤년 판별 함수
#2. 마지막 날짜 계산
#3. 지나온 날짜 계산
#4. 요일 반환
#5. 달력 확인

#--1. 윤년 판별 함수--#
def isYearLeap(year):
    year % 4 == 0 and year % 100 != 0 or year % 400 == 0

#--2. 마지막 날짜 계산--#
#lastDay 인수로 년, 월을 넘겨받아 그 달의 마지막 날짜를 리턴하는 함수

def lastDay(year, month):
    #각 달의 마지막 날짜를 기억하는 리스트 만들기
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #2월의 마지막 날짜가 윤년이면 29일로 수정
    if isYearLeap(year):
        m[1] = 29

    #마지막 날짜 리턴
    return m[month - 1]

#--3. 지나온 날짜 계산--#
# totalDay : 년, 원, 일을 넘겨받아 1년 1월 1일 부터 지난 날짜의 합계를 리턴하는 함수

# total 계산 순서
#1. 평년을 기준으로 전년도까지 일자 합계 -> 윤년이었던 횟수 더하기
#2. 전달까지 해당 연도 일자 더하기
#3. 이번달 날짜 더하기

def totalDay(year, month, day):
    #1년 1월 1일 부터 전 년도 12월 31일까지 지난 날짜를 합산
    total = (year - 1)*365 + (year-1)//4 - (year-1)//100 + (year-1)//400 #12월 31일까지 지난 날자 합산 + 윤년이었던 횟수 더함

    #전년도 까지 지난 날짜의 합계에 전 달까지 지난 날짜 더하기
    for i in range(1, month):
        total += lastDay(year, i) #윤년 확인 포함

    return total + day #전달 까지 지난 날짜에 이번달 날짜를 더해서 리턴

#--4. 요일 반환--#
#weekDay 인수로 년, 월, 일을 넘겨받아 요일을 계산해 숫자로 리턴하는 함수
#1년 1월 1일 부터 인수로 넘겨받은 년, 월, 일까지 지난 날짜의 합계를 7로 나눈 나머지 반환
#일요일(0), 월요일(1), 화요일(2), 수요일(3), 목요일(4), 금요일(5), 토요일(6)

def weekDay(year, month, day):
    return totalDay(year, month, day) % 7

#--5. 달력 확인--#
if __name__ == "__main__":

    #달력 프로그램 도입부
    year, month = map(int, input('달력을 출력할 년, 월을 입력하세요 : ').split()) #공백을 기준으로 변수에 정수를 넣음
    print('=' * 28)
    print('         {0:4d}년{1:2d}월'.format(year, month))
    print('=' * 28)
    print(' 일  월  화  수  목  금  토 ')
    print('=' * 28)

    #1일이 출력될 요일의 위치를 맞추기 위해 1일의 요일만큼 반복하여 빈칸을 출력
    for i in range(weekDay(year, month, 1)):
        print('    ', end = '')

    #1일부터 달력을 출력할 달의 마지막 날짜까지 반복하여 달력을 출력
    for i in range(1, lastDay(year, month) + 1):
        print(' {0:2d} '.format(i), end = '')

        #출력한 날짜(i)가 토요일이고 그 달의 마지막 날짜가 아니면 줄바꿈
        if weekDay(year, month, i) == 6 and i != lastDay(year, month):
            print()

    print('\n' + '=' * 28) #달력 하단