"""2108 통계학"""
from collections import Counter


def aritmeticMean(num):
    """산술 평균을 구하는 함수"""
    return "{0:.0f}".format(sum(num) / len(num))


def median(num):
    """중앙값을 구하는 함수"""
    return num[len(num) // 2]


def mode(num):
    """최빈값을 구하는 함수"""
    count = Counter(num).most_common()  # (수, 들어있는 수의 개수)를 리턴함, 자세한 건 여러 기능들 참고

    if len(num) > 1:
        if count[0][1] == count[1][1]:
            return count[1][0]
        else:
            return count[0][0]
    else:
        return count[0][0]


def reach(num):
    """범위를 구하는 함수"""
    return num[len(num) - 1] - num[0]


n = int(input())  # 수의 개수
num = []  # 수를 저장할 리스트

for _ in range(n):
    temp = int(input())
    num.append(temp)

num.sort()  # 정렬

print(aritmeticMean(num))
print(median(num))
print(mode(num))
print(reach(num))