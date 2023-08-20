
n = int(input())
directions = input().split(', ')
field = [input().strip() for _ in range(n)]



def main_logic(size_of_matrix, current_directions, matrix):
    squirrel_pos = None
    hazelnut_count = 0

    for i in range(size_of_matrix):
        for j in range(size_of_matrix):
            if matrix[i][j] == 's':
                squirrel_pos = (i, j)
                break

    for direction in current_directions:
        if direction == 'left':
            squirrel_pos = (squirrel_pos[0], squirrel_pos[1] - 1)
        elif direction == 'right':
            squirrel_pos = (squirrel_pos[0], squirrel_pos[1] + 1)
        elif direction == 'up':
            squirrel_pos = (squirrel_pos[0] - 1, squirrel_pos[1])
        elif direction == 'down':
            squirrel_pos = (squirrel_pos[0] + 1, squirrel_pos[1])

        if squirrel_pos[0] < 0 or squirrel_pos[0] >= size_of_matrix or squirrel_pos[1] < 0 or squirrel_pos[1] >= size_of_matrix:
            return f"The squirrel is out of the field.\nHazelnuts collected: {hazelnut_count}"

        cell = matrix[squirrel_pos[0]][squirrel_pos[1]]

        if cell == 'h':
            hazelnut_count += 1
            matrix[squirrel_pos[0]] = matrix[squirrel_pos[0]][:squirrel_pos[1]] + '*' + \
                                      matrix[squirrel_pos[0]][squirrel_pos[1] + 1:]




    if hazelnut_count == 3:
        return f"Good job! You have collected all hazelnuts!\nHazelnuts collected: {hazelnut_count}"
    elif cell == 't':
        return f"Unfortunately, the squirrel stepped on a trap...\nHazelnuts collected: {hazelnut_count}"
    else:
        return f"There are more hazelnuts to collect.\nHazelnuts collected: {hazelnut_count}"

print(main_logic(n, directions, field))