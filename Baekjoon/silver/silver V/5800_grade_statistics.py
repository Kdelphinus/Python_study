k = int(input())
for i in range(k):
    num = list(map(int, input().split()))
    num, score = num[0], sorted(num[1:])
    gap = 0
    for j in range(num - 1):
        gap = max(score[j + 1] - score[j], gap)
    print(f"Class {i + 1}\nMax {score[-1]}, Min {score[0]}, Largest gap {gap}")
