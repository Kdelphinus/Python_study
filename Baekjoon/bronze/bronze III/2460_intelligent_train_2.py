train = 0
max_people = 0
for _ in range(10):
    out_n, in_n = map(int, input().split())
    train -= out_n
    train += in_n
    max_people = max(max_people, train)
print(max_people)
