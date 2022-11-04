"""1920 수 찾기"""
import sys

input = sys.stdin.readline


def binary_search(element, some_list, start=0, end=None):
    """이진 탐색 함수"""
    if end == None:  # 처음 리스트가 입력됐을 때, end 지정
        end = len(some_list) - 1

    if start > end:  # 찾는 값이 없으면 0을 리턴
        return 0

    mid = (start + end) // 2  # 중간 인덱스
    if some_list[mid] == element:  # 찾는 값이 있으면 1을 리턴
        return 1

    if element > some_list[mid]:
        return binary_search(element, some_list, mid + 1, end)
    else:
        return binary_search(element, some_list, 0, mid - 1)


n_len = int(input().rstrip())  # n_list의 길이
n_list = list(map(int, input().split()))  # 기준 리스트
n_list.sort()  # 이분 탐색을 위해 정렬

m_len = int(input().rstrip())  # m_list의 길이
m_list = list(map(int, input().split()))  # 확인할 숫자가 담긴 리스트

for m in m_list:  # m_list의 값들을 하나씩 찾아서 출력
    print(binary_search(m, n_list))

# ----------------------------------------------------------------------------------
"""파이썬 함수를 활용 / 시간초과 유의"""
import sys

input = sys.stdin.readline

n_len = int(input().rstrip())  # n_list의 길이
n_list = list(map(int, input().split()))  # 기준 리스트

m_len = int(input().rstrip())  # m_list의 길이
m_list = list(map(int, input().split()))  # 확인할 숫자가 담긴 리스트

for m in m_list:
    if m in n_list:
        print(1)
    else:
        print(0)