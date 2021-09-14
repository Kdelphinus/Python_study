def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append((list(sorted(array[i - 1 : j])))[k - 1])
    return answer


arr = [1, 5, 6, 9, 8, 7, 2, 3, 11]
com = [[1, 6, 2], [2, 5, 1], [4, 8, 2]]

print(solution(arr, com))