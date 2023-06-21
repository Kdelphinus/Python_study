"""11399 ATM"""

num = int(input())  # 줄 선 사람의 수
withdraw = sorted(list(map(int, input().split())))  # 인출할 금액을 오름차순으로 정렬
sum = 0  # 총 걸리는 시간
tem = 0  # 지금 사람이 기다리는 시간

# 모두 더해준다
for i in withdraw:
    tem += i
    sum += tem

print(sum)
