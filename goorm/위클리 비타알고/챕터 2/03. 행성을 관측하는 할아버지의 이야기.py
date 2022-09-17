"""DFS을 이용한 풀이, O(n^2)"""
num, length = map(int, input().split())
# graph[index][0]: index보다 큰 행성, graph[index][1]: index보다 작은 행성
graph = [[[] for _ in range(2)] for _ in range(num + 1)]
visited = [0] * (num + 1)  # 탐색했는지 저장하는 리스트
cnt = 0

for _ in range(length):
    a, b = map(int, input().split())
    graph[a][1].append(b)  # b는 a보다 작다
    graph[b][0].append(a)  # a는 b보다 크다


def DFS(start, option_num):
    """DFS

    Args:
        start (int): 탐색의 기준이 되는 노드
        option_num (int): 0이면 start보다 큰 행성 탐색, 1이면 start보다 작은 행성 탐색
    """
    global cnt

    visited[start] = 1  # 탐색했다고 표시
    for i in graph[start][option_num]:  # graph[start][option_num]에 포함하는 행성 중
        if visited[i] == 0:  # 아직 탐색하지 않은 행성일 때
            visited[i] = 1  # 탐색헀다고 표시
            cnt += 1  # 개수 추가
            DFS(i, option_num)  # 탐색


for planet in range(1, num + 1):
    DFS(planet, 0)  # planet보다 큰 행성 탐색
    print(cnt, end=" ")  # 출력
    cnt = 0  # cnt 초기화
    visited = [0] * (num + 1)  # visited 초기화

    DFS(planet, 1)  # planet보다 작은 행성 탐색
    print(cnt)  # 출력
    cnt = 0  # cnt 초기화
    visited = [0] * (num + 1)  # visited 초기화

# ------------------------------------------------------------------------------------------------

"""Floyd를 이용한 풀이, O(n^3)"""


def floyd(num, length):
    """floyd

    Args:
        num (int): 행성의 개수
        length (int): 주어지는 행성 대소 관계의 수
    """
    # check[i][j] : 0이면 모름, 1이면 i > j, -1이면 i < j
    check = [[0] * (num + 1) for _ in range(num + 1)]

    for _ in range(length):
        a, b = map(int, input().split())
        check[a][b] = -1  # a는 b보다 크다
        check[b][a] = 1  # b는 a보다 작다

    for way_p in range(num + 1):
        for start in range(num + 1):
            for end in range(num + 1):
                # 대소 관계를 알면서 두 대소 관계가 같을 때
                if check[start][way_p] == check[way_p][end] != 0:
                    check[start][end] = check[start][way_p]

    for i in range(1, num + 1):
        # i보다 큰 행성의 수, i보다 작은 행성의 수
        print(check[i].count(1), check[i].count(-1))


num, length = map(int, input().split())
floyd(num, length)

