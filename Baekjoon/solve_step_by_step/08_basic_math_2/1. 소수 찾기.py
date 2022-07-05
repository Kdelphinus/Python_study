""" 1978 소수 찾기 """
test = int(input())
num = list(map(int, input().split()))
cnt2 = 0  #  소수의 개수

for i in num:
    cnt = 0  #  약수의 개수
    if i == 1:
        continue
    for j in range(1, i):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        cnt2 += 1
print(cnt2)
