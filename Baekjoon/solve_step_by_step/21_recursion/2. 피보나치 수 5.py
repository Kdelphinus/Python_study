"""10870 피보나치 수 5"""


def fib(num):
    if num == 0:
        return 0
    elif num <= 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


n = int(input())
print(fib(n))
