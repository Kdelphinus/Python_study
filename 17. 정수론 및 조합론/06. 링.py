"""3036 링"""

from math import gcd  # 최대 공약수를 구하는 함수

num = int(input())  # 링의 개수
radius = list(map(int, input().split()))  # 주어지는 링의 반지름들

for i in range(1, num):
    min_gcd = gcd(radius[0], radius[i])  # 기준이 되는 링과 현재 링의 최대 공약수
    print("{}/{}".format(radius[0] // min_gcd, radius[i] // min_gcd))  # 분수를 약분
