"""5639 이진 검색 트리"""
# 불필요한 재귀를 줄이면 시간이 아주 많이 단축된다
# 링크: https://www.acmicpc.net/source/30813571
import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def pre_to_post(start, end):
    if start > end:
        return

    root = preorder[start]  # 전위 순회는 루트를 가장 먼저 탐색

    # 루트 왼쪽에만 자식이 있을 때
    # 이 코드가 시간을 아주 많이 단축시킴
    if preorder[end] <= root:
        pre_to_post(start + 1, end)
        print(root)
        return

    # 오른쪽 자식이 시작되는 위치를 찾음
    for i in range(start + 1, end + 1):
        if preorder[i] > root:
            idx = i
            break

    pre_to_post(start + 1, idx - 1)  # 왼쪽 서브 트리 탐색
    pre_to_post(idx, end)  # 오른쪽 서브 트리 탐색
    print(root)


preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break
pre_to_post(0, len(preorder) - 1)


# ----------------------------------------------------------------------------------------------

# 링크: https://backtony.github.io/algorithm/2021-02-18-algorithm-boj-class4-20/
# 이진 검색 트리는 왼쪽은 루트보다 작고 오른쪽은 루트보다 큰 것을 기억할 것
import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def find_postorder(start, end):
    if start > end:
        return

    root = preorder[start]  # 전위 순회는 루트를 가장 먼저 탐색
    idx = start + 1  # 루트 다음 노드부터 확인

    # root보다 커지는 지점이 오른쪽 서브 트리의 시작 노드
    while idx <= end:
        if preorder[idx] > root:
            break
        idx += 1

    find_postorder(start + 1, idx - 1)  # 왼쪽 서브 트리
    find_postorder(idx, end)  # 오른쪽 서브 트리

    print(root)  # 루트를 가장 마지막에 탐색한다


preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:  # 입력이 더 이상 안들어오면 입력 종료
        break

find_postorder(0, len(preorder) - 1)
