from math import log

number = int(input())
logarithm_base = input()

if logarithm_base == "natural":
    log_number = log(number)
else:
    log_number = log(number, int(logarithm_base))

print(f"{log_number :.2f}")
