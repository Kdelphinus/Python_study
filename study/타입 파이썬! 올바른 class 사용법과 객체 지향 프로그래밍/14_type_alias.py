from typing import Union, List, Tuple, Optional, Dict
from typing_extensions import TypedDict


# type alias
Value = Union[
    int, bool, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, float]]
]


def cal(v: Value) -> Value:
    return v


# dict alias
class Point(TypedDict):
    x: int
    y: float
    z: str


# key에 따라서 value type을 지정 한다.
point: Point = {"x": 1, "y": 2.0, "z": "3"}
