# -*- coding: utf-8 -*-

#############################################
# raw_input() 내장 함수를 통해 사용자에게 Standard Input을 받을 수 있습니다.
result = raw_input("무엇이든 입력해보세요.")
print "당신이 입력한 내용은 {0}입니다.".format(result)


#############################################
# raw_input()을 이용해 사용자 인터랙티브한 프로그램(숫자 맞추기 게임)을 만들어봅시다.

# 차후에 배우겠지만, 랜덤(임의)한 값을 만들어내기 위해 random이라는 python 기본 라이브러리를 사용합니다.
import random

# 재사용 가능하도록 number_game() 함수를 만듭니다.
def number_game():

    answer = random.randrange(1, 11)  # 1부터 10의 임의의 정답을 만듭니다.
    life = 3  # 목숨은 게임의 룰에 따라 세 개로 정합니다.

    while life > 0:  # 목숨이 존재하는 한, while문을 통해 루프(여기서는 게임 그 자체)를 계속 돌도록 만듭니다.
        user_input = raw_input("1부터 10까지의 숫자를 맞춰보세요. (남은 목숨: {0}개)".format(life))  # 이전에 배운 raw_input()함수를 통해 사용자 입력을 받습니다.

        user_input_int = int(user_input)  # raw_input()으로 입력받은 정보는 문자열형(str)이므로, int()를 통해 정수형(int)으로 치환(casting) 해줍니다.
        if user_input_int == answer:
            print "정답입니다! 게임을 종료합니다."
            return  # 정답을 맞춘 경우 게임을 바로 종료(함수를 return)합니다.
        elif user_input_int > answer:  # 정답이 아닌 경우(입력값이 정답보다 크거나 작은 경우) 사용자에게 힌트를 알려주고 목숨을 하나 차감합니다.
            print "{0}보다 작습니다.".format(user_input_int)
            life -= 1
        elif user_input_int < answer:
            print "{0}보다 큽니다.".format(user_input_int)
            life -= 1

    # while문을 빠져나왔다는 것은 목숨이 모두 없어진 상태(사용자의 패배)이므로, 실제 정답을 알려주고 게임을 종료합니다.
    print "정답은 {0}였습니다!".format(answer)

number_game()

#############################################
# Python에서는 Standard Input 외에 File에서도 사용자 입력을 받을 수 있습니다.

# 윈도우의 경우
f = open("c:\\python_lecture.txt", "w")  # \는 escape 문자라고 하여, 단독으로 사용될 수 없습니다. \문자를 사용하고 싶다면 \\ 이렇게 두개를 입력해주어야 합니다.
# 맥(Unix 계열)의 경우
f = open("/tmp/python_lecture.txt", "w")


# "w"모드로 열였기 때문에, 파일을 (새로) 쓸 수 있습니다.
# 뭔가 해봅시다.
for i in range(1, 11):
    text = "여기는 {0}번 째 줄입니다.".format(i)
    f.write(text)  # write() 함수를 통해 직접 쓸 수 있습니다.

f.close()  # 파일 사용이 끝난 이후에는 반드시 close()해 주어야 다른 프로그램이 해당 파일을 조작할 수 있습니다.


# 이번에는 읽기 모드로 열어보겠습니다.
f = open("/tmp/python_lecture.txt", "r")

# while문을 돌면서, 파일의 끝(아무것도 읽히지 않는 상황)이 올 때 까지 파일을 한 줄씩 읽어 Standard output에 출력하는(print) 모습입니다.
while True:
    line = f.readline()

    if not line:
        break

    print line


f.close()

##############################################
# 특정 파일을 열어 한 줄 씩 읽으면서, 띄어쓰기 기준으로 어떤 단어가 얼마나 쓰였는지 숫자를 세는 프로그램입니다.
# 수업시간에는 위대한 개츠비 소설을 가지고 연습해보았었습니다.

def get_word_cnt(file_path):

    # get total file count
    result = {}

    f = open(file_path, "r")
    while True:
        line = f.readline()
        if not line:
            break
        # print line
        words = line.split()
        for word in words:
            if word in result:
                result[word] += 1
            else:
                result[word] = 1

    f.close()

    return result

result = get_word_cnt("./gatsby.txt")
print result


##############################################
# 절대값을 돌려주는 내장 함수 abs()입니다.
a = -10
print abs(a)


fruits = {
    'grape': 10000,
    'apple': 2000,
    'lemon': 3000
}

# 무엇이든 list형으로 캐스팅해줍니다.
print list("Hello!")

# map() 함수입니다. 일전에 배웠던 List Comprehension이랑 비슷함을 알 수 있습니다.
a = [1, 2, 3, 4, 5]
def make_double(x):
    return x*2

print map(make_double, a)
print [x * 2 for x in a]  # List comprehension이랑 비슷.


# enumerate()를 통해 루프의 순서를 알 수 있습니다.
for i, key in enumerate(fruits):
    print i, key, fruits[key]  # 순서, 키, 값을 동시에 출력함

# for문에서 사용하던 range는 사실..
print range(1, 11)

# sorted()함수를 통해 내림차순, 올림차순 정렬을 할 수 있습니다.
a = [1, 5, 2, 3, 5, 7, 8, 1, 3]
sorted_a = sorted(a)
desc_sorted_a = sorted(a, reverse=True)
print desc_sorted_a


# 우리는 객체지향 프로그래밍(OOP)과 클래스의 개념에 대해 공부해보았습니다.

# 사람이라는 클래스를 만들었습니다.
class Person():

    # 사람은 이름과 나이라는 속성을 가지고 있습니다.
    name = ""
    age = 0

    # __init__()이라는 특수한 함수(메소드)를 사용하여 객체를 초기화 할 수 있습니다.
    def __init__(self, name, age):

        self.name = name
        self.age = age

    # 사람은 말을 하는 기능(메소드, 인터페이스)을 가지고 있습니다.
    def talk(self):

        print "내 이름은 {0}입니다. 나는 {1}살입니다.".format(self.name, self.age)

# 이렇게 Person이라는 빵틀(클래스)을 이용해 실제 빵(객체)를 찍어내는 모습입니다.

iu = Person("아이유", 23)
print iu.name
print iu.age
iu.talk()

sh = Person("설현", 100)
print sh.name
print sh.age
sh.talk()

# 사람 클래스를 상속받은 (확장된)배우 클래스를 만들었습니다. 배우는 사람의 기본 속성에 출연한 영화 목록을 가지고 있는 클래스입니다.
class Actor(Person):

    movies = []

# 사람 클래스의 모든 것들을 상속 받았기 때문에, 사람 클래스가 가지고 있던 속성과 기능을 모두 가지고 있습니다.
tom = Actor("톰행크스", 60)
print tom.name
tom.talk()


# 영화 클래스를 만들었습니다.
class Movie():

    name = ""
    year = 1970

    def __init__(self, name, year):
        self.name = name
        self.year = year


# tom 객체의 출연 영화에, 아까 만든 영화 클래스를 이용해 영화들을 추가해주었습니다.
tom.movies.append(Movie("라이언 일병 구하기", 2000))
tom.movies.append(Movie("캐스트 어웨이", 2001))
tom.movies.append(Movie("터미널", 2009))

for m in tom.movies:
    print m.name, m.year