"""2630 색종이 만들기"""
import sys

input = sys.stdin.readline


def oneColor(n, y, x):
    """종이가 한 가지 색으로만 되어있는지 확인하는 함수"""
    """n은 종이의 크기, x와 y는 색종이 왼쪽 위의 인덱스"""
    global blue_paper, white_paper

    if n == 1:  # 1 x 1 크기의 색종이일 때
        if paper[y][x] == 1:  # 파란 색종이일 때
            blue_paper += 1
        else:  # 하얀 색종이일 때
            white_paper += 1
        return

    flag = True  # 색종이의 모든 부분이 같은 색인지 확인
    for i in range(y, y + n):
        if not flag:  # 다른 색을 발견하면 반복문 종료
            break
        for j in range(x, x + n):
            if paper[i][j] != paper[y][x]:
                flag = False
                break

    if flag:  # 모두 같은 색일 때
        if paper[y][x] == 1:  # 파란 색종이일 때
            blue_paper += 1
        else:  # 하얀 색종이일 때
            white_paper += 1
    else:  # 다른 색이 있다면
        temp = n // 2  # 종이의 범위를 절반으로 나누고
        oneColor(temp, y, x)  # 2사분면
        oneColor(temp, y, x + temp)  # 1사분면
        oneColor(temp, y + temp, x)  # 3사분면
        oneColor(temp, y + temp, x + temp)  # 4사분면


num = int(input().rstrip())  # 색종이의 크기
paper = [list(map(int, input().split())) for _ in range(num)]  # 색종이 색 분포
white_paper, blue_paper = 0, 0  # 하얀 색종이와 파란 색종이의 수
oneColor(num, 0, 0)
print(white_paper)
print(blue_paper)