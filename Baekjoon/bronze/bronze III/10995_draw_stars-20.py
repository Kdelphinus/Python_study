n = int(input())
odd, even = "* ", " *"
for i in range(n):
    print(even * n if i % 2 else odd * n)
