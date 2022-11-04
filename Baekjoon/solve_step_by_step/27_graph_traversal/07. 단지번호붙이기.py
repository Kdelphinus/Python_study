"""2667 단지번호붙이기"""
import sys

input = sys.stdin.readline
anw = 0  # 단지 내 집의 수를 저장할 변수


def DFS(i, j):
    """DFS

    Args:
        i (int): 가로 좌표
        j (int): 세로 좌표
    """
    global anw
    visit[i][j] = 1  # 탐색한 집으로 표시
    anw += 1  # 단지 내 집의 수 추가

    # 차례대로 오른쪽, 왼쪽, 아래쪽, 위쪽을 확인하여 탐색하지 않았고 집이 있다면 탐색
    if i + 1 < num and house_map[i + 1][j] == "1" and visit[i + 1][j] == 0:
        DFS(i + 1, j)
    if i - 1 >= 0 and house_map[i - 1][j] == "1" and visit[i - 1][j] == 0:
        DFS(i - 1, j)
    if j + 1 < num and house_map[i][j + 1] == "1" and visit[i][j + 1] == 0:
        DFS(i, j + 1)
    if j - 1 >= 0 and house_map[i][j - 1] == "1" and visit[i][j - 1] == 0:
        DFS(i, j - 1)


num = int(input())  # 지도의 크기 num x num
house_map = [list(input().strip()) for _ in range(num)]  # 지도, 문자들을 따로 받기 위하여 strip 사용
visit = [[0] * num for _ in range(num)]  # 방문했는지 표시할 지도
answer = []  # 각 단지 별 집의 수가 저장될 리스트

for i in range(num):
    for j in range(num):
        if visit[i][j] == 0 and house_map[i][j] == "1":  # 탐색하지 않았고 집이 있는 곳이라면
            DFS(i, j)  # 탐색하고
            answer.append(anw)  # 단지 내 집의 수를 저장한 뒤
            anw = 0  # 변수 초기화

answer.sort()  # 오름차순 정렬
print(len(answer))  # 단지 개수
for i in answer:  # 단지 내 집의 개수
    print(i)
