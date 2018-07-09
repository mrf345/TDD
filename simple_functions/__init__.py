def print_something(input):
    """ To print and return the input """
    if not isinstance(input, str):
        raise(
            TypeError(
                "print_something(input=) must be string"))
    print(input)
    return input


# from time import sleep

# def print_something_slowly(input, duration):
#     """ To sleep, print and return input """
#     if not isinstance(input, str):
#         raise(
#             TypeError(
#                 "print_something_slowly(input=) must be string"))
#     if not isinstance(duration, int):
#         raise(
#             TypeError(
#                 "print_something_slowly(duration=) must be int"))
#     sleep(duration)
#     print(input)
#     return input