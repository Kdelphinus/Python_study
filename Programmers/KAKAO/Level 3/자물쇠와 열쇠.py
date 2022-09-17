"""2020 KAKAO BLIND RECRUITMENT"""
# brute force를 사용, 코딩테스트에서 numpy를 인정해주지 않는 경우가 많으므로 안 쓰고 푸는 것도 공부해야 함

import numpy as np


def solution(key, lock):
    n, m = len(key), len(lock)
    lock = np.pad(lock, ((n - 1, n - 1), (n - 1, n - 1)))  # lock의 범위를 늘림

    # key를 한 칸씩 옮겨보며 확인
    for i in range(n + m - 1):
        for j in range(n + m - 1):
            # key를 90도씩 회전
            for _ in range(4):

                # key를 lock에 끼워봄
                for y in range(i, i + n):
                    for x in range(j, j + n):
                        lock[y][x] += key[y - i][x - j]

                flag = True
                for y in range(n - 1, n + m - 1):
                    if not flag:
                        break
                    for x in range(n - 1, n + m - 1):
                        if lock[y][x] != 1:  # key와 lock이 맞지 않으면
                            flag = False  # 실패 표시
                            break

                if flag:  # key가 맞았을 때
                    return True

                # key가 맞지 않으면 다시 lock를 초기화
                for y in range(i, i + n):
                    for x in range(j, j + n):
                        lock[y][x] -= key[y - i][x - j]

                key = np.rot90(key)  # 90도 회전

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))

# ---------------------------------------------------------------------------------------------

"""numpy를 쓰지 않는 답안"""
# 링크: https://johnyejin.tistory.com/127

# 90도 회전
def rotation(arr):
    n = len(arr)
    ret = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ret[j][n - 1 - i] = arr[i][j]
    return ret


# 자물쇠가 열리는지 췍
def check(startX, startY, key, lock, expendSize, start, end):
    expendList = [[0] * expendSize for _ in range(expendSize)]

    # expendList에 key 추가
    for i in range(len(key)):
        for j in range(len(key)):
            expendList[startX + i][startY + j] += key[i][j]

    # expendList에 lock 추가하면서 기존 값이랑 더하기
    for i in range(start, end):
        for j in range(start, end):
            expendList[i][j] += lock[i - start][j - start]
            if expendList[i][j] != 1:
                return False

    return True


def solution(key, lock):
    start = len(key) - 1  # expendList에서 lock의 시작 지점
    end = start + len(lock)  # expendList에서 lock이 끝나는 지점
    expendSize = len(lock) + start * 2  # expendList 배열의 크기

    # lock은 고정이고 key가 움직이는거!!!
    for a in range(0, 4):
        for i in range(end):
            for j in range(end):
                if check(i, j, key, lock, expendSize, start, end):
                    return True
        key = rotation(key)

    return False
