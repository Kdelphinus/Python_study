"""위클리 챌린지 9주차"""


def solution(n, wires):
    answer = n

    # 와이어에 대한 그래프 생성
    tree = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        tree[v1].append(v2)
        tree[v2].append(v1)

    # 한 줄씩 끊어봄
    for i in range(n - 1):
        rm1, rm2 = wires[i]  # 끊은 와이어가 연결되어 있던 전신주
        tmp = [[rm1], [rm2]]  # 두 전력망으로 나뉨
        remain = []  # 어느 전력망인지 확인하지 못한 전신주를 넣을 리스트

        # rm1과 연결된 전신주는 전력망1에 추가
        for k in tree[rm1]:
            if k != rm2:
                tmp[0].append(k)

        # rm2와 연결된 전신주는 전력망2에 추가
        for k in tree[rm2]:
            if k != rm1:
                tmp[1].append(k)

        # wires를 토대로 전력망 배치
        for j in range(len(wires)):
            if i != j:  # 제거한 전선이 아닐 때
                if wires[j][0] in tmp[0]:
                    tmp[0].append(wires[j][1])
                elif wires[j][0] in tmp[1]:
                    tmp[1].append(wires[j][1])
                elif wires[j][1] in tmp[0]:
                    tmp[0].append(wires[j][0])
                elif wires[j][1] in tmp[1]:
                    tmp[1].append(wires[j][0])
                else:  # 어느 전력망인지 아직 모를 때
                    remain.append(wires[j][0])
                    remain.append(wires[j][1])

        # 확인하지 못한 전신주들을 다시 확인
        while remain:
            flag = False
            k = remain.pop(0)
            for j in tree[k]:
                if j in tmp[0]:
                    tmp[0].append(k)
                    flag = True
                    break
                elif j in tmp[1]:
                    tmp[1].append(k)
                    flag = True
                    break
            if not flag:
                remain.append(k)

        # 중복 제거
        tmp[0] = set(tmp[0])
        tmp[1] = set(tmp[1])
        answer = min(answer, abs(len(tmp[0]) - len(tmp[1])))

    return answer


# ------------------------------------------------------------------------------------------------------

"""다른 답안"""
# 구동방식을 아직 정확히 이해 못함
uf = []


def find(a):
    global uf
    if uf[a] < 0:
        return a
    uf[a] = find(uf[a])
    return uf[a]


def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb:
        return
    uf[pa] += uf[pb]
    uf[pb] = pa


def solution(n, wires):
    global uf
    answer = int(1e9)
    k = len(wires)
    for i in range(k):
        uf = [-1 for _ in range(n + 1)]
        tmp = [wires[x] for x in range(k) if x != i]
        for a, b in tmp:
            merge(a, b)
        v = [x for x in uf[1:] if x < 0]
        answer = min(answer, abs(v[0] - v[1]))

    return answer


print(solution(4, [[1, 2], [2, 3], [3, 4]]))
