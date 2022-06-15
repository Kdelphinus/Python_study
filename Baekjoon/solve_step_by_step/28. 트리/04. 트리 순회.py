"""1991 트리 순회"""
# 링크: https://jm-codingmemo.tistory.com/22
import sys

input = sys.stdin.readline


def preorder(root):
    """preorder 전위 순회할 때 방문하는 순서를 출력하는 함수

    * 탐색 우선 순위: 루트 > 왼쪽 자식 > 오른쪽 자식

    Args:
        root (str): root 노드
    """
    if root != ".":
        print(root, end="")  # parent
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right


def inorder(root):
    """inorder 중위 순회할 때 방문하는 순서를 출력하는 함수

    * 탐색 우선 순위: 왼쪽 자식 > 루트 > 오른쪽 자식

    Args:
        root (str): root 노드
    """
    if root != ".":
        inorder(tree[root][0])  # left
        print(root, end="")  # parent
        inorder(tree[root][1])  # right


def postorder(root):
    """postorder 후위 순회할 때 방문하는 순서를 출력하는 함수

    * 탐색 우선 순위: 왼쪽 자식 > 오른쪽 자식 > 루트

    Args:
        root (str): root 노드
    """
    if root != ".":
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end="")  # parent


nodes = int(input())
tree = {}
for _ in range(nodes):
    parent, left, right = input().strip().split()
    tree[parent] = [left, right]

preorder("A")
print()
inorder("A")
print()
postorder("A")
