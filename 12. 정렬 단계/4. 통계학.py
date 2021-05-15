"""2108 통계학"""

# 수의 개수
n = int(input())

# 수를 저장할 리스트
num = []

# 수가 주어진다
for _ in range(n):
    temp = int(input())
    num.append(temp)

# 리스트 정렬
num.sort()

# 산술 평균
print("{0:.0f}".format(sum(num) / len(num)))

# 중앙값
print(num[len(num) // 2])

# 최빈값
from collections import Counter

count = Counter(num).most_common()

if len(num) > 1:
    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])

# 범위
print(num[len(num) - 1] - num[0])