i, string = 10, input()
while i < len(string):
    print(string[i - 10 : i])
    i += 10
print(string[i - 10 :])
