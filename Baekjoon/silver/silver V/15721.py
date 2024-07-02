import sys

INPUT = sys.stdin.readline


def solution(num: int, goal: int, flag: int) -> int:
    bbun, daegi, cnt = 0, 0, 2
    while True:
        for i in range(4 + cnt * 2):
            if i < 4:
                if i % 2:
                    daegi += 1
                else:
                    bbun += 1
            elif i < cnt + 4:
                bbun += 1
            else:
                daegi += 1
            if (flag == 0 and bbun == goal) or (flag == 1 and daegi == goal):
                ans = (bbun + daegi) % num - 1
                return num - 1 if ans == -1 else ans
        cnt += 1


if __name__ == "__main__":
    A = int(INPUT())
    T = int(INPUT())
    FLAG = int(INPUT())
    print(solution(A, T, FLAG))
