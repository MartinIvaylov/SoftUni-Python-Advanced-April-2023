from collections import deque

def main_logic(mills_of_caffeine, energy_drinks):
    max_caffeine = 300
    total_caffeine = 0
    while mills_of_caffeine and energy_drinks:

        current_caffeine = mills_of_caffeine.pop()
        current_energy_drink = energy_drinks.popleft()

        caffeine_to_drink = int(current_caffeine) * int(current_energy_drink)
        total_caffeine += caffeine_to_drink
        if total_caffeine > max_caffeine:
            energy_drinks.append(current_energy_drink)
            total_caffeine -= caffeine_to_drink
            total_caffeine -= 30
            if total_caffeine < 0:
                total_caffeine = 0
        else:
            continue

    if energy_drinks:
        remaining_energy_drinks = [energy_drink for energy_drink in energy_drinks]

        print(f"Drinks left: {', '.join(map(str, remaining_energy_drinks))}")

    else:
        print("At least Stamat wasn't exceeding the maximum caffeine.")

    return f"Stamat is going to sleep with {total_caffeine} mg caffeine."


milligrams_of_caffeine = deque(map(int,input().split(", ")))
energy_drinks = deque(map(int,input().split(", ")))


print(main_logic(milligrams_of_caffeine, energy_drinks))
