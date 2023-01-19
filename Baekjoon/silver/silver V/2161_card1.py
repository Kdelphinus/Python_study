from collections import deque


def card1(n: int) -> None:
    cards = deque([i for i in range(1, n + 1)])

    while True:
        print(cards.popleft(), end=" ")

        if not cards:
            return

        tmp = cards.popleft()
        cards.append(tmp)


if __name__ == "__main__":
    num = int(input())
    card1(num)
