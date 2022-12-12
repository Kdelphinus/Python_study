def is_knight(past: str, curr: str) -> bool:
    if not past:
        return True
    if abs(ord(past[0]) - ord(curr[0])) == 1 and abs(int(past[1]) - int(curr[1])) == 2:
        return True
    if abs(ord(past[0]) - ord(curr[0])) == 2 and abs(int(past[1]) - int(curr[1])) == 1:
        return True
    return False


def check_path(path: list) -> str:
    board = dict()
    for h in ("A", "B", "C", "D", "E", "F"):
        board[h] = [0 for _ in range(6)]

    past = ""
    for p in path:
        if board[p[0]][int(p[1]) - 1] or not is_knight(past, p):
            return "Invalid"
        board[p[0]][int(p[1]) - 1] = 1
        past = p
    if not is_knight(past, path[0]):
        return "Invalid"
    return "Valid"


if __name__ == "__main__":
    tour_path = list()
    for _ in range(36):
        tour_path.append(input())
    print(check_path(tour_path))
