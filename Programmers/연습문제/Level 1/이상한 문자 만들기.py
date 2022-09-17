def solution(s):
    answer = ""
    flag = 0  # 짝수번째인지 홀수번째인지 알려주는 변수

    for i in s:
        if i.isalpha():  # 문자일 때
            if flag:  # 홀수번째면
                answer += i.lower()  # 소문자로
                flag = 0  # 다음은 짝수
            else:  # 짝수번째면
                answer += i.upper()  # 대문자로
                flag = 1  # 다음은 홀수
        else:  # 공백이면
            answer += " "  # 공백 저장
            flag = 0  # 첫 시작은 0이므로 짝수번째와 동일

    return answer
