""" 함수를 받을 때, optional parameter를 지정하면 값을 입력받지 않아도 됨 """
# 밑의 함수에서 리스트만 입력해도 작동 가능
def quicksort(my_list, start=0, end=None):
    pass


# -----------------------------------------------------------------------------------------

""" zfill """
print("1".zfill(6))  # 000001
print("333".zfill(2))  # 333
print("a".zfill(8))  # 0000000a
print("ab".zfill(8))  # 000000ab
print("abc".zfill(8))  # 00000abc

# -----------------------------------------------------------------------------------------

""" random 모듈 """
from random import randint, uniform

x = randint(1, 20)  # 1 이상, 20 이하의 임의의 정수 x를 리턴
y = uniform(0, 1)  # 0 이상, 1 이하의 임의의 소수 y를 리턴

# -----------------------------------------------------------------------------------------

""" *args """
# *args를 사용하여 이름의 개수를 미리 지정하지 않는다. Names에는 tuple형태로 저장
def Lastname_and_Fisrtname(*Names):
    """이름을 받아 출력하는 함수"""
    for name in Names:
        print("{}".format(name), end=" ")
    print("\n")


Lastname_and_Fisrtname("유재석", "박명수")  # 유재석 박명수
Lastname_and_Fisrtname("유재석")  # 유재석
Lastname_and_Fisrtname("유재석", "박명수", "정준하", "하하")  # 유재석 박명수 정준하 하하

# -----------------------------------------------------------------------------------------

""" **kwargs """
# **kwargs는 키워드 = ""로 입력할 경우 각각 키와 값을 가져오는 딕셔너리로 처리
def introduceEnglishName(**Names):
    for key, value in Names.items():
        print("{} is {}".format(key, value))


introduceEnglishName(고명준="Ko Myoung Jun")  # 고명준 is Ko Myoung Jun

# -----------------------------------------------------------------------------------------

""" 0과 1, True와 False """
a = True
if a:  # 'a는 True이다' 라는 가정문을 줄여쓴 것
    print("True")
else:
    print("False")

a = 0
if a:  # 숫자가 들어갈 땐, 0은 False, 나머지 숫자는 True
    print("a: 0이 아닌 수")
else:
    print("a: 0")

# -----------------------------------------------------------------------------------------

"""아스키 코드 변환"""
print(chr(65))  # A
print(ord("A"))  # 65

# -----------------------------------------------------------------------------------------

"""base64"""
"""8비트 이진 데이터를 문자 코드에 영향을 받지 않는 공통 아스키 영역의 문자들로만 이루어진 일련의 문자열로 바꾸는 인코딩 방식"""
"""구동 방식은 SWEA_delphinus/D2/1928. Base64 Decoder.py 참고"""
from base64 import b64decode

string = "TGlmZSBpdHNlbGYgaXMgYSBxdW90YXRpb24u"
print(f"{b64decode(string).decode('UTF-8')}")  # Life itself is a quotation.

# -----------------------------------------------------------------------------------------

"""replace"""
num_dic = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def solution(s):
    """영문으로 써진 숫자를 숫자로 바꿈"""
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)  # answer안에 있는 key를 value로 대체
    return int(answer)


print(solution("one4seveneight"))  # 1478


# -----------------------------------------------------------------------------------------

"""숫자인가? 영어인가?"""
string = "abcdefg"
print(string.isalpha())  # True
print(string.isdigit())  # False

number = "123456"
print(number.isalpha())  # False
print(number.isdigit())  # True

mix = "123abc"
print(mix.isalpha())  # False
print(mix.isdigit())  # False

# -----------------------------------------------------------------------------------------

"""소문자, 대문자"""
string = "abc"
string = string.upper()
print(string)  # ABC

string = string.lower()
print(string)  # abc

# -----------------------------------------------------------------------------------------

"""문자열로된 식 계산"""
ex1 = "5+2-9"
result1 = eval(ex1)  # -2, int형

ex2 = "5+2*"
result2 = eval(ex2)  # error, 계산이 가능한 식만 가능

# -----------------------------------------------------------------------------------------

import copy

"""얕은 복사"""
# 두 리스트는 다른 id를 가지나 내부 객체는 같은 메모리를 가리킴

# 얕은 복사는 id를 새로 부여받으며 재할당하는 것은 서로 영향을 주지 않는다
a = [[1, 2], [3, 4]]
b = copy.copy(a)  # 얕은 복사
# b = a[:]  # 슬라이싱도 얕은 복사

a[0] = [2, 3]  # 재할당
print(a)  # [[2, 3], [3, 4]]
print(b)  # [[1, 2], [3, 4]]

# 그러나 재할당 한 적 없는 값을 변경하면 같이 변경된다
a[1].append(5)
print(a)  # [[2, 3], [3, 4, 5]]
print(b)  # [[1, 2], [3, 4, 5]]


"""깊은 복사"""
# 깊은 복사는 내부 객체까지 모두 새롭게 복사

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)  # 깊은 복사
a[0].append(5)  # 값을 변경해도 영향받지 않음
print(a)  # [[1, 2, 5], [3, 4]]
print(b)  # [[1, 2], [3, 4]]

# -----------------------------------------------------------------------------------------

"""INF 사용"""
INF = float("inf")  # 무한대
M_INF = float("-inf")  # 음수 무한대

# 정수 최댓값, 최솟값
import sys

int_max = sys.maxsize  # 정수 최댓값
int_min = -(sys.maxsize + 1)  # 정수 최솟값

# -----------------------------------------------------------------------------------------

"""첫 알파벳만 대문자로 만들기(JadenCase)"""
text = "i am ko myoung jun."
print(text.capitalize())  # I am ko myoung jun.
print(" ".join([word.capitalize() for word in text.split(" ")]))  # I Am Ko Myoung Jun.
