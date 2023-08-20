from collections import deque

def main_logic(seat_numbers, seq_one, seq_two):
    seat_matches = []
    rotations = 0

    while len(seat_matches) < 3 and rotations < 10:
        first_number = seq_one.popleft()
        second_number = seq_two.pop()

        sum_of_numbers = int(first_number) + int(second_number)
        current_character = chr(sum_of_numbers)
        seat_one = first_number + current_character
        seat_two = second_number + current_character

        if seat_one in seat_numbers:
            if seat_one in seat_matches:
                break
            seat_numbers.remove(seat_one)
            seat_matches.append(seat_one)
        elif seat_two in seat_numbers:
            if seat_two in seat_matches:
                break
            seat_numbers.remove(seat_two)
            seat_matches.append(seat_two)
        else:
            seq_one.append(first_number)
            seq_two.appendleft(second_number)

        rotations += 1
    print(f"Seat matches: {', '.join(seat_matches)}")
    return f"Rotations count: {rotations}"


seats_numbers = input().split(", ")
sequence_one = deque(input().split(", "))
sequence_two = deque(input().split(", "))
print(main_logic(seats_numbers, sequence_one, sequence_two))
