# Monkey Patching Example
print("### Monkey Patching Example ###")
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
print("### Staticmethod vs Classmethod Example ###")
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
print("### Singleton Example ###")

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
print(" Meta class Example")

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
print("### Abstract class Example ###")
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
