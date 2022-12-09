def flip(n: int):
    fish_shaped_burn = [input() for _ in range(n)]
    for f in fish_shaped_burn:
        print(f[::-1])


if __name__ == "__main__":
    n, m = map(int, input().split())
    flip(n)
