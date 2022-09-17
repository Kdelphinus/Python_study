cnt = 0
stack = []
iron_rod = input()
for idx, i in enumerate(iron_rod):
    # 여는 괄호는 일단 집어넣는다.
    if i == "(":
        stack.append(i)
        # 레이저가 아니면 쇠막대기 개수 추가
        if iron_rod[idx + 1] != ")" and idx < len(iron_rod) - 1:
            cnt += 1
    # 닫는 괄호면 일단 뺀다.
    else:
        stack.pop()
        # 레이저일 경우, 절단된 막대기 수만큼 추가
        if idx > 0 and iron_rod[idx - 1] == "(":
            cnt += len(stack)
print(cnt)
