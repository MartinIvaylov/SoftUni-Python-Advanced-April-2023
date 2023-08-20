new_file = "my_first_file.txt"
content = "I just created my first file!"
with open(new_file, 'w') as file:
    file.write(content)