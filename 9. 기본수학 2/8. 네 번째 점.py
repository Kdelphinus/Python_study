""" 3009 네 번째 점 """

# 세 점이 주어진다
a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

# x 좌표와 y 좌표를 리스트로 모음
width = sorted([a, c, e])
height = sorted([b, d, f])

# 출력할 두 좌표
g = 0
h = 0

# x 좌표 구하기
if width[0] == width[1]:
    g = width[2]
else:
    g = width[0]

# y 좌표 구하기
if height[0] == height[1]:
    h = height[2]
else:
    h = height[0]

# 출력
print(g, h)
