"""6549 히스토그램에서 가장 큰 직사각형"""
import sys

input = sys.stdin.readline

while True:
    N, *hist = list(map(int, input().split()))  # 히스토그램 크기, 히스토그램들의 높이가 담긴 리스트
    hist.append(0)  # 마지막 히스토그램까지 계산하기 위하여 추가
    if N == 0:  # 종결조건
        break
    stack = []  # 히스토그램의 인덱스를 담을 스택
    max_area = 0  # 최대 넓이
    for index, height in enumerate(hist):
        # 스택에 값이 있고 스택에 저장된 마지막 히스토그램의 높이가 현재 히스토그램 높이보다 높을 때
        while stack and hist[stack[-1]] > height:
            ih = hist[stack.pop()]  # 마지막 stack의 높이

            # 전 스택부터 전전 스택까지의 거리 = 가로길이
            # 가로길이를 구하기 위해 index에서부터 stack의 top까지의 거리를 이용
            # stack에 값이 없으면 시작까지 거리가 가로 길이
            w = index - stack[-1] - 1 if stack else index

            if max_area < w * ih:
                max_area = w * ih
        stack.append(index)
    print(max_area)

# ---------------------------------------------------------------------------------------------
# 시간 초과
# while True:
#     hist = list(map(int, input().split()))  # 히스토그램을 받음

#     if hist[0] == 0:  # 종결 조건
#         break

#     size = hist[0] + 1  # 히스토그램 길이
#     area_list = []  # 넓이를 담을 스택

#     for i in range(1, size):
#         for j in range(i, size):
#             if i == j:  # 같은 인덱스일 때
#                 area_list.append(hist[i])
#             else:
#                 if hist[i] <= hist[j]:  # 다음 히스토그램 넓이가 같거나 클 때
#                     area_list[-1] += hist[i]  # 직사각형을 계속해서 이어간다
#                 else:  # 다음 히스토그램 넓이가 더 작을 때
#                     break  # 다음 히스토그램으로 넘어간다

#     print(max(size_list))