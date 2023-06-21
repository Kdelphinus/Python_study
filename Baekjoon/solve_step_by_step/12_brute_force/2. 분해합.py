"""2231 분해합"""


N = int(input())

num = 0

for i in range(1, N + 1):
    div_num = list(map(int, str(i)))
    sum_num = i + sum(div_num)
    if sum_num == N:
        num = i
        break

print(num)
