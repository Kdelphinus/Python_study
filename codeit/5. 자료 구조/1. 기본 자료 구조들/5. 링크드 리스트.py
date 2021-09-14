class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, data):
        self.data = data  # 실제 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스


class LinkedList:
    """링크드 리스트 클래스"""

    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        # 링크드 리스트가 비어 있으면 새로운 노드가 링크드 리스트의 처음이자 마지막 노드다
        if self.head is None:
            self.head = new_node
        # 링크드 리스트가 비어 있지 않으면
        else:
            self.tail.next = new_node  # 가장 마지막 노드 뒤에 새로운 노드를 추가하고

        self.tail = new_node  # 마지막 노드를 추가한 노드로 바꿔준다

    def prepend(self, data):
        """링크드 리스트의 가장 앞의 데이터 삽입"""
        new_node = Node(data)

        if self.head is None:  # 리스트가 비어있을 경우
            self.head = new_node
            self.tail = new_node
        else:  # 리스트가 비어있지 않을 경우
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, previous_node, data):
        """링크드 리스트 주어진 노드 뒤 삽입 연산 메소드"""
        new_node = Node(data)

        if previous_node is self.tail:  # 가장 마지막 순서 삽입
            self.tail.next = new_node
            self.tail = new_node
        else:  # 두 노드 사이에 삽입
            new_node.next = previous_node.next
            previous_node.next = new_node

    def pop_left(self):
        """링크드 리스트의 가장 앞의 데이터 삭제. 단, 링크드 리스트에 항상 노드가 있다고 가정"""
        data = self.head.data

        if self.head is self.tail:  # 리스트의 값이 하나 남았을 때
            self.head = None
            self.tail = None
        else:  # 리스트의 값이 두 개 이상 남았을 때
            self.head = self.head.next

        return data

    def delete_after(self, previous_node):
        """링크드 리스트 삭제 연산. 주어진 노드 뒤 노드를 삭제한다"""
        # 삭제하는 노드를 출력하는 것이 관습.
        data = previous_node.next.data

        if previous_node.next is self.tail:  # 마지막 노드를 지울 때
            previous_node.next = None
            self.tail = previous_node
        else:  # 두 노드 사이 노드를 지울 때
            previous_node.next = previous_node.next.next

        return data

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


# 새로운 링크드 리스트 생성
linked_list = LinkedList()

# 여러 데이터를 링크드 리스트 마지막에 추가
linked_list.append(2)
linked_list.append(4)
linked_list.append(5)
linked_list.append(7)
linked_list.append(11)

print(linked_list)

# 데이터 2를 갖는 노드 탐색
node_with_2 = linked_list.find_node_with_data(2)

if not node_with_2 is None:
    print(node_with_2.data)
else:
    print("2를 갖는 노드는 없습니다")

# 링크드 리스트 노드에 접근 (데이터 가지고 오기)
print(linked_list.find_node_at(3).data)  # 데이터 가져오기
linked_list.find_node_at(2).data = 5  # 데이터 바꾸기

print(linked_list)

# 인덱스 2에 있는 노드 접근 후, 인덱스 2 뒤에 6 삽입
node_2 = linked_list.find_node_at(2)
linked_list.insert_after(node_2, 6)

print(linked_list)

# head node는 생성과정에서 이미 지정
head_node = linked_list.head
linked_list.insert_after(head_node, 3)

print(linked_list)

# 리스트 맨 앞에 삽입
linked_list.prepend(1)

print(linked_list)

# 인덱스 1 뒤에 값을 삭제
node_1 = linked_list.find_node_at(1)
print(linked_list.delete_after(node_1))  # 삭제되는 값 출력

print(linked_list)