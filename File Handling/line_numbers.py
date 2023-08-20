from string import punctuation

with open("text.txt", "r") as file:
    text = file.readlines()

output_file = open("output.txt", "w")

for i in range(len(text)):
    row = text[i]

    letters = 0
    symbols = 0

    for symbol in row:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            symbols += 1

    output_file.write(f"Line {i + 1}: {''.join(row[:-1])} ({letters})({symbols})\n")

output_file.close()
