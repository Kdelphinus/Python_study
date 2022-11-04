"""10816 숫자 카드 2"""

"""이분탐색을 이용한 방법: 4484ms"""
# import sys
#
# input = sys.stdin.readline
#
#
# def binary_search(element, some_list, start, end):
#     """이진 탐색 함수"""
#     if start > end:  # 다 탐색하면 종료
#         return 0
#
#     mid = (start + end) // 2  # 중간 인덱스
#     if some_list[mid] == element:  # 값을 찾았다면
#         return some_list[start : end + 1].count(
#             element
#         )  # 지금 구한 리스트에서 같은 값을 가지는 인덱스의 개수를 구함
#     elif some_list[mid] > element:  # 중간값보다 찾는 값이 작으면 앞부분만 확인
#         return binary_search(element, some_list, start, mid - 1)
#     elif some_list[mid] < element:  # 중간값보다 찾는 값이 크다면 뒷부분만 확인
#         return binary_search(element, some_list, mid + 1, end)
#
#
# n_len = int(input())
# n_list = sorted(map(int, input().split()))
#
# m_len = int(input())
# m_list = list(map(int, input().split()))
# m_dict = {}  # 값: 개수를 저장할 사전
#
# for m in m_list:
#     if m not in m_dict:
#         m_dict[m] = binary_search(m, n_list, 0, n_len - 1)
#
# print(" ".join(str(m_dict[x]) if x in m_dict else "0" for x in m_list))

#########################################################################################

"""Counter 라이브러리를 이용한 방법: 780ms"""
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
cnt = Counter(cards)
# for문보다 comprehension이 더 빠르다.(844ms VS 780ms)
# for c in check:
#     if c in cnt:
#         print(cnt[c], end=" ")
#     else:
#         print(0, end=" ")
print(" ".join(str(cnt[c]) if c in cnt else "0" for c in check))
