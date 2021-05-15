"""15649 N과 M (1)"""
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
