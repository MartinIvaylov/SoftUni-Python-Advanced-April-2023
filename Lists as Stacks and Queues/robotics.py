from collections import deque
from datetime import datetime, timedelta

robots = {r.split("-")[0]: [int(r.split("-")[1]), 0] for r in input().split(";")}
# robots  = {}
# for r in input().split(";"):
#   name, time_needed = input().split()
#   robots[name] = [int(time_needed), 0]
#
#
#
#
#
factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()

    if product == "End":
        break

    products.append(product)

while products:
    factory_time += timedelta(0, 1)
    product = products.popleft()

    robots = {r[0]: [r[1][0], r[1][1] - 1]  if r[1][1] != 0 else r[1] for r in robots.items()}
#   for r in robots.items():
#       if value[1] != 0:
#           robots[name][1] -= 1
#
#
#
#
#
    free_robots = list(filter(lambda x: x[1][1] == 0, robots.items()))

    if not free_robots:
        products. append(product)
        continue
    robots[free_robots[0][0]][1] = free_robots[0][1][0]

    print(f"{free_robots[0][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")