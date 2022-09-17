class StationNode:
    """지하철 역을 나타내는 역"""

    def __init__(self, station_name):
        self.station_name = station_name
        self.adjacent_stations = []
        self.visited = 0  # 한 번도 본적 없을 때: 0, 스택에 있을 때: 1, 발견된 상태: 2

    def add_connection(self, station):
        """파라미터로 받은 역과 엣지를 만들어주는 메소드"""
        self.adjacent_stations.append(station)
        station.adjacent_stations.append(self)


def create_station_graph(input_file):
    stations = {}

    # 일반 텍스트 파일을 여는 코드
    with open(input_file, "r", encoding="utf-8") as stations_raw_file:
        for line in stations_raw_file:  # 파일을 한 줄씩 받아온다
            previous_station = None  # 엣지를 저장하기 위한 변수
            raw_data = line.strip().split("-")

            for name in raw_data:
                station_name = name.strip()

                if station_name not in stations:
                    current_station = StationNode(station_name)
                    stations[station_name] = current_station

                else:
                    current_station = stations[station_name]

                if previous_station is not None:
                    current_station.add_connection(previous_station)

                previous_station = current_station

    return stations