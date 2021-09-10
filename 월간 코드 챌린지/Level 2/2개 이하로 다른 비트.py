"""월간 코드 챌린지 시즌 2"""


# -------------------------------------------------------------------------------------------

"""내장함수를 사용했으나 시간초과, 밑에 코드보단 효율이 훨씬 좋음"""


def solution(numbers):
    answer = []
    for number in numbers:
        num = number + 1
        while bin(number ^ num).count("1") > 2:
            num += 1
        answer.append(num)
    return answer


print(solution([2, 7]))

# -------------------------------------------------------------------------------------------

"""길이가 긴 두 케이스에서 시간초과"""


def solution(numbers):
    answer = []
    for number in numbers:
        num = number + 1
        standard = format(number, "b")
        while True:
            flag = 0
            tmp = format(num, "b")
            tmp_standard = standard.zfill(len(tmp))
            for i in range(len(tmp)):
                if tmp[i] != tmp_standard[i]:
                    flag += 1
                    if flag > 2:
                        break
            if flag <= 2:
                answer.append(num)
                break
            num += 1
    return answer
