student = set(i for i in range(1, 31))
for _ in range(28):
    n = int(input())
    student.discard(n)
student = list(student)
print(f"{student[0]}\n{student[1]}")
