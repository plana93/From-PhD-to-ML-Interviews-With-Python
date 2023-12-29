print("############################################################")

print("### Generators Example ###")

# When the line yield a is executed in the fibonacci_generator function,
# the value of a is returned to the caller, and at the same time, the function's state is suspended.
# The next time the function is called using next, it resumes from the statement following yield,
# retaining the value of a and allowing b to be updated in the next iteration.
# In summary, yield allows the function to maintain an internal state, and each time it is called with next,
# the function resumes from where it left off, producing the next value in the Fibonacci sequence.
# A return is not necessary because the function can be called multiple times while preserving its state.

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator to print the first 10 Fibonacci numbers
fibonacci_gen = fibonacci_generator()
for _ in range(10):
    print(next(fibonacci_gen))

print()
print("############################################################")
print()
############################################################
############################################################


print("### Iterator Example ###")

class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

# Using the custom iterator
my_iter = MyIterator(5)

# Iterating through the iterator
for value in my_iter:
    print(value)

print()
print("############################################################")
print()
############################################################
############################################################