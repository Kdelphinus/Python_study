"""1427 소트인사이드"""

# 받은 수
n = int(input())

num = []

while n > 0:
    num.append(n % 10)
    n //= 10

num.sort()
ch = str(num[len(num) - 1])

for i in range(len(num) - 2, -1, -1):
    ch += str(num[i])

print(ch)
