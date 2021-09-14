def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    # 자식 노드가 더 이상 없을 경우 리턴
    if left_child_index >= len(tree):
        return

    # 자식 노드와 주어진 노드 중 최댓값을 가진 노드의 인덱스를 구함
    max_tree = max(tree[left_child_index], tree[right_child_index], tree[index])
    max_index = tree.index(max_tree)

    # 최대값을 가진 인덱스와 부모 노드의 인덱스가 다르면 위치 변경
    if max_index != index:
        swap(tree, max_index, index)
        heapify(tree, max_index, tree_size)  # 값을 바꿨기 때문에 max_index가 자식 인덱스


# 실행 코드
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
print(tree)
