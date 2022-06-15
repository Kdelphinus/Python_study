"""10816 숫자 카드 2"""
import sys

input = sys.stdin.readline


def binary_search(element, some_list, start, end):
    """이진 탐색 함수"""
    if start > end:  # 다 탐색하면 종료
        return 0

    mid = (start + end) // 2  # 중간 인덱스
    if some_list[mid] == element:  # 값을 찾았다면
        return some_list[start : end + 1].count(
            element
        )  # 지금 구한 리스트에서 같은 값을 가지는 인덱스의 개수를 구함
    elif some_list[mid] > element:  # 중간값보다 찾는 값이 작으면 앞부분만 확인
        return binary_search(element, some_list, start, mid - 1)
    elif some_list[mid] < element:  # 중간값보다 찾는 값이 크다면 뒷부분만 확인
        return binary_search(element, some_list, mid + 1, end)


n_len = int(input())
n_list = sorted(map(int, input().split()))

m_len = int(input())
m_list = list(map(int, input().split()))
m_dict = {}  # 값: 개수를 저장할 사전

for m in m_list:
    if m not in m_dict:
        m_dict[m] = binary_search(m, n_list, 0, n_len - 1)

print(" ".join(str(m_dict[x]) if x in m_dict else "0" for x in m_list))


# ------------------------------------------------------------------------------------------------------------------------
"""내장 함수 이용"""
"""훨씬 빠름"""
import sys
from collections import Counter

n_len = int(input())
n_list = sys.stdin.readline().split()

m_len = int(input())
m_list = sys.stdin.readline().split()

C = Counter(n_list)  # '값: 들어있는 개수'로 사전 정의(자세한 건 '여러 기능들/collections.py' 참고)

for m in m_list:
    if m in C:
        print(C[m], end=" ")
    else:
        print(0, end=" ")

# comprehension을 쓸 때는 문자열을 써야함
# print(" ".join(f"{C[m]}" if m in C else "0" for m in m_list))
