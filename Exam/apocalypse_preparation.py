from collections import deque

textiles = deque(map(int, input().split()))
medicaments = list(map(int, input().split()))

healing_items = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100
}

healing_items_created = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0
}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()

    sum_of_both = current_textile + current_medicament

    if sum_of_both == healing_items["Patch"]:
        healing_items_created["Patch"] += 1

    elif sum_of_both == healing_items["Bandage"]:
        healing_items_created["Bandage"] += 1

    elif sum_of_both >= healing_items["MedKit"]:
        healing_items_created["MedKit"] += 1
        if sum_of_both > healing_items["MedKit"]:
            plus_sum = sum_of_both - 100
            some_medicament = medicaments.pop()
            some_medicament += plus_sum
            medicaments.append(some_medicament)


    else:
        current_medicament += 10
        medicaments.append(current_medicament)
else:
    if not textiles and not medicaments:
        print("Textiles and medicaments are both empty.")
    elif not textiles:
        print("Textiles are empty.")
    elif not medicaments:
        print("Medicaments are empty.")

if healing_items_created:
    output = ""


    sorted_items = sorted(healing_items_created.items(), key=lambda x: (-x[1], x[0]))
    for item in sorted_items:
        if int(item[1]) > 0:
            print(f"{item[0]} - {item[1]}")

if textiles:

    print(f"Textiles left: {', '.join(map(str, textiles))}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")



# from collections import deque
#
# textiles = deque(map(int, input().split()))
# medicaments = list(map(int, input().split()))
#
# items = {"Patch": 0, "Bandage": 0, "MedKit": 0}
#
# while True:
#     if not textiles and not medicaments:
#         print("Textiles and medicaments are both empty.")
#         break
#     if not textiles:
#         print("Textiles are empty.")
#         break
#     if not medicaments:
#         print("Medicaments are empty.")
#         break
#     first_textile = textiles.popleft()
#     last_medicament = medicaments.pop()
#     summed_items = first_textile + last_medicament
#     if summed_items == 30:
#         items["Patch"] += 1
#     elif summed_items == 40:
#         items["Bandage"] += 1
#     elif summed_items == 100:
#         items["MedKit"] += 1
#     elif summed_items > 100:
#         items["MedKit"] += 1
#         summed_items -= 100
#         medicaments[-1] += summed_items
#     else:
#         last_medicament += 10
#         medicaments.append(last_medicament)
#
# sorted_items = sorted(items.items(), key=lambda x: (-x[1], x[0]))
# for item in sorted_items:
#     if int(item[1]) > 0:
#         print(f"{item[0]} - {item[1]}")
#
# if medicaments:
#     medicaments.reverse()
#     print(f"Medicaments left: {', '.join(map(str, medicaments))}")
# if textiles:
#     print(f"Textiles left: {', '.join(map(str, textiles))}")