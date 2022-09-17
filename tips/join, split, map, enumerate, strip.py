"""1. split()"""
"""() 안 함수 인자로 문자열을 나눌 기준을 입력 받아 문자열을 나눔"""

text = "Hello World/It's good day"
print(text.split("/"))  # ['Hello World', "It's good day"]

text = "aa   cc"
# split()안에 아무것도 없으면 공백을 제외하고 나눔
print(text.split())  # ['aa', 'cc']

# 공백을 쓰면 공백도 포함하여 나눔
print(text.split(" "))  # ['aa', '', '', 'cc']


"""2. join()"""
"""특정 문자열을 삽입하여 나뉘어 있던 문자열을 새로운 문자열로 합쳐줌"""
a = ["a", "b", "c", "d"]
print("".join(a))  # abcd, 공백 없이 붙임
print(",".join(a))  # a,b,c,d  사이에 ,를 넣어줌


"""3. map()"""
"""함수(f)와 반복 가능한(iterable) 자료형을 입력 받음"""
num = [1.2, 3.3, 4.5, 5.6, 55.3]
number = list(map(int, num))
print(number)  # [1, 3, 4, 5, 55]


"""4. enumerate()"""
"""열거하다라는 의미로 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력받아 인덱스 값을 포함하는 enumerate 객체로 돌려줌"""
animal = ["lion", "panda", "dog"]

print(list(enumerate(animal)))  # [(0, 'lion'), (1, 'panda'), (2, 'dog')]

for i, name in enumerate(animal):
    print(i, name)

# 출력 결과
# 0 lion
# 1 panda
# 2 dog


"""5. strip()"""
"""공백을 제거하는 함수"""
text_1 = " asdf "
print(text_1.strip())  # asdf

"""strip으로 나누면 글자 하나하나가 리스트로 들어가지만 split은 정해진 구간으로만(기본은 띄어쓰기) 나누어 들어간다"""
text_2 = "1324568997"
print(list(text_2.strip()))  # ['1', '3', '2', '4', '5', '6', '8', '9', '9', '7']
print(list(text_2.split()))  # ['1324568997']
