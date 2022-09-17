"""연습문제"""
cnt = 0


def solution(n):
    width = [False] * n
    left_diagonal = [False] * (2 * n)
    right_diagonal = [False] * (2 * n)

    def n_queen(y):
        global cnt

        if y == n:
            cnt += 1
            return

        for x in range(n):
            if not (width[x] or left_diagonal[x - y + n - 1] or right_diagonal[x + y]):
                width[x] = left_diagonal[x - y + n - 1] = right_diagonal[x + y] = True
                n_queen(y + 1)
                width[x] = left_diagonal[x - y + n - 1] = right_diagonal[x + y] = False

    n_queen(0)

    return cnt
