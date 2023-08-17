# 비둘기 집의 원리: https://ko.wikipedia.org/wiki/%EB%B9%84%EB%91%98%EA%B8%B0%EC%A7%91_%EC%9B%90%EB%A6%AC
# mbti 개수가 16개이므로 32개가 넘어가면 무조건 겹치는 3개를 찾을 수 있다.


def diff_str(str1: str, str2: str, str3: str) -> int:
    if str1 == str2 == str3:
        return 0

    diff = 0
    for s1, s2 in zip(str1, str2):
        if s1 != s2:
            diff += 1
    for s1, s3 in zip(str1, str3):
        if s1 != s3:
            diff += 1
    for s2, s3 in zip(str2, str3):
        if s2 != s3:
            diff += 1
    return diff


def psycho_dist(n: int, mbti: list) -> int:
    if n > 32:
        return 0
    dist = float("inf")
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                dist = min(dist, diff_str(mbti[i], mbti[j], mbti[k]))
    return dist


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        MBTI = list(input().split())
        print(psycho_dist(N, MBTI))
