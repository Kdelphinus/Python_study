"""2751 수 정렬하기 2"""
"""O(nlogn)인 정렬 알고리즘으로 풀 수 있다 -> 병합 정렬, 힙 정렬 등"""


# 두 리스트를 병합하며 정렬하는 함수
def merge(list1, list2):
    i = 0
    j = 0

    merged_list = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    if i == len(list1):
        merged_list += list2[j:]
    elif j == len(list2):
        merged_list += list1[i:]

    return merged_list


# 리스트를 합병 정렬하는 리스트
def merged_sort(temp_list):
    if len(temp_list) <= 1:
        return temp_list

    middle = len(temp_list) // 2
    list1 = temp_list[:middle]
    list2 = temp_list[middle:]

    return merge(merged_sort(list1), merged_sort(list2))


# 받을 숫자의 개수
n = int(input())

# 숫자를 담을 리스트
num = []

# 숫자를 받아 num에 저장
for _ in range(n):
    temp = int(input())
    num.append(temp)

# 합병 정렬
num_sort = merged_sort(num)

# 정렬된 리스트를 출력
for i in range(n):
    print(num_sort[i])