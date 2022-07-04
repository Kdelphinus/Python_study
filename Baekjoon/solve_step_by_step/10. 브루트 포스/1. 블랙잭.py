"""2798 블랙잭"""

# # num: 카드의 개수, max: 목표 합
# num, limit = map(int, input().split())
#
# # 내가 가진 카드
# card = list(map(int, input().split()))
#
# # 합의 초기값
# sum = 0
#
# for i in range(len(card) - 2):
#     for j in range(i + 1, len(card) - 1):
#         for k in range(j + 1, len(card)):
#             if i < j and j < k:
#                 if card[i] + card[j] + card[k] <= limit:
#                     sum = max(card[i] + card[j] + card[k], sum)
# print(sum)

##############################################################################

"""2022/07/04 때 간단하게 수정"""


def blackjack(card: list, num: int, limit: int):
    sum = 0
    for i in range(num - 2):
        for j in range(i + 1, num - 1):
            for k in range(j + 1, num):
                if card[i] + card[j] + card[k] < limit:
                    sum = max(card[i] + card[j] + card[k], sum)
                elif card[i] + card[j] + card[k] == limit:
                    return limit
    return sum


# num: 카드의 개수, max: 목표 합
num, limit = map(int, input().split())

# 내가 가진 카드
card = list(map(int, input().split()))

# 합의 초기값
sum = 0
print(blackjack(card, num, limit))
