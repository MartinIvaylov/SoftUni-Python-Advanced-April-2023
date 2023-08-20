def file_numbers_sum(file_name):
    data = open(file_name, "r")

    sum_numbers = 0
    try:
        for num in data:
            sum_numbers += int(num)
    except ValueError:
        pass

    return sum_numbers


result = file_numbers_sum("numbers.txt")
print(result)
