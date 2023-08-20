# def get_info(**kwargs):
#     values = []
#     for k, v in kwargs.items():
#         values.append(v)
#
#     return f"This is {values[0]} from {values[1]} and he is {values[2]} years old"



def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"




print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
