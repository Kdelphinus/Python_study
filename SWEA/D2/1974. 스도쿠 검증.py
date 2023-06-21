test = int(input())

for t in range(test):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    flag = True

    for i in range(9):
        for j in range(9):
            for k in range(9):
                if sudoku[i][j] == sudoku[i][k] and j != k:
                    flag = False
                    break
                if sudoku[i][j] == sudoku[k][j] and i != k:
                    flag = False
                    break
            if not flag:
                break
            for k in range(i // 3 * 3, i // 3 * 3 + 3):
                for q in range(j // 3 * 3, j // 3 * 3 + 3):
                    if sudoku[i][j] == sudoku[k][q] and i != k and j != q:
                        flag = False
                        break
                if not flag:
                    break
            if not flag:
                break
        if not flag:
            break

    if flag:
        print("#{} 1".format(t + 1))
    else:
        print("#{} 0".format(t + 1))
