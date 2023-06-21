"""10870 피보나치 수 5"""


def Fib(num):
    if num == 0:
        return 0
    elif num <= 2:
        return 1
    else:
        return Fib(num - 1) + Fib(num - 2)


n = int(input())
print(Fib(n))
