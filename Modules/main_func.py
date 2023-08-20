import operator as op


# def print_triangle(size):
#     for row in range(1, size + 2):
#         print(*[col for col in range(1, row)])
#     for row in range(size, 0, -1):
#         print(*[col for col in range(1, row)])

def print_triangle(size):
    figure = ""

    for row in range(1, size + 1):
        for i in range(1, row + 1):
            figure += f"{i}"
        figure += "\n"
    for row in range(size, 0, -1):
        for i in range(1, row):
            figure += f"{i}"
        figure += "\n"

    return figure


def mathematical_operation(first_number, operator, second_number):
    first_number, second_number = int(first_number), int(second_number)
    valid_operators = {
        "+": op.add,
        "-": op.sub,
        "*": op.mul,
        "/": op.truediv,
        "^": op.xor
    }

    return valid_operators[operator](first_number, second_number)


sequence_of_numbers = []


def create_fibonacci_sequence(number):
    sequence_of_numbers.clear()
    sequence_of_numbers.append(0)
    sequence_of_numbers.append(1)

    for _ in range(number - 2):
        sequence_of_numbers.append(
            sequence_of_numbers[-1] + sequence_of_numbers[-2]
        )

    return " ".join(map(str, sequence_of_numbers))


def locate_number(element):
    if element in sequence_of_numbers:
        element_index = sequence_of_numbers.index(element)
        return f"The number - {element} is at index {element_index}"
    else:
        return f"The number {element} is not in the sequence"
