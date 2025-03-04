import sys

INPUT = sys.stdin.readline


def change_channels(first: int, second: int) -> str:
    ans = first * "1" + first * "4"
    if first > second:
        second += 1
    ans += second * "1" + (second - 1) * "4"

    return ans


if __name__ == "__main__":
    N = int(INPUT())
    KBS1, KBS2 = -1, -1
    for i in range(N):
        tmp = INPUT().strip()
        if tmp == "KBS1":
            KBS1 = i
        elif tmp == "KBS2":
            KBS2 = i
    print(change_channels(KBS1, KBS2))
