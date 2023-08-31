import sys

INPUT = sys.stdin.readline


def score(n, string):
    sub_str = []
    for i in range(1, len(string) - 1):
        for j in range(i + 1, len(string)):
            tmp1, tmp2, tmp3 = "".join(string[:i]), "".join(string[i:j]), "".join(string[j:])
            sub_str.append(tmp1)
            sub_str.append(tmp2)
            sub_str.append(tmp3)
    sub_str = sorted(list(set(sub_str)))

    cnt = 0
    for i in range(1, len(string) - 1):
        for j in range(i + 1, len(string)):
            tmp1, tmp2, tmp3 = "".join(string[:i]), "".join(string[i:j]), "".join(string[j:])
            cnt = max(cnt, sub_str.index(tmp1) + sub_str.index(tmp2) + sub_str.index(tmp3) + 3)

    return cnt


if __name__ == "__main__":
    N = int(INPUT())
    STRING = INPUT().strip()
    print(score(N, STRING))