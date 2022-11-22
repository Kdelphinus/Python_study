def white_space(b: list) -> int:
    """
    흰 칸 위에 놓인 말의 개수를 반환하는 함수
    Args:
        b: 체스판

    Returns:
        cnt: 흰 칸 위에 놓인 말의 개수

    """
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0 and b[i][j] == "F":
                cnt += 1
    return cnt


if __name__ == "__main__":
    board = [input() for _ in range(8)]
    print(white_space(board))
