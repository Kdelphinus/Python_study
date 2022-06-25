""" 3053 택시 기하학 """

from math import pi, sqrt


# 반지름 정의
radius = int(input())

# 유클리드 기하학에서 원의 넓이
Euclidean_area = radius * radius * pi
print(Euclidean_area)

# 택시 기하학에서 원의 넓이
Taxicab_radius = sqrt(radius ** 2 + radius ** 2)
Taxicab_area = Taxicab_radius * Taxicab_radius
print(Taxicab_area)
