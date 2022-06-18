changyoung, sangdeok = 100, 100
num = int(input())
for _ in range(num):
    chang, sang = map(int, input().split())
    if chang > sang:
        sangdeok -= chang
    elif chang < sang:
        changyoung -= sang
print(changyoung)
print(sangdeok)
