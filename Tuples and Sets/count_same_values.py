values = tuple(map(float, input().split()))
# counter_of_values = {value: values.count(value) for value in values}
#
# # for k, v in counter_of_values.items():
# #     print(f"{k} - {v} times")
#
# # def count_method(vales, value):
# #     count = 0
# #     for n in vales:
# #         if n == value:
# #             count += 1
# #
# #     return count
value_counter = {}
for value in values:
    if value not in value_counter:
        value_counter[value] = 0
    value_counter[value] += 1

for k, v in value_counter.items():
    print(f"{k} - {v} times")


