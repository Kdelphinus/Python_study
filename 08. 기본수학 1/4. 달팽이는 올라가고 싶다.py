"""2869 달팽이는 올라가고 싶다"""

import math

A, B, V = map(int, input().split())  # A: 올라가는 높이 B: 미끄러지는 높이 V: 나무 높이
# 1 <= B < A <= V <= 1,000,000,000
day = math.ceil(((V - A) / (A - B))) + 1
print(day)
