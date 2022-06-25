"""1629 곱셈"""
import sys

input = sys.stdin.readline

number, num, div_num = map(int, input().split())  # 숫자, 제곱 수, 나눌 수


def product(number, num):
    global div_num

    if num == 1:  # 제곱수가 1일 때
        return number % div_num
    else:
        temp = product(number, num // 2)

        if num % 2 == 0:  # 제곱수가 짝수일 때
            return (temp * temp) % div_num
        else:  # 제곱수가 홀수일 때
            return (temp * temp * number) % div_num


print(product(number, num))
