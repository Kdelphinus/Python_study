"""15649 N과 M (1)"""

"""내장 함수 이용"""
from itertools import permutations

# 1부터 n까지의 자연수 중에서 중복 없이 m개를 고른 수열
n, m = map(int, input().split())

# # 1부터 n까지의 자연수를 가진 리스트
# num = list(str(i) for i in range(1, n + 1))
# nums = list(permutations(num, m))

# for i in nums:
#     for j in range(len(nums[0])):
#         print(i[j], end=" ")
#     print()

# 위의 코드와 같은 코드
P = permutations(range(1, n + 1), m)  # tuple

for i in P:
    print(" ".join(map(str, i)))  # tuple -> str


# ------------------------------------------------------------------------------

"""직접 구현"""
import sys

input = sys.stdin.readline


def DFS(l, num, count):
    """permutations를 구현한 함수"""
    if l == count:  # 수열을 원하는 길이만큼 만들었을 때
        print(*result)
        return

    for i in range(num):  # 1 ~ num까지의 숫자를 살펴본다
        if not check[i]:  # 아직 숫자를 쓰지 않았다면
            check[i] = True  # 숫자를 썼다고 표시하고
            result.append(i + 1)  # 숫자를 수열에 추가한 뒤
            DFS(l + 1, num, count)  # 다음 인덱스로 이동
            result.pop()  # 결과를 출력한 뒤, 넣었던 값을 빼주고
            check[i] = False  # 쓰지 않은 숫자로 표시


num, count = map(int, input().split())
result = []  # 결과를 저장하는 리스트
check = [False] * num  # 숫자 사용여부를 표시할 리스트

DFS(0, num, count)