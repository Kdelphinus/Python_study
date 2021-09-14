"""1992 쿼드트리"""
import sys

input = sys.stdin.readline


def compression(n, y, x):
    """이미지를 압축하는 함수"""
    if n == 1:  # 이미지가 1 x 1일 경우
        print(image[y][x], end="")
        return

    flag = True  # 같은 값만 있는지 확인하는 변수
    for i in range(y, y + n):
        if not flag:  # 다른 값이 있다면
            break
        for j in range(x, x + n):  # 잘린 사진 확인
            if image[y][x] != image[i][j]:
                flag = False
                break

    if flag:  # 같은 값만 있다면
        print(image[y][x], end="")
    else:  # 다른 값이 있다면
        print("(", end="")
        temp = n // 2
        compression(temp, y, x)  # 2사분면
        compression(temp, y, temp + x)  # 1사분면
        compression(temp, y + temp, x)  # 3사분면
        compression(temp, y + temp, temp + x)  # 4사분면
        print(")", end="")


num = int(input())  # 이미지 크기
image = [list(input().strip()) for _ in range(num)]  # 이미지, 정수로 받으면 앞에 0이 있는 것은 다 날라감
compression(num, 0, 0)