first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

functions = {
    "Add First": lambda x: [first.add(el) for el in x],
    "Add Second": lambda x: [second.add(el) for el in x],
    "Remove First": lambda x: [first.discard(el) for el in x],
    "Remove Second": lambda x: [second.discard(el) for el in x],
    "Check Subset": lambda: print(True) if first.issubset(second) or second.issubset(first) else print(False)

}

for _ in range(int(input())):
    first_command, *data = input().split()
    command = first_command + " " + data.pop(0)

    if data:
        functions[command](int(x) for x in data)
    else:
        functions[command]()

    # if command == "Add First":
    #     [first.add(int(el)) for el in data]
    # elif command == "Add Second":
    #     [second.add(int(el)) for el in data]
    # elif command == "Remove First":
    #     [first.discard(int(el)) for el in data]
    # elif command == "Remove Second":
    #     [second.discard(int(el)) for el in data]
    # else:
    #     if first.issubset(second) or second.issubset(first):
    #         print(True)
    #     else:
    #         print(False)

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
