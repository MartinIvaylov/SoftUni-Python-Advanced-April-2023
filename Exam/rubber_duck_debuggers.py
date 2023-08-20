from collections import deque


time_needed = deque(list(map(int, input().split())))
number_of_tasks = deque(list(map(int, input().split())))

rubber_ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}



while time_needed and number_of_tasks:
    current_time = time_needed.popleft()
    current_number_of_tasks = number_of_tasks.pop()

    sum_of_numbers = current_time * current_number_of_tasks

    if sum_of_numbers <= 60:
        rubber_ducks["Darth Vader Ducky"] += 1
    elif 60 < sum_of_numbers <= 120:
        rubber_ducks["Thor Ducky"] += 1
    elif 120 < sum_of_numbers <= 180:
        rubber_ducks["Big Blue Rubber Ducky"] += 1
    elif 180 < sum_of_numbers <= 240:
        rubber_ducks["Small Yellow Rubber Ducky"] += 1
    elif sum_of_numbers > 240:
        current_number_of_tasks -= 2
        number_of_tasks.append(current_number_of_tasks)
        time_needed.append(current_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for k, v in rubber_ducks.items():
    print(f"{k}: {v}")