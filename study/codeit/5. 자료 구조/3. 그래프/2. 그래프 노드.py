class StationNode:
    """간단한 지하철 역 노드 클래스"""

    def __init__(self, station_name):
        self.station_name = station_name


def create_station_nodes(input_file):
    """input_file에서 데이터를 읽어 와서 지하철 그래프 노드들을 리턴하는 함수"""
    stations = {}  # 지하철 역 노드들을 담을 딕셔너리

    # 파라미터로 받은 input_file 파일을 연다
    with open(input_file, "r", encoding="utf8") as stations_raw_file:
        for line in stations_raw_file:  # 파일을 한 줄씩 받아온다
            subway_line = line.strip().split("-")  # 앞 뒤 띄어쓰기를 없애고 "-"를 기준점으로 데이터를 나눈다

            for name in subway_line:
                station_name = name.strip()  # 앞 뒤 띄어쓰기 없애기

                # 지하철 역 이름이 이미 저장한 key 인지 확인
                if station_name not in stations:
                    current_station = StationNode(station_name)  # 새로운 인스턴스를 생성하고
                    # dictionary에 역 이름은 key로, 역 노드 인스턴스를 value로 저장한다
                    stations[station_name] = current_station

    return stations


stations = create_station_nodes(
    "./codeit/5. 자료 구조/3. 그래프/stations.txt"
)  # stations.txt 파일로 그래프 노드들을 만든다

# stations에 저장한 역들 이름 출력 (채점을 위해 역 이름 순서대로 출력)
for station in sorted(stations.keys()):
    print(stations[station].station_name)