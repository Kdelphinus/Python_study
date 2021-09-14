"""2019 카카오 개발자 겨울 인턴십"""


def solution(board, moves):
    box = []
    answer = 0

    y = len(board)
    x = len(board[0])
    dolls = [-1] * x

    for i in range(x):
        if board[0][i]:
            dolls[i] = 0
        else:
            for j in range(y - 1, -1, -1):
                if board[j][i] == 0:
                    dolls[i] = j + 1
                    break

    for i in moves:
        index_x = i - 1
        index_y = dolls[index_x]
        tmp = 0

        if index_y < y:
            tmp = board[index_y][index_x]
            board[index_y][index_x] = 0
            dolls[index_x] += 1

        if len(box) > 0 and box[-1] == tmp:
            box.pop()
            answer += 2
        elif tmp:
            box.append(tmp)

    return answer


# ------------------------------------------------------------------------------------
# 스택을 정석적으로 이용
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                stacklist.append(board[j][i - 1])
                board[j][i - 1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer
