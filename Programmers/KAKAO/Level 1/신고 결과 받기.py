from collections import defaultdict


def solution(id_list, report, k):
    report = list(set(report))
    check_cnt = defaultdict(int)
    check_victim = defaultdict(set)

    for users in report:
        victim, attacker = users.split()
        check_cnt[attacker] += 1
        check_victim[victim].add(attacker)

    reporter = []
    for id, cnt in check_cnt.items():
        if cnt >= k and id not in reporter:
            reporter.append(id)

    answer = []
    for id in id_list:
        cnt = 0
        for attacker in check_victim[id]:
            if attacker in reporter:
                cnt += 1
        answer.append(cnt)

    return answer


#################################################################################
"""다른 사람 풀이"""


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}

    # 신고 당한 횟수 세기
    for r in set(report):
        reports[r.split()[1]] += 1

    # 신고가 확정 되면 결과 통보 횟수 추가
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
