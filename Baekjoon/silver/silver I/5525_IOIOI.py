#


def ioioi() -> int:
    ans, cnt, i = 0, 0, 0
    n = int(input())
    m = int(input())
    string = input()

    while i < m - 1:
        if string[i : i + 3] == "IOI":
            i += 2
            cnt += 1
            if cnt == m:
                ans += 1
                cnt -= 1
        else:
            i += 1
            cnt = 0

    return ans


if __name__ == "__main__":
    print(ioioi())
