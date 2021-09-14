"""2021 KAKAO BLIND RECRUITMENT"""
from itertools import combinations
from collections import Counter


def solution(orders, course):
    """solution 각 손님들에게 받은 메뉴를 사용하여 가장 많이 주문된 코스 요리를 만드는 함수

    Args:
        orders (list): 주문한 메뉴들이 들어있는 리스트
        course (list): 코스별로 들어가야 할 메뉴의 수가 담긴 리스트

    Returns:
        answer (list): 가장 많이 주문된 메뉴들로 만들어진 코스 메뉴들
    """
    answer = []
    for i in course:  # 요리 개수 별로 코스를 만듬
        menu = []
        for order in orders:  # 손님별로 주문한 메뉴를 받음
            order = list(order.strip())  # 각각의 메뉴로 나눠서 리스트로 저장
            order.sort()  # 조합에서 다른 조합이 나오지 않도록 정렬을 먼저함(xy, yx로 만들어지지 않도록)
            menu += list(map("".join, combinations(order, i)))  # 메뉴 가짓수만큼 조합을 만들어 저장
        menu_cnt = Counter(menu).most_common()  # 각각의 조합이 얼마나 있는지 리스트로 만듬

        if (
            len(menu_cnt) >= 1 and menu_cnt[0][1] > 1
        ):  # 하나의 메뉴라도 만들어졌고 주문한 사람이 두 명 이상일 때
            max_num = menu_cnt[0][1]  # 가장 많이 주문된 코스 요리의 주문 횟수를 저장하고
            answer.append(menu_cnt[0][0])  # 코스 요리를 추가
            for i in range(1, len(menu_cnt)):  # 만약 동률인 메뉴가 있다면 그것들도 추가
                if menu_cnt[i][1] < max_num:
                    break
                answer.append(menu_cnt[i][0])

    answer.sort()  # 메뉴를 이름순으로 정렬
    return answer


# ---------------------------------------------------------------------------------------------------------------------
"""방법은 동일, 구현은 더 간단"""


def simple(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)

        most_ordered = Counter(order_combinations).most_common()
        result += [
            menu
            for menu, order_num in most_ordered
            if order_num > 1 and order_num == most_ordered[0][1]
        ]
    # print(result)
    return ["".join(menu) for menu in sorted(result)]


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print("나의 답: ", solution(orders, course))
print("모범답안: ", simple(orders, course))
