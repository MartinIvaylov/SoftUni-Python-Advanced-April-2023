from collections import deque

textile = deque(list(map(int, input().split(" "))))
medicaments = deque(list(map(int, input().split(" "))))

items = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100
}
created_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0
}

while textile and medicaments:

    current_textile = textile.popleft()
    current_medicament = medicaments.pop()

    current_sum = current_textile + current_medicament

    if current_sum == 30:
        created_items["Patch"] += 1
    elif current_sum == 40:
        created_items["Bandage"] += 1

    elif current_sum == 100:
        created_items["MedKit"] += 1

    elif current_sum > 100:
        created_items["MedKit"] += 1
        next_value_medicament = medicaments.pop()
        next_value_medicament += current_sum - 100
        medicaments.append(next_value_medicament)
    else:
        current_medicament += 10
        medicaments.append(current_medicament)


else:
    if not textile and not medicaments:
        print("Textiles and medicaments are both empty.")
    elif not textile:
        print("Textiles are empty.")
    elif not medicaments:
        print("Medicaments are empty.")




ordered_values = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))
for value in ordered_values:
    if value[1] > 0:
        print(f"{value[0]} - {value[1]}")


if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")

if textile:
    print(f"Textiles left: {', '.join(map(str, textile))}")



