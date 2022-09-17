def solution(n):
    n = list(str(n))
    n.sort()
    answer = ""

    for i in range(len(n) - 1, -1, -1):
        answer += n[i]

    return int(answer)
