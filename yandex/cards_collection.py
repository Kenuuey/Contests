import sys

n = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().split()))

pos = {}

for i, card in enumerate(cards):
    if card not in pos:
        pos[card] = []
    pos[card].append(i)

min_deletions = float('inf')

for indexes in pos.values():
    if len(indexes) > 1:
        for j in range(len(indexes) - 1):
            min_deletions = min(min_deletions, indexes[j + 1] - indexes[j] - 1)

print(min_deletions if min_deletions != float('inf') else -1)