class StationNode:
    """간단한 지하철 역 노드 클래스"""

    def __init__(self, station_name):
        self.station_name = station_name
        self.adjacent_stations = []  # 인접 리스트

    def add_connection(self, other_station):
        """지하철 역 노드 사이 엣지 저장하기"""
        self.adjacent_stations.append(other_station)
        other_station.adjacent_stations.append(self)

    def __str__(self):
        """지하철 노드 문자열 메소드. 지하철 역 이름과 연결된 역들을 모두 출력해준다"""
        res_str = f"{self.station_name}: "  # 리턴할 문자열

        # 리턴할 문자열에 인접한 역 이름들 저장
        for station in self.adjacent_stations:
            res_str += f"{station.station_name} "

        return res_str


def create_subway_graph(input_file):
    """input_file에서 데이터를 읽어 와서 지하철 그래프를 리턴하는 함수"""
    stations = {}  # 지하철 역 노드들을 담을 딕셔너리

    # 파라미터로 받은 input_file 파일을 연다
    with open(input_file, "r", encoding="utf-8") as stations_raw_file:
        for line in stations_raw_file:  # 파일을 한 줄씩 받아온다
            previous_station = None  # 엣지를 저장하기 위한 도우미 변수. 전 역을 저장
            subway_line = line.strip().split("-")  # 앞 뒤 띄어쓰기를 없애고 "-"를 기준점으로 데이터를 나눈다

            for name in subway_line:
                station_name = name.strip()  # 앞 뒤 띄어쓰기 없애기

                # 지하철 역 이름이 이미 저장한 key 인지 확인
                if station_name not in stations:
                    current_station = StationNode(station_name)  # 새로운 인스턴스를 생성하고
                    stations[
                        station_name
                    ] = current_station  # dictionary에 역 이름은 key로, 역 노드 인스턴스를 value로 저장한다
                else:
                    current_station = stations[
                        station_name
                    ]  # 이미 저장한 역이면 stations에서 역 인스턴스를 갖고 온다

                if previous_station is not None:
                    current_station.add_connection(
                        previous_station
                    )  # 현재 역과 전 역의 엣지를 연결

                previous_station = current_station  # 현재 역을 전 역으로 변경
    return stations


stations = create_subway_graph(
    "./codeit/5. 자료 구조/3. 그래프/stations.txt"
)  # stations.txt 파일로 그래프를 만든다

# stations에 저장한 역 인접 역들 출력 (채점을 위해 역 이름 순서대로 출력)
for station in sorted(stations.keys()):
    print(stations[station])
