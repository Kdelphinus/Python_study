"""월간 코드 챌린지 시즌 2"""

"""
- 홀수일 때 원리
3 = 011 (마지막 1의 개수 2개)
4 = 100
5 = 101 (3 + (2 ** (1의 개수-1) )) = (3 + (2** (2-1) )) = 5

7 = 111 (마지막 1의 개수 3개)
8 = 1000
9 = 1001
10 = 1010
11 = 1011 (7 + (2 ** (1의개수) -1)) = (7 + (2** (3-1)) ) = 11

- 짝수일 땐 맨 뒤가 무조건 0이므로 다음 숫자가 된다
"""


def solution(numbers):
    answer = []
    for number in numbers:
        cnt = 0
        if number % 2:
            bin_num = bin(number)
            for i in range(len(bin_num) - 1, -1, -1):
                if bin_num[i] != "1":
                    break
                cnt += 1
            answer.append(number + 2 ** (cnt - 1))
        else:
            answer.append(number + 1)
    return answer


# -------------------------------------------------------------------------------------------

"""비트 연산자를 이용한 간단한 풀이"""
# 링크: https://programmers.co.kr/learn/courses/30/lessons/77885/solution_groups?language=python3


def solution(numbers):
    answer = []
    for idx, val in enumerate(numbers):
        answer.append(((val ^ (val + 1)) >> 2) + val + 1)

    return answer


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
