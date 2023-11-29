def my_func(add_numbers):
    def wrapper (*args, **kwargs):

        result = add_numbers(*args,**kwargs)
        return result*2
    return wrapper

@my_func
def add_numbers(a,b):
    return a+b

print(add_numbers(a = int(input()),b = int(input())))