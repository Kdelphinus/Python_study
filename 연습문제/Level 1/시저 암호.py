def solution(s, n):
    answer = ""
    for i in s:
        if 65 <= ord(i) <= 90:  # 대문자일 때
            if ord(i) + n <= 90:  # 알파벳을 밀어도 대문자이면
                answer += chr(ord(i) + n)  # 바로 바꾸고
            else:  # 대문자를 벗어난다면
                answer += chr(ord(i) + n - 26)  # Z -> A로 넘어감
        elif 97 <= ord(i) <= 122:  # 소문자일 때
            if ord(i) + n <= 122:  # 알파벳을 밀어도 소문자이면
                answer += chr(ord(i) + n)  # 바로 바꾸고
            else:  # 소문자를 벗어난다면
                answer += chr(ord(i) + n - 26)  # z -> a로 넘어감
        else:  # 공백이라면
            answer += i  # 바로 추가

    return answer
