"""1193 분수찾기"""

X = int(input())
start = 1
end = 2
a = []
for i in range(X):
    if X == 1:
        print("1/1")
    start += i + 1
    end += i + 2
    c = end - start - 1
    if X in range(start, end):
        for j in range(c + 1):
            b = str(j + 1)
            e = str((c - j + 1))
            if c % 2 != 0:
                s = f"{b}/{e}"
                a.append(s)
            else:
                s = f"{e}/{b}"
                a.append(s)
        d = X - start
        print(a[d])

# --------------------------------------------------------------------

"""모범답안"""

X = int(input())
line = 1
while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    a = X
    b = line - X + 1
else:
    a = line - X + 1
    b = X
print(a, "/", b, sep="")
