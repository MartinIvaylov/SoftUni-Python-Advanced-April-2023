def move(direction_, position_):
    if direction_ == 'up':
        position_[0] -= 1
    elif direction_ == 'down':
        position_[0] += 1
    elif direction_ == 'left':
        position_[1] -= 1
    elif direction_ == 'right':
        position_[1] += 1
    return position_



row, column = map(int, input().split())


matrix = []
for _ in range(row):
    line = input().split()

    if "B" in line:
        player_pos = [column, line.index("B")]

    matrix.append(line)

touched_opponents = 0
moves = 0

while True:
    command = input()

    if command == "Finish" or touched_opponents == 3:

        break

    else:

        position = move(command, player_pos)


        if command == "up":
            if matrix[position[0]][position[1]] == "-":
                matrix[position[0]][position[1]] = "B"
                moves += 1
                position = matrix[position[0]][position[1]]
            elif matrix[position[0]][position[1]] == "O":
                continue
            elif matrix[position[0]][position[1]] == "P":
                matrix[position[0]][position[1]] = "-"
                touched_opponents += 1
                position = matrix[position[0]][position[1]]

                moves += 1
        elif command == "down":
            if matrix[position[0]][position[1]] == "-":
                matrix[position[0]][position[1]] = "B"
                position = matrix[position[0]][position[1]]
                moves += 1
            elif matrix[position[0]][position[1]] == "O":
                continue
            elif matrix[position[0]][position[1]] == "P":
                matrix[position[0]][position[1]] = "-"
                touched_opponents += 1
                position = matrix[position[0]][position[1]]

                moves += 1
        elif command == "right":
            if matrix[position[0]][position[1]] == "-":
                matrix[position[0]][position[1]] = "B"
                moves += 1
                position = matrix[position[0]][position[1]]
            elif matrix[position[0]][position[1]] == "O":
                    continue
            elif matrix[position[0]][position[1]] == "P":
                matrix[position[0]][position[1]] = "-"
                touched_opponents += 1
                position = matrix[position[0]][position[1]]

                moves += 1
        elif command == "left":
            if matrix[position[0]][position[1]] == "-":
                matrix[position[0]][position[1]] = "B"
                moves += 1
                position = matrix[position[0]][position[1]]
            elif matrix[position[0]][position[1]] == "O":
                continue
            elif matrix[position[0]][position[1]] == "P":
                matrix[position[0]][position[1]] = "-"
                touched_opponents += 1
                position = matrix[position[0]][position[1]]

                moves += 1



print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves}")

# def find_my_cooridnates(r, c, mtrx):
#     for row in range(r):
#         for col in range(c):
#             if mtrx[row][col] == "B":
#                 return [row, col]
#
# def check_my_next_position(my_row, my_col, current_matrix):
#     if 0 <= my_row < len(current_matrix) and 0 <= my_col < len(current_matrix[0]):
#         next_position = current_matrix[my_row][my_col]
#         if next_position == "O":
#             return False
#         elif next_position == "-":
#             return [my_row, my_col], current_matrix, 0
#         elif next_position == "P":
#             current_matrix[my_row][my_col] = "-"
#             return [my_row, my_col], current_matrix, 1
#
#
# n, m = map(int, input().split())
#
# matrix = []
# for _ in range(n):
#     matrix.append(input().split())
#
#
# my_coordinates = find_my_cooridnates(n, m, matrix)
# matrix[my_coordinates[0]][my_coordinates[1]] = "-"
# result = False
# touched_opponents = 0
# moves_made = 0
#
# while True:
#     if touched_opponents == 3:
#         break
#
#     command = input()
#     if command == 'Finish':
#         break
#
#     if command == 'up':
#         result = check_my_next_position(my_coordinates[0] - 1, my_coordinates[1], matrix)
#     elif command == 'down':
#         result = check_my_next_position(my_coordinates[0] + 1, my_coordinates[1], matrix)
#     elif command == 'left':
#         result = check_my_next_position(my_coordinates[0], my_coordinates[1] - 1, matrix)
#     elif command == 'right':
#         result = check_my_next_position(my_coordinates[0], my_coordinates[1] + 1, matrix)
#
#     if result:
#         my_coordinates, matrix, touches = result
#         touched_opponents += touches
#         moves_made += 1
#
# print("Game over!")
# print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")
