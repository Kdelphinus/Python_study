from collections import defaultdict

player = defaultdict(int)
n = int(input())
for _ in range(n):
    player[input()[0]] += 1
player = sorted(list(player.items()), key=lambda x: (-x[1], x[0]))
ans = ""
for c, i in player:
    if i < 5:
        break
    ans += c
print("".join(sorted(ans))) if ans else print("PREDAJA")
