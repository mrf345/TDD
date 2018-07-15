from static_parameters import function_parameters

@function_parameters
def print_something(input):
    """To print and return the input ((input:str))"""
    print(input)
    return input

# def print_something_heavily(input, times):
    """ To print and return input. With memory overflow 
        ((input:str)) ((times:int))
    """
    for _ in range(0, times):
        locals()[str(_)] = hash(_)
    print(input)
    return input