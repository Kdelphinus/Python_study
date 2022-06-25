"""1806 부분합"""

INF = float("inf")


def two_pointer(num, goal, numbers):
    anw = INF  # 만들 수 없다면 무한의 길이를 가짐
    end = 0
    tmp = 0

    if goal in numbers:  # 배열에 그 숫자가 있다면 하나로 만들 수 있음
        return 1

    for start in range(num):
        while end < num and tmp < goal:  # 부분합이 goal을 넘을 때까지 end를 뒤로 옮기며 더함
            tmp += numbers[end]
            end += 1

        if tmp >= goal:  # 부분합이 goal보다 크면 길이를 최신화
            anw = min(anw, end - start)  # while을 나올 때 end가 하나 더 뒤로 가기에 1을 더하지 않음
        tmp -= numbers[start]  # start가 뒤로 한 칸 이동하기에 부분합에서 빠질 값을 빼줌

    return anw if anw < INF else 0


num, goal = map(int, input().split())
numbers = list(map(int, input().split()))
print(two_pointer(num, goal, numbers))
