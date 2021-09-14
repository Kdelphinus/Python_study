class Node:
    """이진 트리 노드 클래스"""

    def __init__(self, data):
        """데이터와 두 자식 노드에 대한 레퍼런스를 갖는다"""
        self.data = data
        self.left_child = None
        self.right_child = None


# root 노드 생성
root_node = Node("A")

# 자식 노드들 생성
node_2 = Node("B")
node_3 = Node("C")
node_4 = Node("D")
node_5 = Node("E")
node_6 = Node("F")
node_7 = Node("G")
node_8 = Node("H")

# 자식 노드 지정
root_node.left_child = node_2
root_node.right_child = node_3
node_2.left_child = node_4
node_2.right_child = node_5
node_3.right_child = node_6
node_5.left_child = node_7
node_5.right_child = node_8

# 실행 코드
test_node = root_node.right_child.right_child
print(test_node.data)

test_node = root_node.left_child.right_child.left_child
print(test_node.data)

test_node = root_node.left_child.right_child.right_child
print(test_node.data)