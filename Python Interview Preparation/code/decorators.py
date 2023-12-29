
print("### Decorator example ###")

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()


print()
print("############################################################")
print()
############################################################
############################################################

print("### A closure example ###")

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)

# The closure retains access to the variable 'x'
result = closure(5)
print(result)  # Output: 15

print()
print("############################################################")
print()
############################################################
############################################################

print("Example of chain of function decorators")

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"
    return wrapper

@exclamation_decorator
@uppercase_decorator
def greet(name):
    return f"Hello, {name}"

# Equivalent to greet = exclamation_decorator(uppercase_decorator(greet))

result = greet("John")
print(result)  # Output: HELLO, JOHN!
