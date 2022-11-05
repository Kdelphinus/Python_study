"""2563 색종이"""


def paper_init(width: int = 100, height: int = 100) -> list:
    return [[0] * (width + 1) for _ in range(height + 1)]


def glue_paper(n: int) -> list:
    paper = paper_init()
    for _ in range(n):
        x, y = map(int, input().split())
        for i in range(y, y + 10):
            for j in range(x, x + 10):
                if paper[i][j] == 0:
                    paper[i][j] = 1
    return paper


def colored_paper(n: int) -> int:
    area, paper = 0, glue_paper(n)
    for p in paper:
        area += sum(p)
    return area


if __name__ == "__main__":
    print(colored_paper(int(input())))
