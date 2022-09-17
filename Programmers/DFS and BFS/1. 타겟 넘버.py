from collections import deque


# 나의 풀이
# BFS 풀이
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([0, 0])

    while queue:
        total, level = queue.popleft()
        if level > len(numbers):
            break

        if level == len(numbers) and total == target:
            answer += 1
        elif level < len(numbers):
            queue.append([total + numbers[level], level + 1])
            queue.append([total - numbers[level], level + 1])

    return answer


print(solution([1, 1, 1, 1, 1], 3))


# --------------------------------------------------------------------------------------------

# 최다 추천 풀이
# 재귀를 이용한 풀이
def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target - numbers[0]) + solution(
            numbers[1:], target + numbers[0]
        )


# --------------------------------------------------------------------------------------------

# DFS 풀이
answer = 0


def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if idx == N and target == value:
        answer += 1
        return
    if idx == N:
        return

    DFS(idx + 1, numbers, target, value + numbers[idx])
    DFS(idx + 1, numbers, target, value - numbers[idx])


def solution(numbers, target):
    global answer
    DFS(0, numbers, target, 0)
    return answer
