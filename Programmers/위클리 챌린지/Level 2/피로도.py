"""위클리 챌린지 12주차"""
from itertools import permutations


def solution(k, dungeons):
    answer = -1
    for dungeon in permutations(dungeons):
        cnt = 0
        energy = k
        for minimum, waste in dungeon:
            if energy < minimum:
                break

            energy -= waste
            cnt += 1
        answer = max(cnt, answer)
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))

# ---------------------------------------------------------------------------------

"""DFS를 이용한 풀이"""

answer = []


def solution(k, dungeons):
    def __DFS(k, dungeons, depth):
        tmp = True
        for d in range(len(dungeons)):
            dun = dungeons[d]
            if dun[0] <= k:  # 던전을 갈 수 있다면
                tmp_dungeons = dungeons[:]  # 던전 리스트 복사
                del tmp_dungeons[d]  # 지금 간 던전은 제거
                __DFS(k - dun[1], tmp_dungeons, depth + 1)  # 다음 던전으로 이동
                tmp = False  # 아직 갈 수 있는 던전이 남아있다

        if tmp:  # 갈 수 있는 던전이 없다면
            answer.append(depth)  # 지금까지 돌아본 던전을 저장

    __DFS(k, dungeons, 0)

    return max(answer)
