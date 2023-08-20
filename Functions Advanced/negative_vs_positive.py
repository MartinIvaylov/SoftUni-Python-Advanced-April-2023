def sum_negative():
    sum_of_negative_numbers = 0
    for num in numbers:
        if num < 0:
            sum_of_negative_numbers += num

    return sum_of_negative_numbers


def sum_positive():
    sum_of_positive_numbers = 0
    for num in numbers:
        if num > 0:
            sum_of_positive_numbers += num

    return sum_of_positive_numbers


def print_function(positive, negative):
    print(negative_numbers)
    print(positive_numbers)

    if abs(negative) > abs(positive):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]

positive_numbers = sum_positive()
negative_numbers = sum_negative()
print_function(positive_numbers, negative_numbers)
