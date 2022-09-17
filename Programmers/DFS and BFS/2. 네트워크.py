"""나의 풀이"""
from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False] * n  # 탐색했는지 여부를 나타내는 배열

    for i in range(n):
        if not visited[i]:  # 아직 탐색하지 않은 컴퓨터일 때
            visited[i] = True  # 탐색했다고 표시
            queue = deque()
            queue.append(i)

            while queue:  # 큐가 빌 때까지 반복
                num = queue.popleft()  # 가장 앞의 컴퓨터를 빼고
                for j in range(n):
                    if (
                        not visited[j] and computers[num][j]
                    ):  # 아직 방문하지 않았으며 뺀 컴퓨터와 연결된 컴퓨터일 때
                        visited[j] = True
                        queue.append(j)
            answer += 1  # 네트워크 하나 생성

    return answer
