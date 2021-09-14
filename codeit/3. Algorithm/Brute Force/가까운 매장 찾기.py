# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)


# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    min_num = float(10 ** 10)
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if i < j:
                num = distance(coordinates[i], coordinates[j])
                min_num = min(num, min_num)
                if num == min_num:
                    a = i
                    b = j
    return [coordinates[a], coordinates[b]]


# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))