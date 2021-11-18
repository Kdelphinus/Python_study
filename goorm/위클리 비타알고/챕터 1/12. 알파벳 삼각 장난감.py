height = int(input())
toy = [[] for _ in range(height)]
for h in range(height):
    for l in input().strip():
        toy[h].append(ord(l) - 64)  # 점수로 환산해서 저장

# 밑에서부터 큰 값을 더하며 올라온다
for i in range(height - 2, -1, -1):
    for j in range(len(toy[i])):
        toy[i][j] += max(toy[i + 1][j], toy[i + 1][j + 1])

print(toy[0][0])
