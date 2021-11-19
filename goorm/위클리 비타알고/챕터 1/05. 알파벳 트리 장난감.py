height = int(input())
max_tree = [[] for _ in range(height)]
min_tree = [[] for _ in range(height)]

for h in range(height):
    level = input()
    for l in level:
        max_tree[h].append(ord(l) - 64)
        min_tree[h].append(ord(l) - 64)
        
for idx in range(height - 2, -1, -1):
	for i in range(len(max_tree[idx])):
		j = (i + 1) * 2 - 1
		max_tree[idx][i] = max_tree[idx][i] + max(max_tree[idx + 1][j - 1], max_tree[idx + 1][j])
		min_tree[idx][i] = min_tree[idx][i] + min(min_tree[idx + 1][j - 1], min_tree[idx + 1][j])
		

print(min_tree[0][0])
print(max_tree[0][0])
