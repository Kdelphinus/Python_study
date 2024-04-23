"""
Generic type class
- 데이터 형식에 의존 하지 않고, 하나의 값이 여러 다른 데이터 타입들을 가질 수 있는 기술
- generic type은 mypy와 pyright 사이에서 호환되지 않는 것에 유의할 것
"""

from typing import Optional, TypeVar, Generic

# TypeVar({type name}, 허용 하는 타입들...)
T = TypeVar("T", int, float, str)
H = TypeVar("H", int, float, str)


# 생성 시, 타입을 받고 T은 객체마다 받은 타입으로 지정된다.
class Robot(Generic[T, H]):
    def __init__(self, arm: T, head: H):
        self.arm: T = arm
        self.head: H = head

    def decode(self):
        pass


robot1 = Robot[int, int](121341234, 212342134)
robot2 = Robot[str, int]("212341234", 312341234)
robot3 = Robot[float, str](31234.1234, "412341234")


# 상속 받을 때
class Siri(Generic[T, H], Robot[T, H]):
    pass


siri1 = Siri[int, int](1234, 1234)
siri2 = Siri[str, int]("1234", 1234)
siri3 = Siri[float, str](1234.1234, "1234")
