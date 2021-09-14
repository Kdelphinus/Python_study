# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    num1 = my_list[index1]
    num2 = my_list[index2]
    my_list[index1] = num2
    my_list[index2] = num1

    return my_list


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    cnt = start
    pivot = end
    big = start
    while cnt < pivot:
        if my_list[cnt] <= my_list[pivot]:
            swap_elements(my_list, cnt, big)
            big += 1
        cnt += 1
    swap_elements(my_list, pivot, big)
    pivot = big

    return pivot

# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)



# 모범답안
# # 두 요소의 위치를 바꿔주는 helper function
# def swap_elements(my_list, index1, index2):
#     temp = my_list[index1]
#     my_list[index1] = my_list[index2]
#     my_list[index2] = temp


# # 퀵 정렬에서 사용되는 partition 함수
# def partition(my_list, start, end):
#     # 리스트 값 확인과 기준점 이하 값들의 위치 확인을 위한 변수 정의
#     i = start
#     b = start
#     p = end

#     # 범위안의 모든 값들을 볼 때까지 반복문을 돌린다
#     while i < p:
#         # i 인덱스의 값이 기준점보다 작으면 i와 b 인덱스에 있는 값들을 교환하고 b를 1 증가 시킨다
#         if my_list[i] <= my_list[p]:
#             swap_elements(my_list, i, b)
#             b += 1
#         i += 1

#     # b와 기준점인 p 인덱스에 있는 값들을 바꿔준다
#     swap_elements(my_list, b, p)
#     p = b

#     # pivot의 최종 인덱스를 리턴해 준다
#     return p


# # 테스트 1
# list1 = [4, 3, 6, 2, 7, 1, 5]
# pivot_index1 = partition(list1, 0, len(list1) - 1)
# print(list1)
# print(pivot_index1)

# # 테스트 2
# list2 = [6, 1, 2, 6, 3, 5, 4]
# pivot_index2 = partition(list2, 0, len(list2) - 1)
# print(list2)
# print(pivot_index2)