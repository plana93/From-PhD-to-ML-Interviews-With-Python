# Python Interview Preparation

Welcome to my Python interview preparation repository! This space is dedicated to brushing up on various aspects of Python to excel in interviews.

## Table of Contents
0. [Basics-0](#basics-0)
1. [Basics-1](#basics-1)
2. [Functions](#functions)
3. [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
4. [Exception Handling](#exception-handling)
5. [File Handling](#file-handling)
6. [Modules and Packages](#modules-and-packages)
7. [List Comprehensions](#list-comprehensions)
8. [Generators and Iterators](#generators-and-iterators)
9. [Decorators](#decorators)
10. [Concurrency](#concurrency)
11. [Common Libraries and Frameworks](#common-libraries-and-frameworks)
12. [Time and Space Complexity](#time-and-space-complexity)
13. [Coding Challenges](#coding-challenges)

## Basics-0
<details>
<summary><strong> Details </strong></summary>

### What is Python, and how is it different from other programming languages?

**Answer:** Python is a high-level, interpreted programming language known for its <ins>readability</ins> and <ins>simplicity</ins>. It emphasizes code readability and allows programmers to express concepts in fewer lines of code than might be possible in languages such as C++ or Java. <ins>Python supports multiple programming paradigms, including procedural, object-oriented, and [functional programming](https://en.wikipedia.org/wiki/Functional_programming).</ins>

### Explain the differences between Python 2 and Python 3.

**Answer:** Python 2 and Python 3 are two major versions of the Python programming language. Python 3 was introduced as an upgrade to Python 2 with some significant changes to improve consistency and eliminate redundancy. Key differences include changes to print syntax (print is a function in Python 3), Unicode support, integer division, and various library updates. Python 2 reached its end of life on January 1, 2020, and developers are encouraged to use Python 3 for all new projects.

### What are the main features of Python?

**Answer:** Python has several key features:

- **Readability:** Python's syntax is clear and readable, making it an excellent language for beginners.
- **Versatility:** Python supports both procedural and object-oriented programming paradigms.
- **Interpretation:** It is an <ins>interpreted language</ins>, which means code execution occurs line by line.
- **Dynamic typing:** <ins>Variables are dynamically typed</ins, allowing flexibility.
- **Extensive libraries:** Python has a rich standard library and numerous third-party libraries, facilitating diverse applications.
- **Community support:** Python has a large, active community contributing to its development and providing support.

### What are the different data types in Python?

**Answer:** Python has various data types, including int (integer), str (string), float (floating-point), tuple, list, dict (dictionary), and bool (boolean).

### What is the output of (0, 1, 2, 3, (4, 5, 6), 7, 8, 9)[::2]

**Answer:** (0, 2, (4, 5, 6), 8) Certainly, the annotation [::2] is a slicing notation in Python that allows extracting a subsequence from a sequence (such as a list or tuple) by specifying three parameters separated by colons. The general form is start:stop:step, where: 
- start represents the starting index (inclusive).
- stop represents the ending index (exclusive).
- step represents the step or increment between selected elements.

### What is the output of (10, 20, 30, 40, 50)[::-2]?

**Answer:** (50, 30, 10). The notation [::-2] reverses the tuple and returns every second element. The [::-2] slice notation means to start from the end and move backwards by 2 steps. In this case, it starts from the end of the tuple and selects every second element moving towards the beginning.

### Output of l_numbers=[[]]*5, l_numbers[0].append(1)?

**Answer:** _l_numbers_ will be equal to [[1], [1], [1], [1], [1]]. When you multiply a list by a number, you get a list of references to the same elements. So, modifying one of them reflects on all.

### What is the difference between == and is in Python?

**Answer:** _==_ is a comparison operator that checks <ins>equality</ins> between the values of two objects.
_is_ is an identity operator that checks whether two variables <ins>refer to the same object in memory</ins>.


### What is the purpose of the single underscore “_” variable in Python?

**Answer:** In Python, the single underscore (_) has several conventional uses, and its purpose can depend on the context in which it is used. Here are some common cases: 
i) Placeholder for Unused Variables 
ii) Last Expression in an Interactive Interpreter
ii) "I don't care" in Unpacking ->  _, _, result = some_function_returning_a_tuple()

### Explain the concept behind dictionary in Python

**Answer:** In Python, a dictionary is a data structure that stores a collection of key-value pairs. Each key in a dictionary must be unique. You cannot have duplicate keys; if you try to use the same key more than once, the new value will overwrite the previous one.
Keys must be of a type that is <ins>immutable</ins>, meaning they cannot be changed after creation (e.g. you cannot use a list as key). Common examples of immutable types for keys include strings, numbers, and tuples.
Values in a dictionary can be of any data type, including numbers, strings, lists, or even other dictionaries (also mixed).
<ins>Dictionaries are mutable.</ins> Dictionaries provide fast and efficient lookups. 

### Difference between an expression and a statement in Python

**Answer:**: A _statement_ is a complete line of code that performs an action. It's an executable unit that can include assignments, function calls, loops, conditionals, etc.
An _expression_ is any part of the code that evaluates to a value. It can be a combination of variables, operators, and function calls. 
An expression can also be a statement if it stands alone as a complete line of code. In some languages, expressions and statements are distinct, but in Python, many expressions can be used as statements.


### Difference between an array and list

**Answer:** 

1. **Data Type:**
   - **List:** Holds elements of different data types.
   - **Array:** Typically holds elements of the same data type.

2. **Memory Efficiency:**
   - **List:** More memory-efficient but less space-efficient.
   - **Array:** More space-efficient due to contiguous memory.

3. **Operations:**
   - **List:** Versatile with many built-in methods.
   - **Array:** Fewer built-in methods; specialized libraries like NumPy enhance functionality.

4. **Usage:**
   - **List:** General-purpose data storage and manipulation.
   - **Array:** Common in mathematical and scientific computations.

5. **Mutability:**
   - **List:** Mutable; elements can be changed after creation.
   - **Array:** Core arrays are mutable; NumPy arrays can be mutable or immutable.

In summary, lists offer flexibility, while arrays are more specialized for certain tasks, especially in scientific computing.


#### Data Types

- Understanding and working with various data types:
  ```python
  # Example
  num = 42
  name = "John"
  coordinates = (10.5, 20.0)
  
  # Everything from numbers, lists, strings, functions and classes are python objects.
  ```

#### Operators

- Utilizing operators for arithmetic, comparison, logical operations:
  ```python
  # Example
  result = 10 + 5  # Addition
  is_equal = (3 == 3)  # Comparison
  logical_result = True and False  # Logical AND
  ```

#### Variables

- Declaring and using variables to store values:
  ```python
  # Example
  age = 30
  message = f"My age is {age}."
  ```

#### Control Flow

- Implementing control flow structures such as if statements, loops:
  ```python
  # Example
  age = 30
  if age >= 18:
      print("You are an adult.")
  else:
      print("You are a minor.")
  
  # Loop example
  for i in range(5):
      print(i)
  ```

more examples in the file code/basics_0.py  

</details>

## Basics-1
<details>
<summary><strong> Details </strong></summary>

### What is mutable and immutable objects/data types in Python?

**Answer:**: Mutation generally refers to 'change'. So when we say that an object is mutable or immutable we meant to say that the value of object can/cannot change.
When an object is created in Python, it is assigned a _type_ and an _id_. <ins> An object/data type is mutable if with the same id, the value of the object changes after the object is created. </ins>
**Mutable objects** in Python -- Objects that can change after creation. Lists, byte arrays, sets, and dictionaries.
**Immutable objects** in Python -- Numeric data types, strings, bytes, frozen sets, and tuples.


### What is the difference between list and tuples in Python?

**Answer:**
**Mutability** list is mutable and tuple is immutable. 
**Syntax definition**,
**Performance** List: Slower due to mutability and Tuple: Faster due to immutability
**Memory Consumption** List: Consumes more memory and  Tuple: More memory-efficient

### How is memory managed in Python?

**Answer:**: Memory in Python is managed using a private heap space. The Python Memory Manager handles the allocation and deallocation of memory for objects. Garbage collection is employed to reclaim memory from unused objects.


### Explain shallow and deep copy in Python

**Answer:**: In Python, a shallow copy creates a new object but does not clone nested objects. A deep copy, on the other hand, creates a new object and recursively clones all nested objects.


### Why Python generates a .pyc file even when it is an interpreted language?

**Answer:**:# Python is both interpreted and compiled. When a .py file is executed, 
it goes through a compilation process called bytecode compilation.
The generated bytecode is platform-independent and stored in .pyc files to improve execution speed on subsequent runs.
.pyc files contain the compiled version of the Python source code, making it faster to load and execute.
When a .py file is imported, Python checks if a corresponding .pyc file exists and is newer. 
If not, it compiles the .py file into .pyc.

### How private varibles are declared in Python?

**Answer:**: Python does not have anything called private member however by convention two underscore before a variable or function makes it private.

### Can _set_ have lists as elements?

**Answer:**: No, a set in Python cannot have lists as elements. Sets are designed <ins> to store unique and immutable elements. </ins> Since lists are mutable (meaning their contents can be changed after they are created), they cannot be used as elements in a set.


</details>

## Functions
<details>
<summary><strong> Details </strong></summary>

### Explain briefly about lambda() and map() functions. 

**Answer:**: <ins>Lambda()</ins> function mainly used to create a function without a name, 
it can receive any number of arguments, but can only have one expression.

<ins>Map()</ins> function takes a function and a list as input. 
Map() performs an operation on the entire list and return the result in a new list
(see example on basics_1.py).

### Difference between a class variable and instance variable.

**Answer:**: In Python, class variables are shared among all instances of a class and have a global scope within the class.
Instance variables, declared with "self" inside methods or the constructor, 
are specific to each instance and have a local scope within that instance (see example on basics_1.py).

</details>

## Object-Oriented Programming (OOP)
<details>
<summary><strong> Details </strong></summary>

### What is monkey patching? How to use it in Python?

**Answer:**: Monkey patching refers to dynamically modifying or extending a module or class at runtime, 
typically to alter behavior or add features (see example on basics_1.py).


### What is the difference between staticmethod and classmethod?

**Answer:**: The key difference lies in how they are bound to the class. `staticmethod` is bound to the class and takes no special first argument, 
while `classmethod` is bound to the class and takes the class as its first argument (see example on basics_1.py).


### Explain Singleton class and its uses?

**Answer:**: A Singleton class ensures that only one instance of the class is created and provides a global point of access to that instance. 
It is often used when exactly one object is needed for coordination or to control actions (see example on basics_1.py).

### Explain Meta Classes in Python. 

**Answer:**: Meta-classes in Python are classes that define the behavior of other classes, 
commonly known as class factories. They allow customization and modification of class creation, 
often used to enforce coding standards or add specific behaviors to classes (see example on basics_1.py).

### Explain Abstract Classes and its uses.

**Answer:**: Abstract classes in Python are classes that cannot be instantiated and typically include abstract methods 
that must be implemented by their subclasses. 
They serve as a blueprint for other classes and ensure that certain methods are implemented by concrete classes (see example on basics_1.py).


# Explain object creation process in detail. Which method is called first?

**Answer:**: During object creation in Python, the class is defined with its attributes and methods. 
Memory is allocated for the object. Optionally, the __new__ method is called to create and return the object. 
Subsequently, the __init__ method is invoked to initialize the object's attributes.


Explain inheritance in Python / What is MRO in Python? How does it work?

<ins>Inheritance</ins> is a fundamental concept in object-oriented programming (OOP) that allows a class (subclass or derived class) to inherit attributes and methods from another class (base class or parent class). This promotes code reuse and the creation of a hierarchy of classes.

- Classes, objects, inheritance, encapsulation

</details>

## Exception Handling
<details>
<summary><strong> Details </strong></summary>

Explain exception handling in Python.
Is there a sequence in defining exceptions in except block for exception handling?

- try, except, else, finally blocks

</details>

## File Handling
<details>
<summary><strong> Details </strong></summary>

How would you load large data file in Python?

- Reading and writing to files, context managers

</details>

## Modules and Packages
<details>
<summary><strong> Details </strong></summary>

What's the difference between a Python module and a Python package?

- Importing modules, creating packages

</details>

## List Comprehensions
<details>
<summary><strong> Details </strong></summary>

Which is faster, list comprehension or for loop?

- Creating concise lists

</details>

## Generators and Iterators
<details>
<summary><strong> Details </strong></summary>


Explain Generators and use case of it.
What is an iterator? How is iterator is different from a generator?

- Yield statement, iterating through generators

</details>

## Decorators
<details>
<summary><strong> Details </strong></summary>

Explain Closures in Python
How to make a chain of function decorators?

- Defining and using decorators

</details>

## Concurrency
<details>
<summary><strong> Details </strong></summary>

What is a global interpreter lock (GIL)?
Explain threading in Python

- Threading vs. multiprocessing, GIL

</details>

## Common Libraries and Frameworks
<details>
<summary><strong> Details </strong></summary>

- Requests, NumPy, Pandas, Flask/Django

</details>

## Time and Space Complexity
<details>
<summary><strong> Details </strong></summary>

- Big O notation, algorithm efficiency

</details>

## Coding Challenges
<details>
<summary><strong> Details </strong></summary>

- Practice on platforms like LeetCode, HackerRank

</details>




Feel free to use this repository to track your progress and make updates as you continue your preparation. Happy coding!
