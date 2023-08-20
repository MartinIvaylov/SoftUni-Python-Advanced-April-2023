# def even_odd(*args):
#     command = args[-1]
#     numbers = []
#     for num in args[:-1]:
#         if command == 'even' and int(num) % 2 == 0:
#             numbers.append(num)
#
#         elif command == 'odd' and int(num) % 2 == 1:
#             numbers.append(num)
#
#     return numbers

def even_odd(*args):
    command = args[-1]

    if command == 'even':
        return [n for n in args[:-1] if n % 2 == 0]
    elif command == 'odd':
        return [n for n in args[:-1] if n % 2 == 1]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))