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

# 롱형: 정수형 상수의 최대 범위를 벗어난 수
# 롱형은 메모리가 허용하는 한 유효자리 수가 무한
# 롱형을 명시하는 방법 → 숫자 끝에 L을 붙여줌

h1 = 123456789012345678901234567890L
# 마지막에 L을 붙여서 명시적으로 long 형이라고 알려도 되고
# L을 붙이지 않아도 int형이 담을 수 있는 수치를 초과하면 자동으로 long형이 된다.
print type(h1)


# 복소수형 상수: 실수부(ex. 10)와 허수부(ex. 20j)로 구성. 복소수형 상수는 실수부와 허수부가 각각 계산됨
a = 10 + 20j
print a
b = 10 + 5j
print a + b

# math 모듈의 수치 연산 함수
import math
print math.pi       # 파이값
print math.e        # 지수값
print math.sin(1.0) # 1.0 라디안에 대한 사인 값
print math.sqrt(2)  # 제곱근

# 문자열을 만들 때에는 단일 따옴표 또는 이중 따옴표를 사용. 사용 시 차이 없으므로 선택적으로 사용 가능
# 문자열 안에서 따옴표를 쓸 필요가 있을수 있으므로 둘다 사용 가능하게 하였음.
# 여러 줄의 문자열을 만들 때에는 ''' ''' 또는 """ """ 사용

# 인덱싱
s = "Hello world!"
print s[0]
print s[-1]     # 마이너스는 뒤에서 부터. 가장 뒷 문자를 불러올때 유용.(마이너스(-1) 사용)

# 슬라이싱
# 문자열 자료형은 내부 내용 변경 불가능. s[0] = 'm' 형태로 수정이 불가능함.
# 문자열 내의 문자를 바꿀 수 없으므로 주의. 문자형은 시퀀스형이 아니다.
# 문자열을 바꾸기 위해서는 슬라이싱을 활용

#  문자열 + 문자열 → 순서 그대로 두 문자열 연결
print 'Hello' + '' + 'World'       # → HelloWorld
#  문자열 * 숫자 → 숫자만큼 문자열 반복
print 'Hello' * 3                   # → HelloHelloHello

########################### 4장 #######################
# 사전(dictionary)
# Keys, values, items가 반환하고 있는 자료형 → 리스트. 아래 결과는 임의의 순서로 반환됨. 사전은 해시 순서로 저장, 반환됨.
d = {'one': 1, 'two': 'dul', 'three': 'set', 'four': 'net'}
print d.keys() # 키만 리스트로 추출함
print d.values() # 값만 리스트로 추출함
print d.items() # 키와 값의 튜플을 리스트로 반환함

print type(None) #None 객체, 아무 값도 없다(혹은 아니다)를 나타내는 객체

# id(): 객체의 식별자를 반환한다. 파이썬 인터프리터가 관리하는 식별자 출력
# 파이썬에서는 숫자를 따로 객체로 만들지 않음(이미 존재)

# is 키워드: 두 객체의 식별자가 동일한지 테스트한다.


c = [1,2,3]
d = [1,2,3]
print c is d            # 이게 다른 식별자를 가진다는게 의외.
a = 500
b = a
print a is b
x = 1
y = 1
print x is y            # 파이썬에서는 숫자를 따로 객체로 만들지 않음(이미 존재). 수치는 새로 만들어지지 않고 이미 존재하므로 두값은 같은 식별자.
e = f = [4,5,6]         # f의 레퍼런스를 e에 할당하는것이므로 두개가 같은 식별자를 갖는것은 ok.
print e is f

# == 연산자: 두 객체의 값이 동일한지를 테스트한다.
# c와 d는 서로 다른 객체를 가지지만 내용이 같으므로 True
# ==는 두 객체의 내용이 같은지 확인, is는 식별자가 같은지 확인
c = [1,2,3]
d = [1,2,3]
print c == d

