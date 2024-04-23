"""
객체 내에 있는 변수들은 __dict__에 저장되어 있다.
__slots__를 사용하면 __dict__를 사용하지 않아 메모리를 절약할 수 있다.

그러나 무작정 slot을 사용 하는 것은 좋지 않다.
"""

import timeit


class WithoutSlotClass:
    def __init__(self, name, email):
        self.name = name
        self.email = email


wos = WithoutSlotClass("a", "b")
print(wos.__dict__)  # {'name': 'a', 'email': 'b'}
wos.__dict__["hello"] = "world"
print(wos.__dict__)  # {'name': 'a', 'email': 'b', 'hello': 'world'}


class WithSlotClass:
    __slots__ = ["name", "email"]

    def __init__(self, name, email):
        self.name = name
        self.email = email


ws = WithSlotClass("a", "b")
# print(ws.__dict__)  # AttributeError: 'WithSlotClass' object has no attribute '__dict__'
# ws.__dict__["hello"] = "world"  # AttributeError: 'WithSlotClass' object has
# no attribute '__dict__'
print(ws.__slots__)  # ['name', 'email']


# 메모리 사용량 비교


def repeat(obj):
    def inner():
        obj.name = "a"
        obj.email = "b"
        del obj.name
        del obj.email

    return inner


no_slot_time = timeit.repeat(repeat(wos), number=1000000)
use_slot_time = timeit.repeat(repeat(ws), number=1000000)

print("no slot: ", min(no_slot_time))  # no slot:  0.2708...
print("use slot: ", min(use_slot_time))  # use slot:  0.1247...
