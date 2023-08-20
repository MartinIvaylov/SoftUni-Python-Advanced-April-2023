from collections import deque

egg_size = deque(map(int, input().split(", ")))
paper_size = deque(map(int, input().split(", ")))
BOX_SIZE = 50
boxes_filled = 0

while egg_size and paper_size:
    current_egg = egg_size.popleft()
    current_paper = paper_size.pop()

    if current_egg <= 0:
        paper_size.append(current_paper)
        continue

    if current_egg == 13:

        left_paper = paper_size.popleft()
        paper_size.appendleft(current_paper)
        paper_size.append(left_paper)
        continue

    if current_egg + current_paper <= BOX_SIZE:
        boxes_filled += 1

    else:
        continue


if boxes_filled:
    print(f"Great! You filled {boxes_filled} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if egg_size:
    print(f"Eggs left: {', '.join(map(str,egg_size))}")

if paper_size:
    print(f"Pieces of paper left: {', '.join(map(str, paper_size))}")