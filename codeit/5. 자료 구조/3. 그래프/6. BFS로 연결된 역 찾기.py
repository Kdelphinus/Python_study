from collections import deque
from subway_graph_bfs import create_station_graph


def bfs(graph, start_node):
    """시작 노드에서 bfs를 실행하는 함수"""
    queue = deque()  # 빈 큐 생성

    # 일단 모든 노드를 방문하지 않은 노드로 표시
    for station_node in graph.values():
        station_node.visited = False

    start_node.visited = True  # 시작 노드 방문 표시
    queue.append(start_node)  # 시작 노드 큐에 추가

    # 인접 노드들을 돌면서 방문표시
    while queue:
        check_list = queue.popleft().adjacent_stations
        for station in check_list:
            if station.visited is False:
                station.visited = True
                queue.append(station)


stations = create_station_graph(
    "./codeit/5. 자료 구조/3. 그래프/new_stations.txt"
)  # stations.txt 파일로 그래프를 만든다

gangnam_station = stations["강남"]

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
bfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들이 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들이 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)