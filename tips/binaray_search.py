from bisect import bisect_left, bisect_right

a = [1, 2, 3, 3, 5, 10]  # 정렬되어 있어야 한다
x = 3
print(f"bisect_left: {bisect_left(a, x)}")  # 2, 첫 3의 앞 인덱스
print(f"bisect_right: {bisect_right(a, x)}")  # 4, 마지막 3의 뒤 인덱스


"""이분탐색을 이용해 특정 범위 내, 특정 값의 개수 구하기"""


def find_num_cnt(arr, left, right):
    left_idx = bisect_left(arr, left)
    right_idx = bisect_right(arr, right)
    return right_idx - left_idx


arr = [5, 6, 7, 7, 7, 7, 8, 8, 9, 10]
print(find_num_cnt(arr, 9, 9))  # 1, arr에 들어있는 9의 개수
print(find_num_cnt(arr, 4, 7))  # 6, arr에 들어있는 4 ~ 7 사이에 수의 개수
