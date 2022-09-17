class Node:
    """이진 탐색 트리 노드 클래스"""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None