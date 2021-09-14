def solution(phone_number):
    answer = ""

    star = len(phone_number) - 4
    for i in range(star):
        answer += "*"
    answer += phone_number[-4:]
    return answer
