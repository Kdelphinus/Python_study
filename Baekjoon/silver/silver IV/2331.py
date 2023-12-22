import sys

INPUT = sys.stdin.readline


def divide_cal(num: int, pow: int) -> int:
    ans = 0
    while num > 0:
        ans += (num % 10) ** pow
        num //= 10
    return ans


A, P = map(int, INPUT().split())
lst = [A]
while True:
    tmp = divide_cal(lst[-1], P)
    if tmp in lst:
        break
    lst.append(tmp)

print(lst.index(tmp))
