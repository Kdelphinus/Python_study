"""월간 코드 챌린지 시즌 1"""


def solution(arr):
    answer = [0, 0]
    n = len(arr)

    def quad_tree(n, x, y):
        if n == 1:
            answer[arr[y][x]] += 1
            return

        flag = True
        for i in range(y, y + n):
            if not flag:
                break
            for j in range(x, x + n):
                if arr[y][x] != arr[i][j]:
                    flag = False
                    break

        if flag:
            answer[arr[y][x]] += 1
        else:
            n //= 2
            quad_tree(n, x, y)
            quad_tree(n, x + n, y)
            quad_tree(n, x, y + n)
            quad_tree(n, x + n, y + n)

    quad_tree(n, 0, 0)
    return answer


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
