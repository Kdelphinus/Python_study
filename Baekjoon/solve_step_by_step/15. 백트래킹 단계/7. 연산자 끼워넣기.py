"""14888 연산자 끼워넣기"""

from itertools import permutations


# 파이썬과 나누기 방식이 다르기에 함수로 정의
def divide(a, b):
    if a < 0:
        a *= -1
        anw = a // b
        anw *= -1
        return anw
    else:
        return a // b


n = int(input())  # 숫자의 개수
num = list(map(int, input().split()))  # 숫자
oper = list(map(int, input().split()))  # (+, -, *, /)순서로 연산자의 수를 받음

opers = []  # 가능한 모든 연산자 조합을 저장할 리스트
nums = []  # 구해진 숫자들을 모을 리스트
value = num[0]  # 연산의 첫 시작은 항상 첫번째 숫자

for i in range(4):  # p: +, m: -, x: X, d: //
    for j in range(oper[i]):
        if i == 0:
            opers.append("p")
        elif i == 1:
            opers.append("m")
        elif i == 2:
            opers.append("x")
        else:
            opers.append("d")

opers = list(map("".join, permutations(opers)))

for oper in opers:
    for i in range(len(oper)):
        if oper[i] == "p":
            value += num[i + 1]
        elif oper[i] == "m":
            value -= num[i + 1]
        elif oper[i] == "x":
            value *= num[i + 1]
        else:
            value = divide(value, num[i + 1])

    nums.append(value)
    value = num[0]

print(max(nums))
print(min(nums))
