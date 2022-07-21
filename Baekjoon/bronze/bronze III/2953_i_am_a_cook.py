winner = 0
top_score = 0
for i in range(1, 6):
    score = sum(map(int, input().split()))
    if top_score < score:
        top_score = score
        winner = i
print(f"{winner} {top_score}")
