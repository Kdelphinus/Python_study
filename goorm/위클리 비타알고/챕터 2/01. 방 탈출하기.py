def binary_search(num, start, end):
    if start > end:  # 종결조건, 값이 없다
        return False

    mid = (start + end) // 2
    # 시작, 중간, 끝 인덱스 중 값이 있다면 종료
    if example[mid] == num or example[start] == num or example[end] == num:
        return True

    # 중간값보다 크다면 오른쪽만 확인
    if example[mid] > num:
        return binary_search(num, start + 1, mid - 1)
    # 중간값보다 작으면 왼쪽만 확인
    else:
        return binary_search(num, mid + 1, end - 1)


example_len = int(input())
example = list(map(int, input().split()))
example.sort()  # 이분 탐색을 위해 정렬
check_num = int(input())
for c in input().split():
    if binary_search(int(c), 0, example_len - 1):
        print(1)
    else:
        print(0)
