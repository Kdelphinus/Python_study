"""2261 가장 가까운 두 점"""
"""
* 푸는 과정
1. x값을 기준으로 정렬
2. 좌표의 중복값을 제거하여 중복점이 있으면 0 리턴
3. 중복값이 없다면 중간값을 기준으로 왼쪽 점들과 오른쪽 점들의 최소 거리의 제곱을 구함
4. 오른쪽, 왼쪽 점들의 최소 거리의 제곱 중 최소값 dist를 구함
5. (중간값의 x좌표 - 임의의 점 x좌표) ** 2 < dist인 점들만 middle 리스트에 저장(하나는 오른쪽, 하나는 왼쪽에 있는 점들의 거리를 구하기 위하여)
6. middle 리스트의 임의의 두 점 중, y좌표의 차의 제곱이 dist보다 작은 값들은 거리를 구함
7. dist와 구한 거리를 비교하여 더 작은 값을 dist로 지정
"""

import sys

input = sys.stdin.readline


def distance_square(dot1, dot2):
    """두 점 사이의 거리의 제곱을 구하는 함수"""
    return (dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2


def close_dot(location):
    """주어진 점들 중 가장 가까운 점의 거리의 제곱을 찾는 함수"""
    if len(location) == 2:  # 점이 두 개일 때
        return distance_square(location[0], location[1])
    elif len(location) == 3:  # 점이 세 개일 때
        return min(
            distance_square(location[0], location[1]),
            distance_square(location[0], location[2]),
            distance_square(location[1], location[2]),
        )
    mid = len(location) // 2  # 중간값
    dist = min(
        close_dot(location[:mid]), close_dot(location[mid:])
    )  # 왼쪽과 오른쪽 중 더 짧은 두 점의 거리

    middle = []  # x좌표가 중간점의 x와 dist보다 멀지 않은 점들을 담을 리스트

    for i in range(len(location)):  # x좌표가 중간점의 x와 dist보다 멀지 않은 점들
        if (location[mid][0] - location[i][0]) ** 2 < dist:
            middle.append(location[i])
    middle.sort(key=lambda x: x[1])  # y좌표 기준으로 오름차순
    if len(middle) > 1:  # 두 점 이상 있을 때
        for i in range(len(middle) - 1):
            for j in range(i + 1, len(middle)):
                if (middle[i][1] - middle[j][1]) ** 2 < dist:  # y좌표끼리 거리가 dist보다 짧을 때
                    dist = min(dist, distance_square(middle[i], middle[j]))
                else:
                    break

    return dist


num = int(input().rstrip())  # 주어질 좌표의 수
location = [list(map(int, input().split())) for _ in range(num)]  # 주어진 좌표들
location.sort()  # x좌표 기준 오름차순으로 정렬

location_set = list(set(map(tuple, location)))  # 이중 배열을 set으로 만들어 중복 제거
if len(location) == len(location_set):  # 중복되는 점이 없을 때
    print(close_dot(location))
else:  # 중복되는 점이 있다면
    print(0)
