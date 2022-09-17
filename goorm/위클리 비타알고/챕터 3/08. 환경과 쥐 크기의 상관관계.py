num = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_num = [0] * 100005
b_num = [0] * 100005

# m - 2 ~ m + 2의 범위를 m ~ m + 4로 바꾸어 카운팅
for a in A:
    for i in range(a, a + 5):
        a_num[i] += 1

for b in B:
    for i in range(b, b + 5):
        b_num[i] += 1

# 다시 m - 2 ~ m + 2로 범위 변경
# 가장 많은 횟수를 갖는 값이 대표값
a = a_num.index(max(a_num)) - 2
b = b_num.index(max(b_num)) - 2

print(a, b)
if a > b:
    print("good")
else:
    print("bad")
