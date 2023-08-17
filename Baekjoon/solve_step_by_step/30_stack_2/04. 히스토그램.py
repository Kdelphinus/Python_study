"""1725 히스토그램"""
# 6549 히스토그램에서 가장 큰 직사각형과 동일

import sys

INPUT = sys.stdin.readline


def find_rectangle(hist: list) -> int:
    ans, stack = 0, []
    hist.append(0)

    for i, h in enumerate(hist):
        while stack and hist[stack[-1]] > h:
            ih = hist[stack.pop()]
            iw = i - stack[-1] - 1 if stack else i
            ans = max(ih * iw, ans)
        stack.append(i)

    return ans


if __name__ == "__main__":
    N = int(INPUT())
    histogram = [int(INPUT()) for _ in range(N)]
    print(find_rectangle(histogram))
