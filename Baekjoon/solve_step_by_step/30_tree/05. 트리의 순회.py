"""2263 트리의 순회"""
# 링크: https://velog.io/@bae_mung/Python-BOJ-2263-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%88%9C%ED%9A%8C
import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def find_preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    # postorder의 맨 뒤는 항상 루트이다
    parent = postorder[post_end]
    print(parent, end=" ")

    # inorder는 루트를 기준으로 앞에 나오면 왼쪽 자식들, 뒤에 나오면 오른쪽 자식들이다
    left = position[parent] - in_start  # 마지막 왼쪽 자식의 위치
    right = in_end - position[parent]  # 첫 오른쪽 자식의 위치

    # 왼쪽 서브 트리 확인
    find_preorder(in_start, in_start + left - 1, post_start, post_start + left - 1)

    # 오른쪽 서브 트리 확인
    # postorder는 맨 뒤가 루트이므로 맨 뒤 값을 제외하도록, inorder는 중간에 루트가 있으므로 중간의 루트를 제외하도록 설정
    find_preorder(in_end - right + 1, in_end, post_end - right, post_end - 1)


num = int(input())
inorder = list(map(int, input().split()))  # 중위 순회 결과
postorder = list(map(int, input().split()))  # 후위 순회 결과

# inorder안에서 루트의 위치를 확인하기 위해 position에 index를 저장
position = [0] * (num + 1)
for i in range(num):
    position[inorder[i]] = i
find_preorder(0, num - 1, 0, num - 1)
