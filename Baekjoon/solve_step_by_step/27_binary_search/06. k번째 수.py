"""1300 k번째 수"""
"""이 문제에서 행과 열은 모두 1부터 시작함을 유의"""
import sys

input = sys.stdin.readline


def num_k(start, end, n, k):  # 탐색을 시작할 숫자, 탐색을 끝낼 숫자, A의 크기, k번째 수
    if start > end:  # 숫자를 찾으면 그 숫자를 리턴
        return start

    mid = (start + end) // 2  # 중간값
    cnt = 0  # 앞에 몇 개의 숫자가 있는지 저장할 변수

    for i in range(1, n + 1):  # 배열 A의 행을 하나씩 확인
        # 배열 A는 1행부터 구구단 형식으로 저장되어 있는 배열
        # 그렇기에 중간값을 행으로 나누면 그 행에서 자기보다 작은 수가 몇개인지 알 수 있다
        if mid // i >= n:  # 몫이 행 크기보다 크면 그 행은 모두 중간값보다 작다
            cnt += n
        else:  # 몫이 행 크기보다 작으면 몫만큼만 작은 숫자를 더한다
            cnt += mid // i

    if cnt < k:  # 중간값보다 작은 숫자가 인덱스보다 적다면
        return num_k(mid + 1, end, n, k)  # 중간값보다 큰 범위만 확인하고
    else:  # 중간값보다 작은 숫자가 인덱스보다 많다면
        return num_k(start, mid - 1, n, k)  # 중간값보다 작은 범위만 확인한다


n = int(input())  # n x n 배열 A
k = int(input())  # 구하고 싶은 배열 B의 인덱스 k
print(num_k(1, k, n, k))

""" 4 x 4 크기라면
배열 A
[
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [3, 6, 9, 12],
    [4, 8, 12, 16],
]

배열 B
[1, 2, 2, 3, 3, 4, 4, 4, 6, 6, 8, 8, 9, 12, 12, 16]
"""
