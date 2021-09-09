"""월간 코드 챌린지 시즌 2"""


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


print(solution([2, 7]))
