"""10814 나이순 정렬"""

# 회원 수
n = int(input())

# 회원 정보가 들어갈 리스트
member = []

# 회원 정보 받기
for _ in range(n):
    age, name = input().split()
    age = int(age)
    name = str(name)
    member.append([age, name])

member.sort(key=lambda x: x[0])

for i, j in member:
    print(i, j)
