total = 0
for _ in range(5):
    score = int(input())
    total += 40 if score < 40 else score
print(int(total / 5))
