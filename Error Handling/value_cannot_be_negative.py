# Create your own exception called ValueCannotBeNegative.\n
# Write a program that reads five numbers from the console (on separate lines).\n
# If a negative number occurs, raise the exception.
# Traceback (most recent call last):
#   File ".\value_cannot_be_negative.py", line 8, in <module>
#     raise ValueCannotBeNegative
# __main__.ValueCannotBeNegative

class ValueCannotBeNegative(Exception):
    pass
numbers = [int(input()) for _ in range(5)]

for num in numbers:

    if num <0:
        raise ValueCannotBeNegative(f"Value cannot be negative number.Convert {num} to {abs(num)}")

