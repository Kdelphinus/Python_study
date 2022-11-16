import sys, heapq

INPUT = sys.stdin.readline
INF = float("inf")


def graph_init(c, b: int) -> list:
    """
    버스 노선 정보를 저장하는 함수
    Args:
        c: 도시의 개수
        b: 버스의 개수

    Returns:
        tmp: 버스 노선 정보가 정리된 리스트

    """
    tmp = [[] for _ in range(c + 1)]
    for _ in range(b):
        s, e, p = map(int, INPUT().split())
        tmp[s].append((e, p))
    return tmp


def dijkstra(c: int, s: int, g: int, gp: list) -> int:
    """
    dijkstra 알고리즘 함수
    Args:
        c: 도시의 개수
        s: 시작 도시
        g: 목표 도시
        gp: 버스 노선 정보

    Returns:
        -1: 갈 수 없음
        positive number: 최소 비용

    """
    heap, dp = [], [INF for _ in range(c + 1)]
    dp[s] = 0
    heapq.heappush(heap, (s, 0))

    while heap:
        cur, price = heapq.heappop(heap)

        if dp[cur] < price:
            continue

        for n, p in gp[cur]:
            np = price + p
            if np < dp[n]:
                dp[n] = np
                heapq.heappush(heap, (n, np))

    return dp[g] if dp[g] < INF else -1


if __name__ == "__main__":
    city = int(INPUT())
    bus = int(INPUT())
    graph = graph_init(city, bus)
    start, goal = map(int, INPUT().split())
    print(dijkstra(city, start, goal, graph))
