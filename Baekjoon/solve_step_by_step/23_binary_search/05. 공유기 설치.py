"""2110 공유기 설치"""
import sys

input = sys.stdin.readline
dist = 0


def router_installation(min_dist, max_dist, router_num, house_rocations):
    """인접한 두 공유기 사이의 거리를 최대로 하여 설치하는 함수"""
    global dist

    if min_dist > max_dist:
        return

    mid = (min_dist + max_dist) // 2  # 처음 집과 설정한 가장 가까운 거리와 설정한 가장 먼 거리의 중간값을 구한다
    router_install = 1  # 첫 집에 공유기 설치
    before_install = house_rocations[0]  # 처음 설치한 집의 위치
    for i in range(1, len(house_rocations)):
        if house_rocations[i] >= before_install + mid:  # 이전 설치한 곳과의 거리가 중간값보다 멀다면
            router_install += 1  # 공유기 설치
            before_install = house_rocations[i]  # 이전 설치한 곳 업데이트

    if router_install < router_num:  # 공유기를 다 설치하지 못했으면
        return router_installation(
            min_dist, mid - 1, router_num, house_rocations
        )  # 가장 먼 거리를 중간값보다 작게하여 다시 설치
    else:  # 공유기를 충분히 설치했다면
        dist = mid  # 우선 값을 저장하고
        return router_installation(
            mid + 1, max_dist, router_num, house_rocations
        )  # 더 먼 거리를 확인하여 더 효율적 설치 방법이 있는지 확인


house_num, router_num = map(int, input().split())  # 집의 개수, 공유기의 개수
house_rocations = sorted([int(input()) for _ in range(house_num)])  # 집의 좌표들
router_installation(
    1, house_rocations[-1] - house_rocations[0], router_num, house_rocations
)
print(dist)
