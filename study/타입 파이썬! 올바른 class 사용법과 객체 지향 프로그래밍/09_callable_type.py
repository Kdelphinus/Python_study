from typing import Callable


def add(a: int, b: int) -> None:
    print(a + b)


# Callable[{parameter type}, {return type}]으로 선언 하면 됨
def foo(func: Callable[[int, int], None]) -> None:
    func(2, 3)


foo(add)
