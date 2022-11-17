"""24060 알고리즘 수업 - 병합 정렬 1"""


def merge(lst: list, p: int, q: int, r: int):
    global k, cnt, result

    i, j = p, q + 1
    tmp = []

    while i <= q and j <= r:
        if lst[i] <= lst[j]:
            tmp.append(lst[i])
            i += 1
        else:
            tmp.append(lst[j])
            j += 1

    while i <= q:
        tmp.append(lst[i])
        i += 1
    while j <= r:
        tmp.append(lst[j])
        j += 1

    i, j = p, 0

    while i <= r:
        lst[i] = tmp[j]
        cnt += 1
        if cnt == k:
            result = lst[i]
            return
        i += 1
        j += 1


def merge_sort(lst: list, p: int, r: int):
    global k, cnt

    if p < r and cnt <= k:
        q = (p + r) // 2
        merge_sort(lst, p, q)
        merge_sort(lst, q + 1, r)
        merge(lst, p, q, r)


if __name__ == "__main__":
    a, k = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt, result = 0, -1
    merge_sort(lst, 0, a - 1)
    print(result)
