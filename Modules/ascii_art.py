from pyfiglet import figlet_format

# print(f"{figlet_format(input())}")

def print_msg(msg):
    ascii_art = figlet_format(msg)
    print(ascii_art)

print_msg(input())
