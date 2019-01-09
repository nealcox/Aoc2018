from collections import defaultdict
from collections import deque

NUM_PLAYERS = 9
NUM_MARBLES = 26

NUM_PLAYERS = 430
NUM_MARBLES = 71588

d = deque()
d.append(0)
current = 0
playernum = -1
scores = defaultdict(int)

for marble in range(1,NUM_MARBLES):
    playernum = ((playernum +1) % NUM_PLAYERS) 
    if marble % 23 != 0:
        d.rotate(-1)
        d.append(marble)
    else:
        d.rotate(7)
        removed = d.pop()
        d.rotate(-1)
        scores[playernum+1] += marble + removed
#    print(f"{playernum +1}\t {d}")

print(scores)
print(max(scores.values()))
