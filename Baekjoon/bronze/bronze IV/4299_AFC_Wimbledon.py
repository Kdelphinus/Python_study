def score(p: int, m: int) -> str:
    if (p + m) % 2 != 0:
        return "-1"
    winner = (p + m) // 2
    looser = p - winner
    if winner < 0 or looser < 0:
        return "-1"
    return f"{winner} {looser}"


if __name__ == "__main__":
    plus, minus = map(int, input().split())
    print(score(plus, minus))
