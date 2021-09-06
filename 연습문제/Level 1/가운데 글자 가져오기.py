def solution(s):
    answer = ""
    mid = len(s) // 2

    if len(s) % 2:  # 홀수면 가운데 글자 하나
        answer += s[mid]
    else:  # 짝수면 가운데 글자 두개
        answer += s[mid - 1 : mid + 1]

    return answer
