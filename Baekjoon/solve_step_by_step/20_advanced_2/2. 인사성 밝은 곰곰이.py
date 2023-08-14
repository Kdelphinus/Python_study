"""25192 인사성 밝은 곰곰이"""
import sys

INPUT = sys.stdin.readline

ans, N = 0, int(INPUT())
member = set()
for _ in range(N):
    name = INPUT().strip()
    if name == "ENTER":
        ans += len(member)
        member.clear()
    else:
        member.add(name)
ans += len(member)
print(ans)
