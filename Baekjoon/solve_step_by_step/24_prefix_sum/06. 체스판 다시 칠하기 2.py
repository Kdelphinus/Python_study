# https://jih3508.tistory.com/59
# 2차원 누적합을 이용해 답을 구하는 문제
#
# 다시 칠해야 하는 부분을 누적합으로 기록한다.
# 그 후, 구간합을 비교해가며 가장 적게 칠할 수 있는 횟수를 갱신한다.
# 이때, 전체 칠해야 하는 수 - 검정을 시작으로 만들 때 칠할 수 = 흰색을 시작으로 만들 떄 칠할 수

import sys

INPUT = sys.stdin.readline


def repainting(n: int, m: int, k: int, board: list) -> int:
    """
    누적합을 이용해 체스판을 다시 칠하는 함수
    Args:
        n: 세로 길이
        m: 가로 길이
        k: 필요한 체스판의 크기
        board: 현재 체스판

    Returns:
        cnt: 다시 칠해야 하는 최소 횟수
    """
    cnt = k**2
    p_sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # 칠해야 하는 개수를 2차원 누적합으로 저장
    for i in range(n):
        for j in range(m):
            value = board[i][j] == "W" if (i + j) % 2 == 0 else board[i][j] == "B"
            p_sum[i + 1][j + 1] = (
                p_sum[i][j + 1] + p_sum[i + 1][j] - p_sum[i][j] + value
            )

    # 2차원 구간합으로 최소 색칠 횟수 계산
    for i in range(1, n - k + 2):
        for j in range(1, m - k + 2):
            cnt_b = (
                p_sum[i + k - 1][j + k - 1]
                - p_sum[i + k - 1][j - 1]
                - p_sum[i - 1][j + k - 1]
                + p_sum[i - 1][j - 1]
            )

            cnt = min(cnt, cnt_b, k**2 - cnt_b)

    return cnt


if __name__ == "__main__":
    N, M, K = map(int, INPUT().split())
    BOARD = []
    for _ in range(N):
        BOARD.append(list(INPUT().strip()))
    print(repainting(N, M, K, BOARD))
