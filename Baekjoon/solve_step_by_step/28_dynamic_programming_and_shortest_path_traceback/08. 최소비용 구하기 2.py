"""11779 최소비용 구하기 2"""
import sys
import heapq

input = sys.stdin.readline


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    dp[start] = 0  # 출발 도시까지 가는 비용은 0
    visited[start] = [0, 0]  # [이전 도시, 방문한 도시의 개수]

    while heap:
        price, now = heapq.heappop(heap)

        if price > dp[now]:
            continue

        for next, next_price in routes[now]:
            next_price += price
            if next_price < dp[next]:
                dp[next] = next_price
                heapq.heappush(heap, (next_price, next))
                visited[next] = [now, visited[now][1] + 1]  # [이전 위치, 방문한 도시의 개수]를 저장


city = int(input())  # 도시의 개수
buses = int(input())  # 버스의 개수
routes = [[] for _ in range(city + 1)]  # 버스 루트를 저장할 리스트
dp = [float("inf") for _ in range(city + 1)]  # 최소 가격을 저장할 리스트
visited = [0 for _ in range(city + 1)]  # [이전 위치, 방문한 도시의 개수]를 저장할 리스트
for _ in range(buses):
    start, end, price = map(int, input().split())
    routes[start].append([end, price])

start, goal = map(int, input().split())
dijkstra(start)

print(dp[goal])  # start에서 goal까지 가는 최소 가격

# goal부터 start까지 거슬러 올라가며 루트 확인
min_route = [goal]
tmp = visited[goal][0]
for _ in range(visited[goal][1]):
    min_route.append(tmp)
    tmp = visited[tmp][0]
print(len(min_route))  # 방문한 도시 개수
print(*min_route[::-1])  # 이동한 루트
