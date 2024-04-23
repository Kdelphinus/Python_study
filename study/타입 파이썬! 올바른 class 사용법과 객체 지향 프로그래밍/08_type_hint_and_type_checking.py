"""
1. python에 내장되어 있는 type hint
2. mypy
3. pyright
"""

from typing import List, Tuple, Dict

int_var: int = 88
str_var: str = "hello"
float_var: float = 3.14
bool_var: bool = True

list_var: List[int] = [1, 2, 3]
tuple_var: Tuple[int, int, int] = (1, 2, 3)
dict_var: Dict[str, int] = {"a": 1, "b": 2, "c": 3}


def type_check(obj, typer) -> None:
    if not isinstance(obj, typer):
        raise TypeError(f"type error: {typer}")


# isinstance(obj, class) 함수를 사용하여 타입 체크
def cal_add(a: int, b: int) -> int:
    type_check(a, int)
    type_check(b, int)
    return a + b


print(cal_add(1, 2))
# print(cal_add(1, "2"))
