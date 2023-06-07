"""2477 참외밭 / 실버 III"""


# def d_init(pd: int, pl: int):
#     if pd == 1:
#         return [4, 2, 3, 1, 4], pl, 0
#     if pd == 2:
#         return [3, 1, 4, 2, 3], pl, 0
#     if pd == 3:
#         return [1, 4, 2, 3, 1], 0, pl
#     return [2, 3, 1, 4, 2], 0, pl
#
#
# k = int(input())
# field = [tuple(map(int, input().split())) for _ in range(6)]
# idx, flag = 0, 0
# pd, pl = field[0]
# minus = 0
# direction, width, height = d_init(pd, pl)
# for d, l in field[1:]:
#     if not flag and direction[idx] != d:
#         flag = 1
#         minus = l * pl
#         idx -= 1
#         continue
#     if d > 2:
#         height = max(l, height)
#     else:
#         width = max(l, width)
#     pd, pl = d, l
#     idx += 1
# minus = field[0][1] * pl if not flag else minus
# print(height, width, minus)
# print((height * width - minus) * k)

######################################################################################

"""다른 풀이"""
# 링크: https://itcrowd2016.tistory.com/84

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(6)]
w, w_idx = 0, 0
h, h_idx = 0, 0
for i in range(len(arr)):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if w < arr[i][1]:
            w, w_idx = arr[i][1], i
    else:
        if h < arr[i][1]:
            h, h_idx = arr[i][1], i

# 직사각형의 앞, 뒤 변의 길이 차이가 빼줄 직사각형의 변의 길이
subh = abs(arr[(w_idx - 1) % 6][1] - arr[(w_idx + 1) % 6][1])
subw = abs(arr[(h_idx - 1) % 6][1] - arr[(h_idx + 1) % 6][1])
print((w * h - subw * subh) * n)
