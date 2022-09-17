def solution(arr):
    answer = []

    tmp = -1
    for i in arr:
        if tmp != i:
            tmp = i
            answer.append(i)

    return answer
