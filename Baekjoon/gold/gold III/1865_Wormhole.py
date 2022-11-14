# 풀이 및 논란에 관한 정리: https://www.acmicpc.net/board/view/72995 (float("inf")가 틀렸던 이유)

import sys

INPUT = sys.stdin.readline
# INF = float("inf") 이를 이용하고 싶으면 모든 정점에서 출발해봐야 하지만 이는 시간 상 불가하다. 이유는 위 링크 참고
INF = int(1e9)


def data_init(n: int, m: int, w: int) -> list:
    """
    주어지는 인자를 정리하는 함수

    Args:
        n: 도시의 개수
        m: 도로의 개수
        w: 웜홀의 개수

    Returns:
        tmp: 정리된 리스트
    """
    tmp = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):  # 가상 시작점을 만들고 이동 시간을 0으로 만듬
        tmp[0].append((i, 0))
    for _ in range(m):  # 도로는 양방향
        s, e, t = map(int, INPUT().split())
        tmp[s].append((e, t))
        tmp[e].append((s, t))
    for _ in range(w):  # 웜홀은 단방향, 시간은 줄어듬
        s, e, t = map(int, INPUT().split())
        tmp[s].append((e, -t))
    return tmp


def bellman_ford(num: int, start: int, linked: list) -> bool:
    """
    bellman ford 알고리즘, 음수 가중치가 있어도 최단거리를 구할 수 있음

    Args:
        num: 도시의 개수
        start: 임의의 시작 지점
        linked: 연결된 도시들의 정보들

    Returns:
        True: 과거로 돌아갈 수 있다.
        False: 과거로 돌아갈 수 없다.

    """
    dp = [INF for _ in range(num + 1)]
    dp[start] = 0

    for i in range(num - 1):
        for wp in range(1, num + 1):
            for e, t in linked[wp]:
                if dp[e] > dp[wp] + t:
                    dp[e] = dp[wp] + t

    for wp in range(1, num + 1):
        for e, t in linked[wp]:
            if dp[e] > dp[wp] + t:
                return True

    return False


def time_warp(n: int, m: int, w: int) -> str:
    """
    시간여행이 가능한지 확인하는 함수

    Args:
        n: 도시의 개수
        m: 도로의 개수
        w: 웜홀의 개수

    Returns:
        시간여행 가능 여부

    """
    linked = data_init(n, m, w)
    # 음의 싸이클이 나오는지 모든 경로에서 판단해야 하기 떄문에 임의의 시작점으로 시작한다.
    if bellman_ford(n, 0, linked):
        return "YES"
    return "NO"


if __name__ == "__main__":
    for _ in range(int(INPUT())):
        node, road, worm = map(int, INPUT().split())
        print(time_warp(node, road, worm))
