from typing import Optional


class Hello:
    def world(self) -> str:
        return "Hello, world!"


class World:
    pass


# class type
# ""로 묶어도 안 묶은 것과 동일하다.
hello: Hello = Hello()
world: "World" = World()


def foo(ins: Hello) -> str:
    return ins.world()


print(foo(hello))


# 아래와 같이 Node가 선언되지 않았는데 자기 자신을 typing 해야 한다면 ""로 묶어서 선언하면 된다.
class Node:
    def __init__(self, data: int, node: Optional["Node"] = None):
        self.data = data
        self.node = node


node2 = Node(27)
node1 = Node(12, node2)
node0 = Node(30, node1)
