"""2981 검문"""


def gcd(a, b):
    """최대 공약수를 구하는 함수"""
    """math에 gcd라는 함수가 있음"""
    return gcd(b, a % b) if b else a


num = int(input())  # 주어지는 숫자의 개수
numbers = []  # 주어진 숫자가 저장되는 리스트
values = []  # 답이 저장되는 리스트

"""틀렸던 이유
틀린 답안: 가장 작은 차이 두 개의 최대공약수만 구했음
수정: 가장 작은 차이의 최대공약수만 구하는게 아니라 모든 차이의 최대공약수를 구해야 함"""

for i in range(num):  # 모든 수의 차이의 최대 공약수를 구한다
    numbers.append(int(input()))
    if i == 1:
        min_gcd = abs(numbers[1] - numbers[0])
    if i > 1:
        min_gcd = gcd(min_gcd, abs(numbers[i] - numbers[i - 1]))

root_min_gcd = int(min_gcd ** 0.5)  # 중복된 값을 방지하기 위해

for i in range(2, root_min_gcd + 1):  # 1과 자기 자신을 제외한 약수를 구한다
    if min_gcd % i == 0:
        values.append(i)
        values.append(min_gcd // i)
values.append(min_gcd)  # 자기 자신 추가
values = sorted(set(values))  # 정렬 및 중복 제거

for i in values:
    print(i, end=" ")
