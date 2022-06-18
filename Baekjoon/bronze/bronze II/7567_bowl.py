bowls = input()
curr = ""
height = 0
for bowl in bowls:
    if bowl == curr:
        height += 5
    else:
        height += 10
        curr = bowl
print(height)
