"""2021 카카오 채용연계형 인턴십"""

# 링크드 리스트를 이용한 풀이
# https://kjhoon0330.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%91%9C-%ED%8E%B8%EC%A7%91-Python


def solution(n, k, cmd):
    now = k
    table = {i: [i - 1, i + 1] for i in range(n)}
    answer = ["O"] * n
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]
    stack = []
    for c in cmd:
        if c == "C":
            answer[now] = "X"
            prev, next = table[now]
            stack.append([prev, now, next])  # 삭제된 정보 저장

            if next == None:  # 다음이 없을 때
                now = table[now][0]
            else:  # 다음이 남아 있을 때
                now = table[now][1]

            if prev == None:  # 제거할 위치가 시작일 때
                table[next][0] = None
            elif next == None:  # 제거할 위치가 끝일 때
                table[prev][1] = None
            else:
                table[prev][1] = next
                table[next][0] = prev

        elif c == "Z":
            prev, cur, next = stack.pop()
            answer[cur] = "O"
            if prev == None:  # 복구할 것이 첫번째 것일때
                table[next][0] = cur
            elif next == None:  # 복구할 것이 마지막 일때
                table[prev][1] = cur
            else:
                table[next][0] = cur
                table[prev][1] = cur

        else:
            c1, c2 = c.split()
            c2 = int(c2)
            if c1 == "D":
                for _ in range(c2):
                    now = table[now][1]
            else:
                for _ in range(c2):
                    now = table[now][0]

    return "".join(answer)


########################################################################################
#
# def solution(n, k, cmd):
#     answer = ""
#
#     check = [1] * n
#     delete = []
#     now = k
#
#     for c in cmd:
#         try:
#             order, num = c.split()
#         except:
#             order = c
#         cnt = 0
#         num = int(num)
#
#         if order == "D":
#             cnt += sum(check[now + 1 : now + num + 1])
#             now += num
#             while cnt < num:
#                 if check[now] == 1:
#                     cnt += 1
#
#                 if cnt == num:
#                     break
#
#                 now += 1
#         elif order == "U":
#             cnt += sum(check[now - num : now])
#             now -= num
#             while cnt < num:
#                 if check[now] == 1:
#                     cnt += 1
#
#                 if cnt == num:
#                     break
#
#                 now -= 1
#         elif order == "C":
#             delete.append(now)
#             check[now] = 0
#             if sum(check[now + 1 :]) == 0:
#                 while check[now] == 0:
#                     now -= 1
#             else:
#                 while check[now] == 0:
#                     now += 1
#         elif order == "Z":
#             past = delete.pop()
#             check[past] = 1
#         else:
#             print("wrong order")
#
#     for c in check:
#         if c == 1:
#             answer += "O"
#         else:
#             answer += "X"
#
#     return answer
#
#
# # print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
# print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
