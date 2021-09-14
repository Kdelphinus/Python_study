test = int(input())

for t in range(test):
    p, q, r, s, w = map(
        int, input().split()
    )  # A사 리터당 가격, B사 기본 요금, B사 기준, B사 추가 요금, 사용량

    A = p * w

    if r >= w:
        B = q
    else:
        B = q + (w - r) * s

    print("#{} {}".format(t + 1, min(A, B)))