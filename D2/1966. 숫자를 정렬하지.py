def merge(list1, list2):
    i = 0  # list1의 인덱스
    j = 0  # list2의 인덱스
    merge_list = []

    while i < len(list1) and j < len(list2):  # 두 리스트를 비교
        if list1[i] < list2[j]:
            merge_list.append(list1[i])
            i += 1
        else:
            merge_list.append(list2[j])
            j += 1

    if i == len(list1):  # list2가 남았을 때
        merge_list += list2[j:]
    elif j == len(list2):  # list1이 남았을 때
        merge_list += list1[i:]

    return merge_list


def mergeSort(number):
    if len(number) <= 1:
        return number
    mid = len(number) // 2
    list1 = number[:mid]
    list2 = number[mid:]

    return merge(mergeSort(list1), mergeSort(list2))


test = int(input())

for t in range(test):
    num = int(input())
    numbers = list(map(int, input().split()))
    sort_list = mergeSort(numbers)
    print("#{}".format(t + 1), end=" ")
    print(*sort_list)