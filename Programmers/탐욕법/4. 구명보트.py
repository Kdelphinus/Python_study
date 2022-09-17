def solution(people, limit):
    answer = 0
    start = 0
    end = len(people) - 1
    people.sort()
    while start <= end:
        tmp = people[end]
        if tmp + people[start] <= limit:  # 최대 2명밖에 못 탐
            tmp += people[start]
            start += 1
        end -= 1
        answer += 1

    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 50, 80], 100))
