def func_executor2(*args):
    return '\n'.join([f"{func.__name__} - {func(*args)}" for func, args in args])


# def func_executor(*args):
#     result = []
#     for func, args in args:
#         result.append(f"{func.__name__} - {func(*args)}")
#
#     return "\n".join(result)


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor2(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))
