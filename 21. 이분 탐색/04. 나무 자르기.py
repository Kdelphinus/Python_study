"""2805 나무 자르기"""
import sys

input = sys.stdin.readline
max_height = 0  # 최소한의 나무를 가져갈 수 있는 절단기의 최대 높이


def felling(start, end, limit, trees):
    """최소한의 나무를 가져갈 수 있는 높이의 최댓값"""
    global max_height

    if start > end:
        return

    total = 0  # 가져갈 수 있는 나무의 길이
    height = (start + end) // 2
    for tree in trees:
        if tree > height:  # 나무가 절단기의 높이보다 높아야 나무를 자를 수 있다
            total += tree - height

    if total >= limit:  # 가져갈 수 있는 나무의 길이가 최소한의 길이보다 길다면
        if height > max_height:  # 기존의 절단기의 최대 높이보다 높다면
            max_height = height
        return felling(height + 1, end, limit, trees)  # 절단기의 높이를 더 높게 설정
    else:  # 가져갈 수 있는 나무의 길이가 최소한의 길이보다 짧다면
        return felling(start, height - 1, limit, trees)  # 절단기의 높이를 더 낮게 설정


num, m = map(int, input().split())  # 나무의 수, 가져가려는 나무의 길이
trees = list(map(int, input().split()))  # 나무의 높이
felling(0, max(trees), m, trees)
print(max_height)