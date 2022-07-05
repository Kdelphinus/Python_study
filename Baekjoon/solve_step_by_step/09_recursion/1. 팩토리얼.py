"""10872 팩토리얼"""


def Factorial(num):
    if num == 0:
        return 1
    else:
        return num * Factorial(num - 1)


n = int(input())
print(Factorial(n))
