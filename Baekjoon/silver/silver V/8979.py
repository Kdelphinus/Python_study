n, m = map(int, input().split())
target, nation = [], []
for _ in range(n):
    tmp = list(map(int, input().split()))
    num, tmp_lst = tmp[0], tuple(tmp[1:])
    nation.append(tmp_lst)
    if num == m:
        target = tmp_lst

nation.sort(key=lambda x: (-x[0], -x[1], -x[2]))
print(nation.index(target) + 1)
