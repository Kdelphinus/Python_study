"""9184 신나는 함수 실행"""

while True:
    a, b, c = map(int, input().split())

    # 종결 선언
    if a == b == c == -1:
        break

    def w_function(a, b, c, w_cach):
        """w함수의 값을 저장한 딕셔너리를 먼저 확인하고 계산"""

        # base case
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        if a > 20 or b > 20 or c > 20:
            return w_function(20, 20, 20, w_cach)

        # 이미 값이 저장되어 있을 때
        if (a, b, c) in w_cach:
            return w_cach[a, b, c]

        # 값이 없다면
        if a < b < c:
            w_cach[a, b, c] = (
                w_function(a, b, c - 1, w_cach)
                + w_function(a, b - 1, c - 1, w_cach)
                - w_function(a, b - 1, c, w_cach)
            )
        else:
            w_cach[a, b, c] = (
                w_function(a - 1, b, c, w_cach)
                + w_function(a - 1, b - 1, c, w_cach)
                + w_function(a - 1, b, c - 1, w_cach)
                - w_function(a - 1, b - 1, c - 1, w_cach)
            )

        return w_cach[a, b, c]

    def w_dict(a, b, c):
        """딕셔너리를 생성하고 계산한 값이 저장된 딕셔너리 보관"""
        w_cach = {}

        return w_function(a, b, c, w_cach)

    print(f"w({a}, {b}, {c}) = {w_dict(a, b, c)}")
