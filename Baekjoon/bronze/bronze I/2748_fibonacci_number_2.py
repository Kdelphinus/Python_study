num = int(input())
fibonacci = [0, 1]
for i in range(2, num + 1):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
print(fibonacci[-1])
