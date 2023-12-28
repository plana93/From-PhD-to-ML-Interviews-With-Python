# Example to Explain Shallow and Deep Copy

import copy

# Original List with nested list
original_list = [1, [2, 3], [4, 5]]

# Shallow Copy
shallow_copy = copy.copy(original_list)

# Deep Copy
deep_copy = copy.deepcopy(original_list)

# Modify the original list
original_list[1][0] = 'X'

# Output
print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)

print()
print("############################################################")
print()
############################################################
############################################################

# Lambda and Map funcions Example
x = 3
y = lambda x: x * x

print(f"lambda function lambda x: x * x, input --> {x} and output --> {y(x)} ")

x = [1,3,5,7]

print(f"Map function lambda x: x * x, input --> {x} and output --> {list(map(y,x))} ")


print()
print("############################################################")
print()
############################################################
############################################################

# class variable and instance variable Example
print("Class variable and instance variable example")

class MyClass:
    class_variable = 10

obj1 = MyClass()
obj2 = MyClass()

print(f"It shows how the two objs share the same class variable --> {obj1.class_variable} and {obj2.class_variable} ")

MyClass.class_variable = 20

class MyClass:
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

obj1 = MyClass(5)
obj2 = MyClass(10)

print(f"It shows how the two instance variables are specific to each instance --> {obj1.instance_variable} and {obj2.instance_variable}")

print()
print("############################################################")
print()
############################################################
############################################################

# Monkey Patching Example

class Dog:
    def bark(self):
        return "Woof!"

# Original behavior
my_dog = Dog()
original_sound = my_dog.bark()
print("Original Sound:", original_sound)

# Monkey patching - adding a playful behavior
def playful_bark(self):
    return "Bark! Bark! Playful Woof!"

# Applying the monkey patch
Dog.playful_bark = playful_bark
playful_sound = my_dog.playful_bark()

# Now, my_dog can exhibit the playful behavior
print("Playful Sound:", playful_sound)

print()
print("############################################################")
print()
############################################################
############################################################

# Staticmethod vs Classmethod Example
class MyClass:
    class_variable = "Class Variable"

    @staticmethod
    def static_method():
        return "Static Method"

    @classmethod
    def class_method(cls):
        return f"Class Method accessing {cls.class_variable}"

# Usage
static_result = MyClass.static_method()
class_result = MyClass.class_method()

# Output
print("Static Method Result:", static_result)
print("Class Method Result:", class_result)

print()
print("############################################################")
print()
############################################################
############################################################

# Singleton Example

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Usage
singleton_instance_1 = Singleton()
singleton_instance_2 = Singleton()

# Check if both instances refer to the same object
are_same_instance = singleton_instance_1 is singleton_instance_2

# Output
print("Are the instances the same?", are_same_instance)

print()
print("############################################################")
print()
############################################################
############################################################

# Meta class Example

# Meta-class for enforcing attribute naming convention
class AttributeNamingMeta(type):
    def __new__(cls, name, bases, dct):
        # Enforce the naming convention for attributes
        print(name)
        print(bases)
        print(dct)
        for attribute_name, value in dct.items():
            if not attribute_name.startswith("custom_"):
                new_attribute_name = "custom_" + attribute_name
                dct[new_attribute_name] = dct.pop(attribute_name)

        # Create the class
        return super().__new__(cls, name, bases, dct)


# Usage
class CustomAttributesClass(metaclass=AttributeNamingMeta):
    custom_name = "John"
    custom_age = 30
    # otherName = "Mark" # RuntimeError: dictionary keys changed during iteration


# Accessing attributes
print(CustomAttributesClass.custom_name)  # Output: John
print(CustomAttributesClass.custom_age)  # Output: 30

print()
print("############################################################")
print()
############################################################
############################################################

# abstract class Example

from abc import ABC, abstractmethod

class AbstractShape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Usage
class ConcreteCircle(AbstractShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius


print()
print("############################################################")
print()
############################################################
############################################################

