## Basics-0

#### Data Types
##### Understanding and working with various data types:

# Example
number = 23  # int
name = "S.W.Erdnase"  # str
l_odd_numbers = [1, 3, 5, 7, 9]  # list
tuple_numbers = (1, 4)  # tuple
dict_examples = {"A": 1, "B": 2}

# Everything from numbers, lists, strings, functions and classes are python objects.

#### Operators
#####  Utilizing operators for arithmetic, comparison, logical operations:

# Example
output_sum = 10 + 5  # Addition
is_equal = (3 == 3)  # Comparison
logical_result = True and False  # Logical AND

#### Variables
##### Declaring and using variables to store values:

# Example
age = 30
message = f"My age is {age}."
print(message)

#### Control Flow
##### Implementing control flow structures such as if statements, loops:

# Example
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Loop example
start = 0
end = 5
step = 1
for idx in range(start, end, step):
    print(idx)


tuple_example = (0, 1, 2, 3, (4, 5, 6), 7, 8, 9)
print(tuple_example[::3]) # 0 3 8
print(tuple_example[::2]) # 0 2 (4, 5, 6) 8
print(tuple_example[::-2]) # 9 7 3 1

l_numbers = [[]] * 5
print(l_numbers)
l_numbers[0].append(1)
print(l_numbers)
l_numbers[1][0] = 3
print(l_numbers)

