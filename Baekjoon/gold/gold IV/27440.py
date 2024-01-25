# 풀이 참고: https://www.acmicpc.net/source/61756160
import sys


INPUT = sys.stdin.readline
DP = {1: 0}


def make_one(num: int) -> int:
    if num in DP.keys():
        return DP[num]

    if num % 3 == 0 and num % 2 == 0:
        DP[num] = min(make_one(num // 2) + 1, make_one(num // 3) + 1)
    elif num % 3 == 0:
        DP[num] = min(make_one(num // 3) + 1, make_one(num - 1) + 1)
    elif num % 2 == 0:
        DP[num] = min(make_one(num // 2) + 1, make_one(num - 1) + 1)
    else:
        DP[num] = make_one(num - 1) + 1

    return DP[num]


if __name__ == "__main__":
    NUMBER = int(INPUT())
    print(make_one(NUMBER))
