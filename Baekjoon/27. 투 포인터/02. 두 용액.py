"""2407 두 용액"""


def two_pointer(num, solutions):
    answer = []
    solutions.sort()  # 투 포인터 사용을 위해 정렬
    goal = 2000000000  # 0과 가장 먼 용액
    start, end = 0, num - 1
    while start < end:
        tmp = abs(solutions[start] + solutions[end])  # 두 용액을 섞었을 때

        if tmp == 0:  # 0이면 바로 리턴
            return [solutions[start], solutions[end]]

        if tmp < goal:  # 기존보다 더 0가 가까운 용액을 만들었다면 최신화
            goal = tmp
            answer = [solutions[start], solutions[end]]

        # 포인터가 가리키는 수들의 합이 더 작아질 수 있도록 이동
        if solutions[start] > 0 and solutions[end] > 0:  # 둘 다 양수일 때
            end -= 1
        elif solutions[start] < 0 and solutions[end] < 0:  # 둘 다 음수일 때
            start += 1
        else:  # 양수와 음수일 때, 혹은 0이 있을 때
            if abs(solutions[start]) < abs(solutions[end]):
                end -= 1
            else:
                start += 1

    return answer


num = int(input())
solutions = list(map(int, input().split()))
print(*two_pointer(num, solutions))

# -------------------------------------------------------------------------------

"""다른 답안"""
# input 입력 받기
n = int(input())
solution = list(map(int, input().split()))

# 정렬하기
solution.sort()

# 이중포인터 설정
left = 0
right = n - 1

answer = 2e9 + 1  # 기준값
final = []  # 정답

# 투포인터 진행
while left < right:
    s_left = solution[left]
    s_right = solution[right]

    tot = s_left + s_right
    # 두 용액의 합이 0과 가장 가까운 용액을 정답에 담아주기
    if abs(tot) < answer:
        answer = abs(tot)
        final = [s_left, s_right]

    # 두 용액의합이 0보다 작다면 왼쪽의 값을 늘려 조금 더 0에 가깝게 만들어준다
    if tot < 0:
        left += 1
    # 반대로, 두 용액의 합이 0보다 크다면 오른쪽의 값을 줄여서 조금 더 0에 가깝게 만들어준다
    else:
        right -= 1

print(final[0], final[1])
