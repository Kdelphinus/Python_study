# 해답: https://eda-ai-lab.tistory.com/465


def solution(number, k):
    stack = [number[0]]  # 첫 숫자를 스택에 삽입
    for num in number[1:]:
        # 들어오는 값이 stack 안에 값보다 크면 제거
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)  # 새로운 값 추가

    if k != 0:  # 다 제거하지 못했으면
        stack = stack[:-k]  # 뒤에서부터 자름

    return "".join(stack)
