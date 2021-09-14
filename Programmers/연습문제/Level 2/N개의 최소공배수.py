"""연습문제"""


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solution(arr):
    if len(arr) == 1:
        return arr[0]

    lcd = arr[0] * arr[1] / gcd(arr[0], arr[1])
    for i in range(2, len(arr)):
        lcd = lcd * arr[i] / gcd(arr[i], lcd)

    return lcd


print(solution([2, 6, 8, 14]))  # 168
print(solution([1, 2, 3]))  # 6
