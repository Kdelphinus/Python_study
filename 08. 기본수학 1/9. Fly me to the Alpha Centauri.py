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
t = int(input())

for i in range(t):
    x, y = map(int, input().split())

    dis = y - x  # 이동해야 할 거리
    dis_sum = 1  # 이동한 거리의 합
    cnt = 1  # 이동한 횟수
    move = 1  # 한 번에 이동한 거리

    # 거리가 1부터 1씩 증가할 때, 이동한 횟수의 숫자 빈도수가 1, 1, 2, 2, 3, 3...으로 나타남
    # 즉, cnt가 1과 2일 땐 1번, cnt가 3, 4일 땐 2번, cnt 5, 6일 땐 3번씩 나옴
    while dis > dis_sum:
        cnt += 1  # 이동
        dis_sum += move  # 이동한 거리만큼 더 해줌

        # 가운데 부분을 제외하곤 대칭이기에 이동한 횟수가 짝수일 때, 이동 거리를 1 늘린다
        # 가운데 부분은 정확하게 알 필요 없기에 이 방법을 사용
        if cnt % 2 == 0:
            move += 1
    print(cnt)

# --------------------------------------------------------------------