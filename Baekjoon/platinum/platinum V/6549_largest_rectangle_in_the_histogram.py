# 단계별로 풀기 중 분할 정복에 있음
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
        # 스택에 값이 없거나 현재 높이가 직전 높이보다 같거나 클 때까지 반복
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
