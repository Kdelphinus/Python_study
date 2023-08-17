# 냅색 문제에 비트마스크 개념을 추가하여 풀어야 한다.
# https://dreamtreeits.tistory.com/178
import sys

INPUT = sys.stdin.readline


def backpack() -> int:
    dp = [0 for _ in range(M + 1)]
    for w, c in OBJECTS:
        for i in range(M, w - 1, -1):
            dp[i] = max(dp[i], dp[i - w] + c)
    return dp[M]


if __name__ == "__main__":
    N, M = map(int, INPUT().split())
    OBJECTS = []
    for _ in range(N):
        V, C, K = map(int, INPUT().split())
        IDX = 1
        while 0 < K:
            m = min(IDX, K)
            OBJECTS.append((V * m, C * m))
            K -= IDX
            IDX *= 2
    print(backpack())
