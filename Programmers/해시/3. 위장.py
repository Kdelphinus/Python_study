"""나의 풀이"""
from collections import Counter


def solution(clothes):
    answer = 1
    type = []

    # 옷의 종류만 리스트에 저장
    for i in clothes:
        type.append(i[1])

    # 옷의 종류를 숫자로 저장
    types = list(Counter(type).values())

    # (옷의 개수 + 1)를 종류별로 곱해주면 안 입는 것부터 모두 착용하는 것까지 경우의 수가 나옴
    for i in types:
        answer *= i + 1

    # 안 입는 것을 제외하기 위해 1을 뺌
    return answer - 1


"""모범 답안"""


def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1