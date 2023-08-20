n = int(input())
numbers = []
for number in range(1, n + 1):
    numbers.append(number)

print(*numbers, sep="")