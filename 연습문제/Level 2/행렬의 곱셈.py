"""연습문제"""


def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr2[0])):
            num = 0
            for k in range(len(arr1[0])):
                num += arr1[i][k] * arr2[k][j]
            tmp.append(num)
        answer.append(tmp)
    return answer


solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])  # [[15, 15], [15, 15], [15, 15]]
solution(
    [[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
)  # [[22, 22, 11], [36, 28, 18], [29, 20, 14]]


# ------------------------------------------------------------------------------------------------

"""zip을 이용한 풀이"""


def solution(A, B):
    return [
        [sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A
    ]
