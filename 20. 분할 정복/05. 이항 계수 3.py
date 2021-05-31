"""11401 이항 계수 3"""

""" 페르마의 소정리
정수 a와 a의 배수가 아니면서 소수(prime number)인 p는 다음 식을 성립한다
-> (a ** p) % p = a

위 식을 토대로 밑의 식도 유추할 수 있다
-> (a ** (p - 1)) % p = 1
-> (a ** (p - 2)) % p = a ** (-1) = 1 / a"""

import sys

input = sys.stdin.readline
p = 1000000007
n, k = map(int, input().split())


def power(number, num):
    if num == 0:  # 제곱수가 1일 때
        return 1
    else:
        if num % 2 == 0:  # 제곱수가 짝수일 때
            return (power(number, num // 2) ** 2) % p
        else:  # 제곱수가 홀수일 때
            return (power(number, num // 2) ** 2 * number) % p


fact = [1 for _ in range(n + 1)]
for i in range(2, n + 1):
    fact[i] = fact[i - 1] * i % p

# 이항계수를 구하는 식의 분자, 분모
numerator = fact[n]  # 분자
denominator = fact[k] * fact[n - k]  # 분모


""" 답을 구하는 식이 나오는 과정
(numerator * (denominator ** -1)) % p
= (numerator * ((denominator ** (p-2)) % p)) % p"""
print((numerator * (power(denominator, p - 2)) % p) % p)