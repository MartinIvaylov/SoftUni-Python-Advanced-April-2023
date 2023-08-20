text = input()
times_to_repeat = input()

# if times_to_repeat.isdigit():
#     print(text * int(times_to_repeat))
# else:
#     print("Variable times must be an integer")

try:
    print(text * int(times_to_repeat))
except ValueError:
    print("Variable times must be an integer")
