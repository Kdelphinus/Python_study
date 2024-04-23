from typing import Union


def foo(x: Union[int, str]) -> None:
    print(x)


xxx: Union[int, str] = 3

foo(xxx)

xxx = "17"

foo(xxx)
