# 13909 창문 닫기
# 결과를 보면 1, 4, 9, 16, 25... 등 제곱수에서 하나씩 증가함을 볼 수 있다.


def close_window(n: int) -> int:
    return int(n**0.5)


if __name__ == "__main__":
    print(close_window(int(input())))
