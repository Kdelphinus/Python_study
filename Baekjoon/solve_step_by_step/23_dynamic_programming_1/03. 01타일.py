"""1904 01타일"""

num = int(input())

# 기본값
previous = 1
current = 1

# 피보나치 수열과 같은 형태를 보인다
for i in range(1, num):
    previous, current = current, (previous + current) % 15746

print(current)
