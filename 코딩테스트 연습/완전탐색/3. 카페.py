"""나의 답안"""


def solution(brown, yellow):
    total = brown + yellow  # 총 타일 개수, 가로 x 세로는 총 타일 개수와 동일

    for i in range(3, int(total ** 0.5) + 1):  # 갈색이 노랑을 감싸기 때문에 가로, 세로는 최소 3이어야 한다
        # 세로 길이(i)가 total의 약수이고 가운데 타일 개수가 노랑색의 개수와 같으면
        if total % i == 0 and yellow == (i - 2) * ((total // i) - 2):
            return [total // i, i]


print(solution(10, 2))
