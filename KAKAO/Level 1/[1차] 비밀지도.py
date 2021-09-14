"""2018 KAKAO BLIND RECRUITMENT"""


def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        tmp = [0] * n

        num1 = arr1[i]  # 숫자를 꺼내고
        index = n - 1  # 이진수는 뒤에서부터 구해진다
        while num1 > 0:
            tmp[index] = num1 % 2
            num1 //= 2
            index -= 1

        num2 = arr2[i]
        index = n - 1
        while num2 > 0:
            if num2 % 2 == 1:
                tmp[index] = 1
            num2 //= 2
            index -= 1

        anw = ""
        for j in tmp:  # 구해진 이진수를
            if j:  # 1이면 #으로
                anw += "#"
            else:  # 0이면 공백으로
                anw += " "
        answer.append(anw)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
