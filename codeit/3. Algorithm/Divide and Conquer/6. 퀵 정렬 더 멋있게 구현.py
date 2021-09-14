def swap_elements(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


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


# 퀵 정렬
def quicksort(my_list, start = 0, end = None):
    if end == None:
        end = len(my_list) - 1
    if end - start <1:
        return
    pivot_index = partition(my_list, start, end)
    quicksort(my_list, start, pivot_index - 1)
    quicksort(my_list, pivot_index + 1, end)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)

