"""17299 오등큰수"""
# 풀이: https://velog.io/@wlrhkd49/%EB%B0%B1%EC%A4%80-17299-%EC%98%A4%EB%93%B1%ED%81%B0%EC%88%98-Python
import sys
from collections import Counter

INPUT = sys.stdin.readline


def ngf(n: int, arr: list) -> list:
    cnt, ans = Counter(arr), [-1 for _ in range(n)]
    stack = []
    for i in range(n):
        while stack and cnt[arr[stack[-1]]] < cnt[arr[i]]:
            ans[stack.pop()] = arr[i]
        stack.append(i)
    return ans


if __name__ == "__main__":
    N = int(INPUT())
    ARR = list(map(int, INPUT().split()))
    print(*ngf(N, ARR))