########################### 5장 #######################
# //: %에 대응되는 연산자 = 몫을 구해주는 연산자
# / = 소수점 이하를 버리는 것. // = 몫을 구해서 출력
print 5 / 3
print 5 // 3

# 서로 다른 자료형간의 크기 관계 - 숫자 < 사전 < 리스트 < 문자열 < 튜플
L = [1,2,3, 'abc', 'a', 'z', (1,2,3), [1,2,3], {1:2}, ['abc']]
L.sort()
print L

# 진리값에 해당하는 True와 False는 다른 사칙연산자를 만나면 다음과 같이 평가됨
# True: 1 , False: 0

#  bool(불): 하나 받는 객체를 evaluate하여 true 또는 false로 반환
#  객체는 대부분 true지만 false로 변환되는 객체들이 존재
#  정수값 0은 bool(불) 내장함수에서 false로 evaluate 됨
#  0.0이 아닌 나머지 모든 실수 = true
# 값이 없는 빈 객체나 None 객체는 False로 평가됨


print [] or 1 # [] 거짓
print [] or ()      # []가 false므로 or에 의해 뒤를 확인해야되므로 뒤가 출력.
print [] and 1      # []가 false이므로 and에 의해 뒤를 볼필요도 없어서 []가 출력.
print
print 1 and 2       # 1이 true이더라도 and에 의해서 뒤를 확인해야되므로 2가 출력.
print 1 or 2        # 1이 true이므로 뒤에값은 보지도 않으므로 1이 출력됨.
print
print [[]] or 1     # [[]] 참으로 간주
print [{}] or 1     # [{}] 참으로 간주
print '' or 1       # 빈 문자열('')은 거짓

########################### 6장 #######################

# •enumerate() 내장 함수: 컨테이너 객체가 지닌 각 요소값뿐만 아니라 인덱스 값도 함께 반환한다.

# l = ['cat', 'dog', 'bird', 'pig']
l = ('cat', 'dog', 'bird', 'pig')
for k, animal in enumerate(l):
    print k, animal

d = {'c':'cat', 'd':'dog', 'b':'bird', 'p':'pig'}
for k, key in enumerate(d):
    print k, key, d[key]

# • continue: 루프 블록 내의 continue 이후 부분은 수행하지 않고 루프의 시작부분으로 이동한다.
for x in range(10):
    if x < 8:
        continue
    print x
print 'done'

# break에 의하여 루프를 빠져나가면 else 블록도 수행되지 않는다.
# else 블록은 for문이 break 걸리지 않고 정상적 수행 시 수행 가능
# else문은 while문에서도 쓰일 수 있고, for문에서도 쓰일 수 있음

########################### 7장 #######################

print 'ab' in 'abcd'
print 'ad' in 'abcd'
print ' ' in 'abcd'
print ' ' in 'abcd '
print '' in 'abcd'

# '한글' 문자열의 인코딩 방식을 'utf-8'형태로 인식시키면서 해당 문자열을 unicode로 변환
# unicode내장함수: unicode(문자열, 문자열 인식 방법)
a = unicode('한글', 'utf-8')
print type(a)
print a

print len('한글과 세종대왕')
print len(unicode('한글과 세종대왕', 'utf-8')) #유니코드 타입의 문자열은 한글 문자열 길이를 올바르게 반환함
print len(u'한글과 세종대왕')
# len(한글) X --> len(u’한글’) O

# 유니코드 타입의 한글 문자열에 대해서는 인덱싱 및 슬라이싱이 올바르게 수행됨.
# 유니코드가 아닐경우 위와같이 문자열을 정상적으로 인식하지 못해서 잘못된 결과가 나옴
u = '한글과 세종대왕'
print u[0]

u = u'한글과 세종대왕'
print u[1]
u = unicode('한글과 세종대왕', 'utf-8')
print u[0]
print u[1]
print u[:3]

########################### 8장 #######################


