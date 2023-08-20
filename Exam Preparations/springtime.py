def start_spring(**data):
    type_of_object = {}
    result = ""

    for key, value in data.items():
        if not value in type_of_object:
            type_of_object[value] = []
            type_of_object[value].append(key)
        else:
            type_of_object[value].append(key)

    sorted_collections_and_objects = sorted(type_of_object.items(), key=lambda x: (-len(x[1]), x[0]))

    for tuple_ in sorted_collections_and_objects:
        type_object = tuple_[0]
        list_of_objects = tuple_[1]
        sorted_list_of_objects = sorted(list_of_objects)
        result += f"{type_object}:\n"
        for obj in sorted_list_of_objects:
            result += f"-{obj}\n"

    return result.strip()







example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
