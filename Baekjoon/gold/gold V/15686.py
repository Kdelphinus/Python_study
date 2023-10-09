import sys
from collections import defaultdict
from itertools import combinations

INPUT = sys.stdin.readline


def find_chicken_dist(limit: int, home: list, chicken: list) -> int:
    ans, chicken_dist = 0, defaultdict(list)
    for idx, (hy, hx) in enumerate(home):
        for cy, cx in chicken:
            chicken_dist[f"{hx}, {hy}"].append(abs(hy - cy) + abs(hx - cx))
        ans += min(chicken_dist[f"{hx}, {hy}"])

    if len(chicken) == limit:
        return ans

    comb = list(combinations(range(len(chicken)), len(chicken) - limit))
    ans = float("inf")
    for com in comb:
        tmp = 0
        for h in chicken_dist.values():
            tmp2 = float("inf")
            for idx, d in enumerate(h):
                if idx in com:
                    continue
                tmp2 = min(tmp2, d)
            tmp += tmp2
        ans = min(ans, tmp)

    return ans


if __name__ == "__main__":
    N, M = map(int, INPUT().split())
    HOME, CHICKEN = [], []
    for i in range(N):
        TMP = list(map(int, INPUT().split()))
        for j, v in enumerate(TMP):
            if v == 1:
                HOME.append((i, j))
            elif v == 2:
                CHICKEN.append((i, j))
    print(find_chicken_dist(M, HOME, CHICKEN))
