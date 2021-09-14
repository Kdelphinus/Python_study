"""연습문제"""


def solution(s):
    return " ".join([word.capitalize() for word in s.split(" ")])


print(solution("3Peple unFollwed me"))  # 3peple Unfollwed Me
print(solution("for the last week"))  # For The Last Week
print(solution("a b  c   d    e"))  # A B  C   D    E
