"""17298 오큰수"""

import sys

input = sys.stdin.readline

# version 1
# num = int(input())  # 주어진 수의 개수
# numbers = list(map(int, input().split()))  # 주어진 수가 담긴 리스트
# stack = []
# anw = [-1 for _ in range(num)]

# stack.append(0)
# i = 1

# while i < num and stack:  # 스택에 값이 있고 인덱스가 범위 안에 있을 때만 진행
#    while (
#        stack and numbers[stack[-1]] < numbers[i]
#    ):  #  스택에 값이 있고 스택의 마지막에 저장된 인덱스 값보다 비교하는 값이 더 크면
#        anw[stack[-1]] = numbers[i]  # 오큰수를 저장
#        stack.pop()  # 저장한 인덱스는 제거한다

#    stack.append(i)  # 기준 대상을 다음 인덱스로 이동
#    i += 1  # 비교할 대상을 다음 인덱스로 이동

# print(*anw)

# --------------------------------------------------------------------------------------------------------

# version 2
# c로 풀었던 방법, 이게 더 파이썬스럽다
# num = int(input())
# number = list(map(int, input().split()))
# stack = []
# anw = [0 for i in range(num)]
#
# for i in range(num - 1, -1, -1):
#     while stack and stack[-1] <= number[i]:
#         stack.pop()
#     if not stack:
#         anw[i] = -1
#     else:
#         anw[i] = stack[-1]
#
#     stack.append(number[i])
#
# print(*anw)


# --------------------------------------------------------------------------------------------------------
# 시간 초과
# num = int(sys.stdin.readline().rstrip())  # 주어진 수의 개수
# numbers = list(map(int, sys.stdin.readline().rstrip().split()))  # 주어진 수가 담긴 리스트
# i = 0  # 오큰수를 구할 인덱스

# for i in range(num):
#     j = i + 1  # 비교는 오큰수보다 오른쪽만 한다
#     while True:
#         if j == num:  # 오른쪽에 숫자가 없는 경우
#             print(-1, end=" ")
#             break

#         if numbers[i] < numbers[j]:  # 오큰수를 찾았다면
#             print(numbers[j], end=" ")
#             break
#         else:
#             j += 1

# --------------------------------------------------------------------------------------------------------

# 오등큰수를 푼 뒤 그 방법으로 바꾼 풀이
num = int(input())
number = list(map(int, input().split()))
stack = []
ans = [-1 for i in range(num)]

for i in range(num):
    while stack and number[stack[-1]] < number[i]:
        ans[stack.pop()] = number[i]
    stack.append(i)

print(*ans)
