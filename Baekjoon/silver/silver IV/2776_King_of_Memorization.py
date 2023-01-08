def binary_search(n: int) -> int:
    start, end = 0, n1 - 1
    while start <= end:
        mid = (start + end) // 2
        if n == note1[mid]:
            return 1
        elif n > note1[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0


t = int(input())
for _ in range(t):
    n1 = int(input())
    note1 = sorted(list(map(int, input().split())))
    n2 = int(input())
    note2 = list(map(int, input().split()))
    for num in note2:
        print(binary_search(num))
