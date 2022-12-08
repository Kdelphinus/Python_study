alphabet = [0 for _ in range(26)]
for s in input():
    alphabet[ord(s) - ord("a")] += 1
print(*alphabet)
