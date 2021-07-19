# -------------------------------------------------------------------------------------

# 정답은 맞으나 효율성이 아예 없음
# from itertools import product


# def solution(n):
#    num_list = ["1", "2", "4"]
#    one_two_four = ["0", "1", "2", "4"]
#    tmp = n
#    cnt = 0

#    while tmp > 0:
#        tmp //= 3
#        cnt += 1
#    print(cnt)

#    for i in range(2, cnt + 1):
#        tmp = list(map("".join, product(num_list, repeat=i)))  # 정렬되어서 나옴
#        one_two_four += tmp

#    return one_two_four[n]


# print(solution(512))
