class Node:
    """이진 탐색 트리 노드 클래스"""

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.right_child = None
        self.left_child = None


def print_inorder(node):
    """주어진 노드를 in-order로 출력해주는 함수"""
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)


class BinarySearchTree:
    """이진 탐색 트리 클래스"""

    def __init__(self):
        self.root = None

    def delete(self, data):
        """이진 탐색 트리 삭제 메소드"""
        node_to_delete = self.search(data)  # 삭제할 노드를 가지고 온다
        parent_node = node_to_delete.parent  # 삭제할 노드의 부모 노드

        # 경우 1: 지우려는 노드가 leaf 노드일 때
        if node_to_delete.left_child is None and node_to_delete.right_child is None:
            if self.root is node_to_delete:
                self.root = None
            else:  # 일반적인 경우
                if node_to_delete is parent_node.left_child:
                    parent_node.left_child = None
                else:
                    parent_node.right_child = None

        # 경우 2: 지우려는 노드가 자식이 하나인 노드일 때
        elif node_to_delete.right_child is None:  # 지우려는 노드가 오른쪽 자식만 있을 때
            if self.root is node_to_delete:
                self.root = node_to_delete.left_child
                self.root.parent = None
            elif parent_node.left_child is node_to_delete:
                parent_node.left_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node
            else:
                parent_node.right_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node
        elif node_to_delete.left_child is None:  # 지우려는 노드가 왼쪽 자식만 있을 때
            if self.root is node_to_delete:
                self.root = node_to_delete.right_child
                self.root.parent = None
            elif parent_node.left_child is node_to_delete:
                parent_node.left_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node
            else:
                parent_node.right_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node

        # 경우 3: 지우려는 노드가 2개의 자식이 있을 때
        else:
            successor = self.find_min(node_to_delete.right_child)
            node_to_delete.data = successor.data
            parent_node = successor.parent

            # successor가 leaf 노드일 때
            if successor.right_child is None:  # successor은 무조건 왼쪽 자식일 수밖에 없다
                parent_node.left_child = None
            else:  # successor가 오른쪽 자식 노드를 가지고 있을 때
                parent_node.right_child = successor.right_child
                successor.right_child = parent_node

    @staticmethod
    def find_min(node):
        """(부분)이진 탐색 트리의 가장 작은 노드 리턴"""
        guide_node = node

        while guide_node.left_child is not None:
            guide_node = guide_node.left_child
        return guide_node

    def search(self, data):
        """이진 탐색 트리 탐색 메소드, 찾는 데이터를 갖는 노드가 없으면 None을 리턴한다"""
        guide_node = self.root

        # 원하는 데이터를 갖는 노드를 찾을 때까지 돈다
        while guide_node is not None:
            # 원하는 데이터를 갖는 노드를 찾으면 리턴
            if data == guide_node.data:
                return guide_node
            # 원하는 데이터가 노드의 데이터보다 크면 오른쪽 자식 노드로 간다
            if data > guide_node.data:
                guide_node = guide_node.right_child
            # 원하는 데이터가 노드의 데이터보다 작으면 왼쪽 자식 노드로 간다
            else:
                guide_node = guide_node.left_child

        return None  # 원하는 데이터가 트리에 없으면 None 리턴

    def insert(self, data):
        new_node = Node(data)  # 삽입할 데이터를 갖는 새 노드 생성

        # 트리가 비었으면 새로운 노드를 root 노드로 만든다
        if self.root is None:
            self.root = new_node
            return

        # 첫 비교 대상은 root 노드
        guide_node = self.root

        # 데이터를 비교하며 새로운 노드를 저장할 위치를 찾는다
        while True:
            if new_node.data > guide_node.data:  # 비교 대상보다 새로운 노드의 데이터가 클 때
                if guide_node.right_child is None:  # 자식 노드가 더 이상 없으먄
                    new_node.parent = guide_node
                    guide_node.right_child = new_node
                    return
                guide_node = guide_node.right_child
            else:
                if guide_node.left_child is None:  # 비교 대상보다 새로운 노드의 데이터가 작을 때
                    new_node.parent = guide_node  # 자식 노드가 더 이상 없으면
                    guide_node.left_child = new_node
                    return
                guide_node = guide_node.left_child

    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        print_inorder(self.root)  # root 노드를 in-order로 출력한다


# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 이진 탐색 트리 출력
print("이진 탐색 트리 출력")
bst.print_sorted_tree()
print()

# 노드 탐색과 출력
print("노드 탐색과 출력")
print(bst.search(7).data)
print(bst.search(19).data)
print(bst.search(2).data)
print(bst.search(20))
print()

print("find_min")
print(bst.find_min(bst.root).data)  # 전체 이진 탐색 트리에서 가장 작은 노드
print(bst.find_min(bst.root.right_child).data)  # root 노드의 오른쪽 부분 트리에서 가장 작은 노드
print()

# leaf 노드 삭제
print("leaf 노드 삭제")
bst.delete(2)
bst.delete(4)

bst.print_sorted_tree()
print()

# 자식이 하나만 있는 노드 삭제
print("자식이 하나만 있는 노드 삭제")
bst.delete(5)
bst.delete(9)

bst.print_sorted_tree()
print()

# 자식이 두 개 다 있는 노드 삭제
print("자식이 두 개 다 있는 노드 삭제")
bst.delete(7)
bst.delete(11)

bst.print_sorted_tree()