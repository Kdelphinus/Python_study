# https://yeorii.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-30804%EB%B2%88-%EA%B3%BC%EC%9D%BC-%ED%83%95%ED%9B%84%EB%A3%A8-%ED%88%AC%ED%8F%AC%EC%9D%B8%ED%84%B0-%EB%B8%8C%EB%A3%A8%ED%8A%B8%ED%8F%AC%EC%8A%A4-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
import sys

sys.setrecursionlimit(10**8)
INPUT = sys.stdin.readline


def tanghuru(start: int, end: int, kind: int) -> None:
    """
    앞에 과일부터 하나씩 추가해가며 두 개의 종류를 가진 가장 긴 탕후루 찾기
    Args:
        start: 탕후루의 가장 왼쪽 부분
        end: 탕후루의 가장 오른쪽 부분
        kind: 현재 탕후루의 과일 종류 개수

    Returns:
        2가지 종류의 과일을 가진 탕후루의 가장 긴 길이
    """
    global MAX_NUM

    if end >= N:
        return

    COUNT[FRUITS[end]] += 1
    if COUNT[FRUITS[end]] == 1:
        kind += 1

    # 과일 종류가 2개를 넘어갈 경우 앞에 과일 하나 빼기
    if kind > 2:
        COUNT[FRUITS[start]] -= 1
        if COUNT[FRUITS[start]] == 0:
            kind -= 1
        start += 1
    MAX_NUM = max(MAX_NUM, end - start + 1)
    return tanghuru(start, end + 1, kind)


if __name__ == "__main__":
    N = int(INPUT())
    FRUITS = list(map(int, INPUT().split()))
    COUNT = [0] * 10
    MAX_NUM = 0
    tanghuru(0, 0, 0)
    print(MAX_NUM)
