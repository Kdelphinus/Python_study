"""1011 Fly me to the Alpha Centauri"""

# t = int(input())
# for i in range(t):
#     x, y = map(int, input().split())
#     dis = y - x
#     num = 1
#     cnt = 1
#     a = 1
#     while True:
#         if dis <= num:
#             print(cnt)
#             break
#         else:
#             if cnt % 2 == 0:
#                 cnt += 1
#                 a += 1
#                 num += a
#             else:
#                 cnt += 1
#                 num += a

# --------------------------------------------------------------------

"""모범 답안"""
# https://pacific-ocean.tistory.com/124
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    c = b - a
    num = 1
    while True:
        if num**2 <= c < (num + 1) ** 2:
            break
        num += 1
    if num**2 == c:  # 거리가 제곱근 일 때
        print((num * 2) - 1)
    elif num**2 < c <= num**2 + num:  # 거리가 두 제곱수 사이의 중간값보다 작을 때
        print(num * 2)
    else:  # 거리가 두 제곱수 사이의 중간값보다 클 때
        print((num * 2) + 1)

# --------------------------------------------------------------------

# 시간은 이게 더 빠름
# 그러나 c++에서 같은 방식을 사용하면 시간초과 뜸
t = int(input())

for i in range(t):
    x, y = map(int, input().split())

    dis = y - x  # 이동해야 할 거리
    dis_sum = 1  # 이동한 거리의 합
    cnt = 1  # 이동한 횟수
    move = 1  # 한 번에 이동한 거리

    # 거리가 1부터 1씩 증가할 때, 이동한 횟수의 나오는 빈도가 1, 1, 2, 2, 3, 3, 4, 4...의 규칙으로 증가
    # 1과 2는 1번, 3과 4는 2번, 5와 6은 3번...
    while dis > dis_sum:
        cnt += 1  # 이동
        dis_sum += move  # 이동한 거리만큼 더 해줌

        # 가운데 부분을 제외하곤 대칭이기에 이동한 횟수가 짝수일 때, 이동 거리를 1 늘린다
        # 가운데 부분은 정확하게 알 필요 없기에 이 방법을 사용
        if cnt % 2 == 0:
            move += 1
    print(cnt)
