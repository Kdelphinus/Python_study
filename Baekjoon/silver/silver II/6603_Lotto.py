def lotto_case() -> None:
    if len(visited) == 6:
        for v in visited:
            print(v, end=" ")
        print()
    else:
        for n in lst:
            if visited and (n in visited or visited[-1] >= n):
                continue
            visited.append(n)
            lotto_case()
            visited.pop()


tc = list(map(int, input().split()))
while tc[0]:
    lst = tc[1:]
    visited = []
    lotto_case()
    tc = list(map(int, input().split()))
    if tc[0] == 0:
        break
    print()
