class Node:
    """더블리 링크드 리스트의 노드 클래스"""

    def __init__(self, data):
        self.data = data  # 실제 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스
        self.prev = None  # 이전 노드에 대한 레퍼런스


class DoubleLinkedList:
    """더블리 링크드 리스트 클래스"""

    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)  # 새로운 데이터를 저장하는 노드

        # 링크드 리스트가 비어 있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:  # 링크드 리스트에 데이터가 이미 있는 경우
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        """링크드 리스트 가장 앞에 데이터를 추가시켜주는 메소드"""
        new_node = Node(data)

        # 노드가 없을 때
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:  # 노드가 이미 있을 때
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, previous_node, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        # tail 노드 다음에 삽입할 때
        if previous_node is self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:  # 노드 중간에 삽입할 때
            new_node.prev = previous_node
            new_node.next = previous_node.next
            previous_node.next.prev = new_node
            previous_node.next = new_node

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""

        # 리스트에 노드가 하나만 있는 경우
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None
        elif node_to_delete is self.head:  # head 노드를 지울 때
            self.head = self.head.next
            self.head.prev = None
        elif node_to_delete is self.tail:  # tail 노드를 지울 때
            self.tail = self.tail.prev
            self.tail.next = None
        else:  # 노드 사이에 있는 노드를 지울 때
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        # 삭제하는 노드의 데이터를 리턴
        return node_to_delete.data

    def find_node_at(self, index):
        """ 링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정 """
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

    def find_node_with_data(self, data):
        """링크드 리스트에서 탐색 연산 메소드. 단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수

        # 링크드 리스트 전체를 돈다
        while iterator is not None:
            # iterator 노드의 데이터가 찾는 데이터면 iterator를 리턴한다
            if iterator.data == data:
                return iterator
            iterator = iterator.next  # 다음 노드로 넘어간다

            # 링크드 리스트 안에 원하는 데이터가 없었기 때문에 None 리턴한다
            return None

    def __str__(self):
        """링크드  리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드  리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str


# 빈 링크드 리스트 정의
my_list = DoubleLinkedList()

# 링크드 리스트에 데이터 추가
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)
my_list.prepend(2)

print(my_list)

# 링크드 리스트 중간에 데이터 삽입
node_at_index_3 = my_list.find_node_at(3)  # 노드 접근
my_list.insert_after(node_at_index_3, 3)
print(my_list)

# 삽입했던 노드 삭제
node_at_index_4 = my_list.find_node_at(4)
print(my_list.delete(node_at_index_4))
print(my_list)