"""백준 17-11 문제와 동일"""
num = int(input())
# 2 * 5의 개수에 따라 뒤에 연속되는 0의 개수 결정
# 2는 너무 많기에 5의 제곱승들에 대해만 계산하면 됨
divide = [5 ** i for i in range(1, 15)]
anw = 0
for i in divide:
    anw += num // i
print(anw)
