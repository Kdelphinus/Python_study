ans, string = "", input()
for s in string:
    if ord("A") <= ord(s) <= ord("Z"):
        ans += chr((ord(s) - ord("A") + 13) % 26 + ord("A"))
    elif ord("a") <= ord(s) <= ord("z"):
        ans += chr((ord(s) - ord("a") + 13) % 26 + ord("a"))
    else:
        ans += s
print(ans)
