import sys
from collections import defaultdict

INPUT = sys.stdin.readline


def main():
    block = defaultdict(int)
    n, m, b = map(int, INPUT().split())
    for _ in range(n):
        for i in map(int, INPUT().split()):
            block[i] += 1
    change, final = float("inf"), float("inf")
    height = sorted(list(block.keys()), reverse=True)
    for h in range(height[0] + 1):
        c_b = b
        c_change = 0
        for h2 in height:
            if h == h2:
                continue

            tmp = abs(h - h2) * block[h2]
            if h > h2 and c_b >= tmp:
                c_change += tmp
                c_b -= tmp
            elif h < h2:
                c_change += tmp * 2
                c_b += tmp
            else:
                break
        else:
            if change > c_change or (change == c_change and final < h):
                change, final = c_change, h
    return change, final


if __name__ == "__main__":
    result = list(main())
    print(*result)
