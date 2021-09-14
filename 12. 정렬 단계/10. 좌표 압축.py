"""18870 좌표 압축"""

# 받을 숫자의 개수
n = int(input())

# 숫자를 리스트의 저장
x = list(map(int, input().split()))

# 리스트 안 중복을 제거하고 오름차순으로 정렬
xt = list(sorted(set(x)))

# 작은 것부터 차례대로 원래 값을 key, 압축된 좌표를 value로 딕셔너리에 저장
xt = {xt[i]: i for i in range(len(xt))}

# 원래 리스트의 값을 딕셔너리 key로 넣어서 value를 출력
# 이때 *을 붙이면 띄어쓰기 형식으로, 안 붙이면 리스트로 출력됨
print(*[xt[i] for i in x])
