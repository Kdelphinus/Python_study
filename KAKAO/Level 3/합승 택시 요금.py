"""2021 KAKAO BLIND RECRUITMENT"""
import heapq


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for start, end, pay in fares:
        graph[start].append([end, pay])
        graph[end].append([start, pay])

    def dijkstra(start_spot, n):
        heap = []
        dp = [float("inf") for _ in range(n + 1)]
        dp[start_spot] = 0
        heapq.heappush(heap, [start_spot, 0])

        while heap:
            now, pay = heapq.heappop(heap)
            if dp[now] < pay:
                continue

            for next_spot, next_pay in graph[now]:
                next_pay += pay
                if dp[next_spot] > next_pay:
                    dp[next_spot] = next_pay
                    heapq.heappush(heap, [next_spot, next_pay])

        return dp

    s_dp = dijkstra(s, n)
    answer = s_dp[a] + s_dp[b]

    for i in range(1, n + 1):
        if i != s:
            i_dp = dijkstra(i, n)
            answer = min(answer, s_dp[i] + i_dp[a] + i_dp[b])

    return answer


# -----------------------------------------------------------------------------------------

"""플로이드 와셜 알고리즘을 이용하여 간단하게 푼 코드"""
import heapq


def solution(n, s, a, b, fares):
    d = [[20000001 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        d[x][x] = 0
    for x, y, c in fares:
        d[x - 1][y - 1] = c
        d[y - 1][x - 1] = c

    for i in range(n):  # 경유지
        for j in range(n):  # 출발
            for k in range(n):  # 도착
                if d[j][k] > d[j][i] + d[i][k]:
                    d[j][k] = d[j][i] + d[i][k]

    minv = 40000002
    for i in range(n):
        minv = min(minv, d[s - 1][i] + d[i][a - 1] + d[i][b - 1])
    return minv


# ----------------------------------------------------------------------------------------------

"""나의 풀이와 같은 구동, 더 간단한 구현"""
from collections import defaultdict
import heapq


def solution(n, s, a, b, fares):
    dic = defaultdict(list)
    for st, ed, co in fares:
        dic[st].append((co, ed))
        dic[ed].append((co, st))
    ans = []
    for i in range(1, n + 1):
        Q = [(0, i)]
        visited = [True] * (n + 1)
        dp = [float("inf")] * (n + 1)
        dp[i] = 0
        while Q:
            co, des = heapq.heappop(Q)
            if visited[des]:
                visited[des] = False
                for cost, destination in dic[des]:
                    dp[destination] = min(cost + dp[des], dp[destination])
                    heapq.heappush(Q, (dp[destination], destination))
        ans.append(dp[a] + dp[b] + dp[s])

    return min(ans)
