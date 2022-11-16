# 20210805의 풀이: https://www.acmicpc.net/source/48139799
# 이게 왜 그리디...?
# 브루트 포스 응용에 가까운 느낌

import sys

INPUT = sys.stdin.readline


def joystick(name: str) -> int:
    length = len(name)
    offsets = [min(ord(s) - ord("A"), ord("Z") - ord(s) + 1) for s in name]
    change = sum(offsets)
    if change == 0:
        return 0

    idx = [i for i, offset in enumerate(offsets) if offset != 0]
    move = idx[-1]  # 오른쪽으로만 이동하면서 끝까지 이동하는 거리
    if len(idx) >= 2:  # 오른쪽으로만 쭉 이동하는 거리와 왼쪽으로만 쭉 이동하는 거리 중 짧은 것으로
        move = min(move, length - (idx[0] if idx[0] != 0 else idx[1]))
    for i in range(len(idx) - 1):  # 오른쪽 이동으로 i에 도달하고 왼쪽으로 이동하여 i + 1에 도달할 때 거리
        move = min(move, 2 * idx[i] + length - idx[i + 1])
    for i in range(1, len(idx)):  # 왼쪽 이동으로 i에 도달하고 오른쪽으로 이동하여 i - 1에 도달할 때 거리
        move = min(move, 2 * (length - idx[i]) + idx[i - 1])

    return change + move


if __name__ == "__main__":
    for _ in range(int(INPUT())):
        print(joystick(INPUT().rstrip()))
