def solution(n):
    answer = ""
    for i in range(1, n + 1):
        if i % 2:
            answer += "수"
        else:
            answer += "박"
    return answer
