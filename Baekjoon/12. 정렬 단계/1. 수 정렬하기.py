"""2750 수 정렬하기"""

# n개의 숫자가 주어진다
n = int(input())

# 숫자를 담을 리스트
num = []

# n개의 숫자를 받는다
for _ in range(n):
    temp = int(input())
    num.append(temp)

# 정렬 함수
num.sort()

# 차례대로 출력
for i in range(n):
    print(num[i])