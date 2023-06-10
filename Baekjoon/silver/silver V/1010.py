"""1010 다리놓기"""

from math import factorial

test = int(input())

# 다리가 서로 겹치지 않아야 하기에 end C start라는 조합이 경우의 수가 된다
for _ in range(test):
    start, end = map(int, input().split())  # 시작하는 위치와 끝나는 위치의 개수
    result = factorial(end) // (factorial(start) * factorial(end - start))
    print(result)
