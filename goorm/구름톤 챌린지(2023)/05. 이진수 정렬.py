N, K = map(int, input().split())
number = list(map(int, input().split()))
sort_lst = []
for num in number:
    sort_lst.append((bin(num).count("1"), num))
sort_lst.sort(key=lambda x: (-x[0], -x[1]))
print(sort_lst[K - 1][1])
