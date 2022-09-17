# # 문제 의도와 상관없이 내 방식으로 풀은 답안
# def merge_sort(list):
#     if len(list) <= 1:
#         return sorted(list)
#     mid = int(len(list) / 2)
#     return sorted(merge_sort(list[:mid]) + merge_sort(list[mid:]))
    

# # 테스트
# print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
# print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
# print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))

# ----------------------------------------------------------------------------

# 문제의도대로 풀은 답안
def merge(list1, list2):
    i = 0
    j = 0

    # 정렬된 항목들을 담을 리스트
    merged_list = []

    # list1과 list2를 돌면서 merged_list에 항목 정렬
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    # list2에 남은 항목이 있으면 정렬 리스트에 추가
    if i == len(list1):
        merged_list += list2[j:]

    # list1에 남은 항목이 있으면 정렬 리스트에 추가
    elif j == len(list2):
        merged_list += list1[i:]

    return merged_list
    

# 합병 정렬
def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    mid = int(len(my_list) / 2)
    list1 = my_list[:mid]
    list2 = my_list[mid:]

    return merge(merge_sort(list1), merge_sort(list2))
    
    

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
