"""9663 N-Queen"""
"""i - j + n - 1과 i + j는 사진 참고"""

# 체스판 크기 n x n
n = int(input())

# 계산에 필요한 것들
count = 0  # 퀸을 놓을 수 있는 경우의 수
columns = [False] * n  # 같은 열에 못들어오도록
right_diagonal = [False] * (2 * n - 1)  # 오른쪽으로 향하는 대각선에 못들어오도록
left_diagonal = [False] * (2 * n - 1)  # 왼쪽으로 향하는 대각선에 못들어오도록


# 퀸을 놓을 수 있는 경우의 수를 구하는 함수
def solution(i):
    global count

    # 퀸을 끝 행까지 다 놓으면 경우의 수를 추가하고 리턴
    if i == n:
        count += 1
        return

    # 한 칸씩 열을 이동하면서 놓을 수 있는지 확인
    for j in range(n):
        # 지금까지 놓여 있는 퀸들의 열, 오른쪽/왼쪽 대각선에 모두 잡히지 않는다면 거기에 퀸을 놓고
        if not (columns[j] or right_diagonal[i - j + n - 1] or left_diagonal[i + j]):
            # 지금 놓은 퀸의 열, 오른쪽/왼쪽 대각선에 잡히는 위치를 True로 바꾼 뒤,
            columns[j] = right_diagonal[i - j + n - 1] = left_diagonal[i + j] = True
            # 다음 행으로 이동
            solution(i + 1)
            # 다 끝마치고 전 행으로 돌아오면 다른 경우의 수를 찾도록 지금 행의 퀸을 빼버림
            columns[j] = right_diagonal[i - j + n - 1] = left_diagonal[i + j] = False


# 0행부터 시작
solution(0)
print(count)