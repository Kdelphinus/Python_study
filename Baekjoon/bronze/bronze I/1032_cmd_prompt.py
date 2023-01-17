n = int(input())
cmd = input()
for _ in range(n - 1):
    tmp = input()
    for i in range(len(cmd)):
        if cmd[i] != tmp[i]:
            cmd = cmd[:i] + "?" + cmd[i + 1 :]
print(cmd)
