A, B, C = map(int, input().split())
if A == B and B != C:
    print("C")
elif A != B and B == C:
    print("A")
elif A == C and A != B:
    print("B")
else:
    print("*")
