"""2447 별 찍기 - 10"""


def stars(star_list):
    # 별 그림을 담을 리스트
    matrix = []

    # 주어진 리스트보다 가로, 세로가 3배 큰 리스트를 matrix에 담음
    for i in range(3 * len(star_list)):
        if i // len(star_list) == 1:  # star_list를 복사하여 알맞은 위치에 복사, 이때 가운데는 빈 칸으로
            matrix.append(
                star_list[i % len(star_list)]
                + " " * len(star_list)
                + star_list[i % len(star_list)]
            )
        else:  # star_list를 복사하여 알맞은 위치에 복사
            matrix.append(star_list[i % len(star_list)] * 3)
    return matrix


# 입력 (N = 3 ** K, K는 1 이상의 자연수)
N = int(input())

# base (N = 3일 때)
star = ["***", "* *", "***"]

# K - 1 구하기
k = 0
while N != 3:
    N = int(N / 3)
    k += 1

# k번만큼 재귀
for i in range(k):
    star = stars(star)

# 주어진 별그림 리스트 출력
for i in star:
    print(i)
