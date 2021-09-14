# def binary_search(element, some_list, start_index=0, end_index=None):
#     # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
#     if end_index == None:
#         end_index = len(some_list) - 1

#     # 코드를 작성하세요.
#     mid = int((start_index + end_index) / 2)
#     if some_list[mid] < element and mid != end_index:
#         if mid == end_index - 1:
#             return binary_search(element, some_list, start_index = end_index, end_index = end_index)
#         return binary_search(element, some_list, start_index = mid, end_index = end_index)
#     elif some_list[mid] > element and mid != start_index:
#         return binary_search(element, some_list, start_index = 0, end_index = mid)
#     elif (mid == 0 or mid == end_index) and some_list[mid] != element:
#         return None
#     return mid

# print(binary_search(2, [2, 3, 5, 7, 11]))
# print(binary_search(0, [2, 3, 5, 7, 11]))
# print(binary_search(5, [2, 3, 5, 7, 11]))
# print(binary_search(3, [2, 3, 5, 7, 11]))
# print(binary_search(11, [2, 3, 5, 7, 11]))

# 모범답안
def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    if start_index > end_index:
        return None

    mid = (start_index + end_index) // 2

    if some_list[mid] == element:
        return mid

    if element < some_list[mid]:
        return binary_search(element, some_list, start_index, mid - 1)
    else:
        return binary_search(element, some_list, mid + 1, end_index)