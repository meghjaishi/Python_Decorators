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

# After decorating the function behaves like: say_hello() = my_decorator(say_hello)
# test 1
# say_hello()

# Decorators with Arguments
def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs): # *args: positional, **kwargs: key-values arguments
            print(f"Calling function {func.__name__} {times} times with positional arguments {args} and keyword arguments {kwargs}")
            for _ in range(times):
                func(*args, **kwargs)
            print(f"Function {func.__name__} successfully called {times} times")
        return wrapper
    return decorator

@repeat_decorator(times=4)
def repeat_utterances(d, name):
    print(f"Okay, {name}, Let's meet again in {d} days!")

# repeat_utterances(15, name="Maria")

# logging decorator
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        # return result
    return wrapper

@log_decorator
def population(a,b, country):
    return f"The human poputation of {country} is roughly {a+b} billion"

# population(0.7, 0.7, country="India")

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
    print(f"Welcome to the admin dashboard of {args[0]}!!")

# view_dashboard("TopWorld", user="guest") # Unauthorized
# view_dashboard("TopWorld", user="admin") # Welcome to the admin dashboard

import time
# Timing decorator
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took: {end_time - start_time:.2f} seconds")
        print(f"Finally I am {result}")
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(3)
    return "done!"

# slow_function()
# Some python built in decorators: @staticmethod, @classmethod, @property

# Some more decorators with both args and kwargs
def alt_decorator(func):
    def wrapper(*args, **kwargs): # captures any arguments
        print(f"Arguments passed to the function: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs) # passes args to original functions
        print(f"Result of the function: {result}")
    return wrapper

@alt_decorator
def org_function(a, b, c=8):
    return a+b+c

# org_function(1, 2, c=9)

# second example with both args
def greet_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} and kwargs={kwargs}")
        # result = func(*args, **kwargs)
        # print(f"{func.__name__} returned {result}")
        print(func(*args, **kwargs)) # Call the original function
    return wrapper

@greet_decorator
def greet(name, greeting="Happy days ahead"):
    return f"{greeting}, {name}!"

# greet("Alice")
# greet("Bob", greeting="Hello")

# Somr more examples 

def authinate(func):
    def wrapper(*args, **kwargs):
        user = kwargs.get("User")
        if user == "TVC":
            print("Permission Denied! Please contact your contract manager")
            return
        elif user ==  "FTE":
            print("Unauthorized! Please check with your mananger")
            return
        elif user == "Admin":
            return func(*args, **kwargs)
        else:
            return
    return wrapper

@authinate
def authorize(*args, **kwargs):
    print(f"Welcome to the admin dashboard of {args[0]}!!")

authorize("TopWorld", User="TVC")
authorize("TopWorld", User="FTE")
authorize("TopWorld", User="Admin")
        

