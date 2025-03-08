n, game = input().split()
participant = set()
for _ in range(int(n)):
    participant.add(input())

player_num = 0
if game == "Y":
    player_num = 2
elif game == "F":
    player_num = 3
elif game == "O":
    player_num = 4

print(len(participant) // (player_num - 1))
