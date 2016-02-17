#-*- coding: utf-8 -*-

########################### 1장 #######################
# 1. 현재 버젼 정보 보기
import sys
print sys.version
print
print sys.version_info

# 2. 달력보기
import calendar
calendar.prmonth(2016, 2)      # 년, 월

########################### 2장 #######################
# 1. 예약어 종류보기
import keyword
print keyword.kwlist
print
print len(keyword.kwlist)

# - 정수 형태의 ASCll코드 값을 입력으로 받아 그에 해당하는 문자를 반환하는 함수
# - 인수 i의 범위: 0부터 255까지
print chr(97)
print chr(65)
print chr(48)

# - 임의의 객체 object에 대해 해당 객체를 표현하는 문자열을 반환하는 함수
print str(3)
print str([1, 2])


# ＼(\ 백슬래시) → 나눠진 줄을 한 줄로 인식하도록 함
# ＼(\ 백슬래시)는 코딩이 길어져 한 화면에 나타나지 않을 때 사용
# 두 문장을 한 줄에 이어 쓸 때 세미콜론(;)을 사용. 세미콜론(;)은 프로그램 가독성 문제로 자주 활용되지 않음
a = 1; b = 3
if (a == 1) and \
(b == 3) :
    print 'connected lines'

# • 두 변수의 값을 swap하는 방법
e = 3.5; f = 5.6
e, f = f, e
print e, f



a = [1, 2, 3]
b = [10, a, 20]
c = ['a', a, 'b']
print a
print b
print c


# 콘솔을 통해 내용을 입력 받는 함수 → raw_input(), input()
# raw_input() → 콘솔창에서 문자열을 입력받는 내장 함수
# name = raw_input('name을 입력하세요 : ')
# print name

# input(): 정수, 실수, Expression 입력 내장함수. 문자열 입력받는 raw_input()과 달리 연산식까지 입력 가능
# i = input('int값을 입력하세요 : ')
# print i

# 콤마(,) → 여러 자료를 한 번에 출력할 때 결과 사이를 한 칸 씩 띄어줌
# 세미콜론(;) → 각 문장의 줄을 분리
# 기본적으로 print는 마지막에 줄바꿈을 하지만 콤마(,)가 마지막에 있으면 줄바꿈을 하지 않는다.

print 1+2, 3+4
print 5; print 6
print 7,
print 8

########################### 3장 #######################
# 정수형 상수
a = 23 # 10진 정수
b = 023 # 8진 정수
c = 0x23 # 16진 정수
print type(a), type(b), type(c)
print a, b, c


import sys
print sys.maxint # 최대 정수 값 확인

# 실수형 상수
a = 1.2
b = 3.5e3
c = -0.2e-4
print type(a), type(b), type(c)
print a, b, c

