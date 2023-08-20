def words_sorting(*words):
    values = {}
    result_str = []
    for word in words:
        numbers = 0

        for letter in word:
            number = ord(letter)
            numbers += number

        values[word] = numbers

    sum_of_numbers = sum(values.values())
    if sum_of_numbers % 2 == 0:
        for word in sorted(values.items(), key=lambda x: x[0]):
            result_str.append(f"{word[0]} - {word[1]}")
    else:
        for word in sorted(values.items(), key=lambda x: -x[1]):
            result_str.append(f"{word[0]} - {word[1]}")




    return '\n'.join(result_str)






print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
        ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
