def count_backstep(height_lst: list[int]) -> int:
    step = 0
    line = []

    for height in height_lst[1:]:
        if not line or max(line) < height:
            line.append(height)
            continue
        idx = 0
        while idx < len(line) and line[idx] < height:
            idx += 1
        step += len(line) - idx
        line = line[:idx] + [height] + line[idx:]

    return step


if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        print(f"{i + 1} {count_backstep(list(map(int, input().split())))}")
