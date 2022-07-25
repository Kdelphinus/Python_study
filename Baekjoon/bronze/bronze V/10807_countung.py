# 메모리나 시간 모두 단순 반복문이 조금씩 좋다. 그러나 거의 비슷함
n = int(input())

# 1. 반복문 사용
cnt = 0
num = list(map(int, input().split()))
check = int(input())
for i in num:
    if i == check:
        cnt += 1
print(cnt)

# 2. Counter 사용
# from collections import Counter
# cnt = Counter(list(map(int, input().split())))
# print(cnt[int(input())])
