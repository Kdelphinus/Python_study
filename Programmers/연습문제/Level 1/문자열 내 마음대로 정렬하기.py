def solution(strings, n):
    strings.sort()  # 사전순으로 정렬
    answer = sorted(strings, key=lambda x: x[n])  # 원하는 문자열 위치기준으로 다시 정렬

    return answer
