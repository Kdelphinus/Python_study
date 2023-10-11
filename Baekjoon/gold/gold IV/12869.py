import sys
from collections import deque
from itertools import permutations

INPUT = sys.stdin.readline


def mutalisk() -> int:
    queue = deque([(SCV[0], SCV[1], SCV[2], 0)])
    while queue:
        scv1, scv2, scv3, cnt = queue.popleft()

        if scv1 <= 0 and scv2 <= 0 and scv3 <= 0:
            return cnt

        scv1 = 0 if scv1 <= 0 else scv1
        scv2 = 0 if scv2 <= 0 else scv2
        scv3 = 0 if scv3 <= 0 else scv3

        if DP[scv1][scv2][scv3] <= cnt:
            continue
        DP[scv1][scv2][scv3] = cnt

        for i in permutations((9, 3, 1), 3):
            queue.append((scv1 - i[0], scv2 - i[1], scv3 - i[2], cnt + 1))


if __name__ == "__main__":
    N = int(INPUT())
    SCV = list(map(int, INPUT().split()))
    while len(SCV) < 3:
        SCV.append(0)

    # 각 인덱스가 SCV의 체력
    DP = [
        [[float("inf") for _ in range(max(SCV) + 1)] for __ in range(max(SCV) + 1)]
        for ___ in range(max(SCV) + 1)
    ]
    print(mutalisk())

###############################################################################################
# 풀이: https://velog.io/@y7y1h13/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%B0%B1%EC%A4%80-12869%EB%B2%88-%EB%AE%A4%ED%83%88%EB%A6%AC%EC%8A%A4%ED%81%ACpython

# import sys
# from itertools import permutations
#
# INPUT = sys.stdin.readline
#
#
# def mutalisk_dfs(scv1: int, scv2: int, scv3: int, cnt: int) -> None:
#     global ANS
#
#     if scv1 <= 0 and scv2 <= 0 and scv3 <= 0:
#         if ANS > cnt:
#             ANS = cnt
#             return
#
#     scv1 = 0 if scv1 <= 0 else scv1
#     scv2 = 0 if scv2 <= 0 else scv2
#     scv3 = 0 if scv3 <= 0 else scv3
#
#     if DP[scv1][scv2][scv3] <= cnt and DP[scv1][scv2][scv3] != 0:
#         return
#
#     DP[scv1][scv2][scv3] = cnt
#
#     for i in permutations((9, 3, 1), 3):
#         mutalisk_dfs(scv1 - i[0], scv2 - i[1], scv3 - i[2], cnt + 1)
#
#
# if __name__ == "__main__":
#     N = int(INPUT())
#     ANS = float("inf")
#     SCV = list(map(int, INPUT().split()))
#     while len(SCV) < 3:
#         SCV.append(0)
#     DP = [
#         [[float("inf") for _ in range(max(SCV) + 1)] for __ in range(max(SCV) + 1)]
#         for ___ in range(max(SCV) + 1)
#     ]
#     mutalisk_dfs(SCV[0], SCV[1], SCV[2], 0)
#     print(ANS)
