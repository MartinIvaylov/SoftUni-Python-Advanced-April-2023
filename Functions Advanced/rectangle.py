# def rectangle(length, width):
#     if length != int(length) or width != int(width):
#         return "Enter valid values!"
#     else:
#         def area():
#             return length * width
#
#         def perimeter():
#             return 2 * (width + length)
#
#     return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return 2 * (width + length)

    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


print(rectangle(2, 10))
print(rectangle('2', 10))
