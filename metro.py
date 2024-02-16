N = int(input())

passengers = []

for _ in range(N):
    entry, exit = map(int, input().split())
    passengers.append((entry, exit))

T = int(input())

passengers_at_T = 0

for entry, exit in passengers:
    if entry <= T <= exit:
        passengers_at_T += 1

print(passengers_at_T)
