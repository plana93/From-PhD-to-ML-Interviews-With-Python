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



print()
print("############################################################")
print()
############################################################
############################################################



