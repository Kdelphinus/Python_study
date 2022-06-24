n = int(input())
remain = 0
for _ in range(n):
    student, apple = map(int, input().split())
    remain += apple % student
print(remain)
