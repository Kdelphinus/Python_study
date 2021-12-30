size = int(input())
size_binary = format(size, "b")  # 이진수로 표현하여 문자열로 반환

print(size_binary.count("1"))  # 1이 있는 곳이 분열을 해서 몸집을 키울 때
for i in range(len(size_binary) - 1, -1, -1):
    if size_binary[i] == "1":
        print(len(size_binary) - i - 1, end=" ")

