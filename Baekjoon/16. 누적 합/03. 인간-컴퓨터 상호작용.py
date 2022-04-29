"""16139 인간-컴퓨터 상호작용"""
# count로 풀면 50점
import sys
from string import ascii_lowercase  # 영어 소문자 리스트

input = sys.stdin.readline
alphabet = {}
for idx, a in enumerate(ascii_lowercase):
    alphabet[a] = idx

string = input()
prefix_sum = [[0] * len(ascii_lowercase)]
for idx, s in enumerate(string):
    if s not in ascii_lowercase:  # 공백이 들어간 것이 있음
        continue

    # 각 철자 순서마다 전체 알파벳에 대하여 누적합
    tmp = prefix_sum[-1][:]
    prefix_sum.append(tmp)
    prefix_sum[-1][alphabet[s]] += 1

cnt = int(input())
for _ in range(cnt):
    alpha, start, end = input().split()
    idx = alphabet[alpha]
    print(prefix_sum[int(end) + 1][idx] - prefix_sum[int(start)][idx])
