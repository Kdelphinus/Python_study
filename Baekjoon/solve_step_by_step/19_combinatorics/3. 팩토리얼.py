"""10872 팩토리얼"""


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


n = int(input())
print(factorial(n))
