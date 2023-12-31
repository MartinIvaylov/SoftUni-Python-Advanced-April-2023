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


size = 6
matrix = []

for i in range(size):
    matrix.append(input().split())

position = list(map(int, input().strip("(").strip(")").split(", ")))


while True:
    command = input()

    if command == "Stop":
        break

    current_command = command.split(", ")
    position = move(current_command[1], position)

    if current_command[0] == "Create":
        value = current_command[2]
        if matrix[position[0]][position[1]] == ".":
            matrix[position[0]][position[1]] = value

    elif current_command[0] == "Update":
        value = current_command[2]
        if matrix[position[0]][position[1]] != ".":
            matrix[position[0]][position[1]] = value
    elif current_command[0] == "Delete":
        if matrix[position[0]][position[1]] != ".":
            matrix[position[0]][position[1]] = "."
    elif current_command[0] == "Read":
        if matrix[position[0]][position[1]] != ".":
            print(matrix[position[0]][position[1]])


for row in matrix:
    print(" ".join(row))