import sys

INPUT = sys.stdin.readline


def binary_search(num: int, flag: int):
    start, end, mid = 0, N - 1, -1
    while start <= end:
        mid = (start + end) // 2
        if LST[mid] == num:
            if flag:
                while mid - 1 >= 0 and LST[mid - 1] == num:
                    mid -= 1
                return mid
            else:
                while mid + 1 < N and LST[mid + 1] == num:
                    mid += 1
                return mid + 1
        elif LST[mid] > num:
            end = mid - 1
        elif LST[mid] < num:
            start = mid + 1
    while LST[mid] < num:
        mid += 1
    return mid


N, M = map(int, INPUT().split())
LST = sorted(list(map(int, INPUT().split())))

for _ in range(M):
    ORDER = list(map(int, INPUT().split()))
    if ORDER[0] == 1:
        if ORDER[1] > LST[-1]:
            print(0)
        elif ORDER[1] < LST[0]:
            print(N)
        else:
            print(N - binary_search(ORDER[1], 1))
    elif ORDER[0] == 2:
        if ORDER[1] > LST[-1]:
            print(0)
        elif ORDER[1] < LST[0]:
            print(N)
        else:
            print(N - binary_search(ORDER[1], 0))
    elif ORDER[0] == 3:
        if ORDER[2] < LST[0] or ORDER[1] > LST[-1]:
            print(0)
        elif ORDER[1] < LST[0] and ORDER[2] > LST[-1]:
            print(N)
        else:
            low = 0 if ORDER[1] < LST[0] else binary_search(ORDER[1], 1)
            high = N if ORDER[2] > LST[-1] else binary_search(ORDER[2], 0)
            print(high - low)
