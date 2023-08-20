def parse_input():
    n = int(input())
    directions = input().split(', ')
    field = [input().strip() for _ in range(n)]
    return n, directions, field


def simulate_game(n, directions, field):
    squirrel_pos = None
    hazelnut_count = 0

    for i in range(n):
        for j in range(n):
            if field[i][j] == 's':
                squirrel_pos = (i, j)
                break

    for direction in directions:
        if direction == 'left':
            squirrel_pos = (squirrel_pos[0], squirrel_pos[1] - 1)
        elif direction == 'right':
            squirrel_pos = (squirrel_pos[0], squirrel_pos[1] + 1)
        elif direction == 'up':
            squirrel_pos = (squirrel_pos[0] - 1, squirrel_pos[1])
        elif direction == 'down':
            squirrel_pos = (squirrel_pos[0] + 1, squirrel_pos[1])

        if squirrel_pos[0] < 0 or squirrel_pos[0] >= n or squirrel_pos[1] < 0 or squirrel_pos[1] >= n:
            return "The squirrel is out of the field.\nHazelnuts collected: {}".format(hazelnut_count)

        cell = field[squirrel_pos[0]][squirrel_pos[1]]

        if cell == 'h':
            hazelnut_count += 1
            field[squirrel_pos[0]] = field[squirrel_pos[0]][:squirrel_pos[1]] + '*' + field[squirrel_pos[0]][
                                                                                      squirrel_pos[1] + 1:]
            if hazelnut_count == 3:
                return "Good job! You have collected all hazelnuts!\nHazelnuts collected: {}".format(hazelnut_count)
        elif cell == 't':
            return "Unfortunately, the squirrel stepped on a trap...\nHazelnuts collected: {}".format(hazelnut_count)

    return "There are more hazelnuts to collect.\nHazelnuts collected: {}".format(hazelnut_count)


def play_game():
    n, directions, field = parse_input()
    result = simulate_game(n, directions, field)
    print(result)


play_game()