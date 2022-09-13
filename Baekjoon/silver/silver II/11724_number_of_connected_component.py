import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

check = [0] * 1001


def dfs(graphs: list, cnt: int, i: int):
    for g in graphs[i]:
        if check[g]:
            continue
        check[g] = cnt
        dfs(graphs, cnt, g)


def main():
    cnt = 0
    n, m = map(int, input().split())
    graphs = [[] for _ in range(n + 1)]
    for _ in range(m):
        n1, n2 = map(int, input().split())
        graphs[n1].append(n2)
        graphs[n2].append(n1)
    for i in range(1, n + 1):
        if not check[i]:
            cnt += 1
            check[i] = cnt
            dfs(graphs, cnt, i)
    return cnt


if __name__ == "__main__":
    print(main())
