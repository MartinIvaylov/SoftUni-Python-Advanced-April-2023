from collections import deque

chocolate_sequence = deque(int(x) for x in input().split(", "))
cups_of_milk_sequence = deque(int(x) for x in input().split(", "))

milkshakes = 0

while milkshakes != 5 and cups_of_milk_sequence and chocolate_sequence:
    chocolate = chocolate_sequence.pop()
    cup_of_milk = cups_of_milk_sequence.popleft()

    if chocolate <= 0 and cup_of_milk <= 0:
        continue
    elif chocolate <= 0:
        cups_of_milk_sequence.appendleft(cup_of_milk)
        continue
    elif cup_of_milk <= 0 :
        chocolate_sequence.append(chocolate)
        continue

    if chocolate == cup_of_milk:
        milkshakes += 1
    else:
        cups_of_milk_sequence.append(cup_of_milk)
        chocolate_sequence.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolate_sequence) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk_sequence) or 'empty'}")