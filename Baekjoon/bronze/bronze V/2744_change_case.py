string = input()
for s in string:
    if ord(s) <= 90:
        print(s.lower(), end="")
    else:
        print(s.upper(), end="")
