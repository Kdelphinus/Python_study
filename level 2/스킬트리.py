"""Summer/Winter Coding(~2018)"""


def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        idx = [27] * len(skill)  # 최대 길이가 26이므로
        for i in range(len(skill)):
            try:  # 찾는 스킬이 있다면 인덱스를 저장하고
                idx[i] = skill_tree.index(skill[i])
            except:  # 없다면 계속 진행
                continue
        if idx == sorted(idx):  # 스킬트리가 오름차순이라면 올바른 스킬트리
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))  # 2
print(solution("ADF", ["ERT", "ADF", "FDA", "DA", "F"]))  # 2

# -----------------------------------------------------------------------
"""다른 풀이"""


def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_list = list(skill)
        for s in skill_tree:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
