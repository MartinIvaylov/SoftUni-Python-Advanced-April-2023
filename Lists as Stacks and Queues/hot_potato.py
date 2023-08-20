from _collections import deque

kids_names = input().split()
step_of_hot_potato = int(input())

players_deque = deque(kids_names)
counter = 0

while len(players_deque) > 1:
    counter += 1
    current_name = players_deque.popleft()

    if counter == step_of_hot_potato:
        print(f"Removed {current_name}")
        counter = 0
    else:
        players_deque.append(current_name)

print(f"Last is {players_deque[0]}")

