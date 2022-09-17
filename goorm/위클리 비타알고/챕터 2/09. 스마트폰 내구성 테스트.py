import sys

sys.setrecursionlimit(10 ** 8)
INF = float("inf")


def min_trial(num, height):
    """min_trial num번의 기회로 0 ~ height 사이 임의의 임계치를 찾는 함수

    Args:
        num (int): 실험할 수 있는 기회
        height (int): 실험할 수 있는 최대 높이

    Returns:
        dp[num][height] (int):  num번의 기회가 있고 height가 최대 실험 높이일 때, 임계치를 확정적으로 찾을 수 있는 횟수
    """
    if num == 1:  # 기회가 한 번이면 밑에서부터 차례대로 실험해야 한다.
        return height

    if height == 0:  # 높이가 0이면 실험하지 않아도 알 수 있다.
        return 0

    if height == 1:  # 높이가 1이면 한 번만 던져보면 된다.
        return 1

    if dp[num][height] < INF:  # 이미 구한 값이면 그 값을 이용한다.
        return dp[num][height]

    for x in range(1, height + 1):  # 높이를 변화시키면서 확인
        # 아직 구하지 않은 값이면 계산한다.
        if dp[num - 1][x - 1] == INF:
            dp[num - 1][x - 1] = min_trial(num - 1, x - 1)
        if dp[num][height - x] == INF:
            dp[num][height - x] = min_trial(num, height - x)

        # 높이에서 꺠져서 범위 아래를 확인할 경우와 꺠지지 않아 범위 위를 확인할 경우 중 더 최악인 것을 고른다.
        dp[num][height] = min(
            max(dp[num - 1][x - 1], dp[num][height - x]) + 1, dp[num][height]
        )

    return dp[num][height]


num, height = map(int, input().split())
dp = [[INF] * (height) for _ in range(num + 1)]
print(min_trial(num, height // 10))
