# Lambda and Map funcions Example
print("### Lambda and Map function examples ###")
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

print("### Class variable and instance variable example ###")

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