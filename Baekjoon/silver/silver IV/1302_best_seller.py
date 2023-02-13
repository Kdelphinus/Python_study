from collections import defaultdict


books = defaultdict(int)
for _ in range(int(input())):
    books[input()] += 1
print(sorted(books.items(), key=lambda x: (-x[1], x[0]))[0][0])
