scores = []
for _ in range(8):
    score = int(input())
    scores.append(score)
ss = sorted(scores, reverse=True)
print(sum(ss[:5]))
for idx, score in enumerate(scores):
    if score >= ss[4]:
        print(idx + 1, end=" ")
