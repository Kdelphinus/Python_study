import sys

INPUT = sys.stdin.readline


def binary_search(goal: int, lst: list[int], start: int, end: int) -> int:
    mid = (start + end) // 2
    origin_start = start
    origin_end = end
    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == goal:
            return mid
        elif lst[mid] > goal:
            end = mid - 1
        else:
            start = mid + 1

    if mid > origin_start and abs(lst[mid] - goal) > abs(lst[mid - 1] - goal):
        return mid - 1
    elif mid < origin_end and abs(lst[mid] - goal) > abs(lst[mid + 1] - goal):
        return mid + 1
    return mid


def find_solution(solution: list[int]) -> list[int]:
    ans = [float("inf"), float("inf")]
    min_sol = float("inf")

    for i in range(len(solution) - 1):
        idx = binary_search(-solution[i], solution, i + 1, len(solution) - 1)
        if abs(solution[idx] + solution[i]) < min_sol:
            min_sol = abs(solution[idx] + solution[i])
            ans = [solution[i], solution[idx]]
            if min_sol == 0:
                return ans

    return ans


if __name__ == "__main__":
    N = int(INPUT())
    SOLUTION = list(map(int, INPUT().split()))
    print(*find_solution(SOLUTION))
