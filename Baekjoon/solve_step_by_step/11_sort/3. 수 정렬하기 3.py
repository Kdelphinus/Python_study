"""10989 수 정렬하기3"""

"""계수 정렬(countuing sort)을 권장하였기에 계수 정렬을 이용
- 중복된 값이 많이 분포할 때 효율적인 정렬 방법
- 양의 정수에 대해서만 적용 가능
"""


# def counting_sorted(my_list, num):
#     """입력받는 값은 정렬 안 된 리스트와 리스트 안에 들어간 수의 최대인 num"""

#     count = [0] * num  # 리스트 안에 들어갈 수 있는 최대 정수까지 넣을 수 있는 리스트 생성
#     count_sort = [0] * len(my_list)  # 정렬된 수들이 들어갈 리스트

#     for i in my_list:  # 주어진 리스트 안, 수의 개수를 리스트 배열 인덱스에 맞춰 저장
#         count[i] += 1

#     for i in range(1, num):  # 배열 인덱스의 수가 자신보다 앞에 있는 수의 개수를 가짐
#         count[i] += count[i - 1]

#     # 주어진 리스트의 가장 뒤에 있는 숫자를 가져옴
#     # 그 숫자 앞에 몇 개의 숫자가 있는지 count 배열의 인덱스를 통해 확인
#     # count_sort 리스트에 앞에 들어갈 숫자만큼 배열을 비워두고 삽입
#     for i in range(len(my_list) - 1, -1, -1):
#         count_sort[count[my_list[i]] - 1] = my_list[i]
#         count[my_list[i]] -= 1  # 그 숫자의 개수가 하나 줄었기 때문에 1을 줄여준다

#     return count_sort


# num = int(input())  # 주어질 숫자의 개수
# num_list = []  # 받은 숫자를 저장할 리스트

# # 주어진 수 받아서 리스트에 저장
# for _ in range(num):
#     temp = int(input())
#     num_list.append(temp)

# # 계수 정렬 함수에 대입
# count_sort = counting_sorted(num_list, 10001)  # 문제에서 최댓값이 10000

# # 정렬된 함수 출력
# for i in range(len(count_sort)):
#     print(count_sort[i])


# ---------------------------------------------------------------------------------------------
"""위가 계수 정렬을 알기 쉽게 풀어쓴 것이나 메모리 제한에 걸려 문제 답이 될 수 없음"""
"""빠르게 진행되는 약식 계수 정렬 코드"""

import sys

n = int(sys.stdin.readline())
li = [0] * 10001  # 문제에서 최댓값이 10000
for i in range(n):  # 숫자의 개수를 각 인덱스에 저장한다
    temp = int(sys.stdin.readline())
    li[temp] += 1

# check = [] # 정렬된 숫자를 저장할 리스트

for j in range(1, 10001):
    if li[j] >= 1:  # 숫자가 있다면 개수만큼 출력한다
        for k in range(li[j]):
            print(j)
            # check.append(j)
