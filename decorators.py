# Decorators are higher order functions
# That takes another function (or methods) as an argument

# Basic decorator structure in python

def my_decorator(func):
    def wrapper():
        print("This is before the function is called.")
        func()
        print("This is after the function is called.")

    return wrapper

# Applying the decorator
@my_decorator
def say_hello():
    print("Hello 2025!!")

# Here: say_hello() = my_decorator(say_hello)
# test 1
# say_hello()

# Decorators with Arguments
def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs): # *args: positional, **kwargs: key-values arguments
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_decorator(times=3)
def say_foobar():
    print("foo : bar!!")

# say_foobar()

# logging decorator
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        # return result
    return wrapper

@log_decorator
def add(a,b):
    return a+b

# add(2,3)

# Authentication decorator
def require_auth(func):
    def wrapper(*args, **kwargs):
        user = kwargs.get("user")
        if user != "admin":
            print("Unauthorized!")
            return
        return func(*args, **kwargs)
    return wrapper

@require_auth
def view_dashboard(*args, **kwargs):
    print("Welcome to the admin dashboard!")

# view_dashboard(user="guest") # Unauthorized
# view_dashboard(user="admin") # Welcome to the admin dashboard

import time
# Timing decorator
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(5)
    print("done!")

# slow_function()
# Python built in decorators: @staticmethod, @classmethod, @property

# Both positional and keyword argument
def alt_decorator(func):
    def wrapper(*args, **kwargs): # captures any arguments
        print(f"Arguments passed to the function: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs) # passes args to original functions
        print(f"Result of the function {result}")
        return result
    return wrapper

@alt_decorator
def org_function(a, b, c=8):
    return a+b+c

# org_function(1, 2, c=9)

# second example with both args
def greet_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} and kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@greet_decorator
def greet(name, greeting="Happy days ahead"):
    return f"{greeting}, {name}!"

greet("Alice")
greet("Bob", greeting="Hello")
