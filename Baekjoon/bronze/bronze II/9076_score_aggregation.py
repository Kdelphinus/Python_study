t = int(input())
for _ in range(t):
    score = sorted(map(int, input().split()))
    print(sum(score[1:4]) if score[3] - score[1] < 4 else "KIN")
