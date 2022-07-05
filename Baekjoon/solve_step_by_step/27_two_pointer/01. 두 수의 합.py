"""3273 두 수의 합"""


def two_pointer(num, numbers, goal):
    """two_pointer

    Args:
        num (int): 주어진 수의 개수
        numbers (list): 주어진 수들이 저장된 리스트
        goal (int): 만들고 싶은 수

    Returns:
        cnt (int): goal을 만들 수 있는 조합의 수
    """
    cnt = 0
    numbers.sort()  # 주어진 수들을 정렬해야 사용 가능
    start, end = 0, num - 1  # 두 개의 포인터는 맨 앞과 맨 뒤로 초기화

    while start < end:
        tmp = numbers[start] + numbers[end]
        if tmp < goal:  # goal보다 작으면 start를 뒤로 한 칸 움직인다
            start += 1
            continue

        if tmp == goal:  # goal을 만들었다면 cnt 추가
            cnt += 1
        end -= 1  # goal 이상의 수를 만들었다면 end를 앞으로 한 칸 움직인다

    return cnt


num = int(input())
numbers = list(map(int, input().split()))
goal = int(input())

print(two_pointer(num, numbers, goal))
