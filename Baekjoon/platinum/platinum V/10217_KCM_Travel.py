"""10217 KCM Travel"""

# 링크: https://codekodo.tistory.com/57
# PyPy3으로만 통과 가능

import sys
import heapq

input = sys.stdin.readline
INF = float("inf")


def go_to_LA(airports_num, total_money, tickets_num):
    """go_to_LA 1번에서 airports_num번까지 가는 경로 중 최단시간을 구해주는 함수

    Args:
        airports_num (int): 주어진 공항의 총 개수
        total_money (int): 주어진 금액
        tickets_num (int): 주어진 티켓의 수

    Returns:
        (int or string): 목적지에 도착하는 방법이 있다면 가장 짧은 시간을, 없다면 "Poor KCM"을 리턴한다
    """
    # 티켓 정보 저장
    tickets = [[] for _ in range(airports_num + 1)]
    for _ in range(tickets_num):
        start, end, price, time = map(int, input().split())
        tickets[start].append([end, price, time])

    # dp[now][cost] = now까지 가는데 cost를 사용했을 때 도착하는 최단시간
    dp = [[INF for _ in range(total_money + 1)] for _ in range(airports_num + 1)]
    dp[1][0] = 0
    heap = []
    heapq.heappush(heap, [1, 0, 0])  # [출발지점, 비용, 시간]

    for cost in range(total_money):
        for now in range(1, airports_num + 1):
            time = dp[now][cost]
            if time == INF:  # 현재 비용으로 못가면 continue
                continue

            for next_spot, next_cost, next_time in tickets[now]:
                next_cost += cost
                next_time += time
                if next_cost <= total_money:  # 주어진 비용으로 갈 수 있는 곳이라면
                    # 현재 값과 지금 구한 루트로 가는 값 중 더 빠른 것을 저장한다
                    dp[next_spot][next_cost] = min(dp[next_spot][next_cost], next_time)

    return min(dp[airports_num]) if min(dp[airports_num]) < INF else "Poor KCM"


test = int(input())

for _ in range(test):
    airports_num, total_money, tickets_num = map(int, input().split())
    print(go_to_LA(airports_num, total_money, tickets_num))

# -----------------------------------------------------------------------------

"""메모리 초과"""


# def go_to_LA(airports_num, total_money, tickets_num):
#    tickets = [[] for _ in range(airports_num + 1)]
#    answer = INF  # 목적지까지 가는 최단시간

#    # 티켓 정보 저장
#    for _ in range(tickets_num):
#        start, end, price, time = map(int, input().split())
#        tickets[start].append([end, price, time])

#    heap = []
#    heapq.heappush(heap, [1, 0, 0])  # 초기값, [시작지점, 현재가격, 현재시간]
#    while heap:
#        now, curr_price, curr_time = heapq.heappop(heap)

#        for next_spot, next_price, next_time in tickets[now]:
#            next_price += curr_price
#            next_time += curr_time
#            if next_price <= total_money:
#                if next_spot == airports_num:
#                    answer = min(answer, next_time)
#                    break
#                heapq.heappush(heap, [next_spot, next_price, next_time])

#    return answer if answer < INF else "Poor KCM"

# test = int(input())

# for _ in range(test):
#    airports_num, total_money, tickets_num = map(int, input().split())
#    print(go_to_LA(airports_num, total_money, tickets_num))
