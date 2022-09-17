"""다른 풀이를 나의 방식대로 약간 변형"""
# 링크: https://wwlee94.github.io/category/algorithm/bfs-dfs/travel-route/


from collections import defaultdict


def solution(tickets):
    airports = defaultdict(list)

    # key공항에서 이동가능한 공항을 value로 저장
    for depart, arrival in tickets:
        airports[depart].append(arrival)

    # 여러 경로가 있을 때, 문자열 오름차순으로 지정하기 위한 정렬
    for key in airports:
        airports[key].sort()

    stack = ["ICN"]  # 시작은 ICN에서
    route = []

    # 더이상 이동 불가한 공항부터 저장, 즉 경로를 역순으로 저장
    while stack:
        top = stack[-1]
        if top not in airports or not airports[top]:  # 현재 위치에서 더이상 갈 공항이 없을 때
            route.append(stack.pop())  # 스택에서 빼고 경로에 추가
        else:  # 현재 위치에서 아직 갈 수 있는 공항이 있을 때
            stack.append(airports[top].pop(0))  # 갈 수 있는 공항을 airports에서 빼서 스택에 삽입

    return route[::-1]  # 역순으로 저장된 경로를 뒤집음


print(solution([["ICN", "A"], ["ICN", "B"], ["B", "INC"], ["A", "B"]]))
# ----------------------------------------------------------------------------------------------------

"""재귀를 이용한 DFS"""
from collections import defaultdict


def dfs(graph, N, key, footprint):
    print(footprint)

    if len(footprint) == N + 1:  # 모든 티켓을 사용하면 경로 리턴
        return footprint

    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)

        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)  # 현재 경로로 이동했을 때

        graph[key].insert(idx, country)  # 잘못된 경로로 갈 경우를 대비하여 사용한 티켓 복원

        if ret:  # 모든 티켓을 사용했을 때
            return ret


def solution(tickets):
    answer = []

    graph = defaultdict(list)

    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()

    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer


print(solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]))
