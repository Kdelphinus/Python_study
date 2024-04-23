"""
optional type
- 있을 수도 있고 없을 수도 있는 값
"""

from typing import Optional

# Union[str, None] 과 동일
xxx: Optional[str] = "hello"

print(xxx)

xxx = None

print(xxx)
