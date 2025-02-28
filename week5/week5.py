# class Parent:  # Creating the parent class
#     def greet(self):
#         print('Hello from the Parent class!')
#
# class Child(Parent):  # Creating the child class
#     pass
#
# # Creating an instance of the Child class
# child = Child()
# child.greet()

# class Parent:
#     def greet(self):
#         print('Hello from the Parent class!')
#
# class Child(Parent):
#     def greet(self):
#         super().greet()
#         print('Hello from the Child class!')
#
# # Creating an instance of the Child class
# child = Child()
# child.greet()


# class Father:
#     def skills(self):
#         print('Programming and Cooking')
#
# class Mother:
#     def skills(self):
#         print('Art and Teaching')
#
# class Child(Father, Mother):
#     pass
#
# # Creating an instance of the Child class
# child = Child()

# class Grandparent:
#     def greet(self):
#         print('Hello from the Grandparent class!')
#
# class Parent(Grandparent):
#     pass
#
# class Child(Parent):
#     pass
#
# # Creating an instance of the Child class
# child = Child()
# child.greet()

# class Parent:
#     def greet(self):
#         print('Hello from the Parent class!')
#
# class Child1(Parent):
#     pass
#
# class Child2(Parent):
#     pass
#
# # Creating instances of the Child classes
# child1 = Child1()
# child2 = Child2()
# child1.greet()
# child2.greet()

# class Engine:
#     def start(self):
#         print('Engine starts')
#
# class Car:
#     def __init__(self):
#         self.engine = Engine()
#     def start(self):
#         self.engine.start()
#
# #creating an instance of the Car class
# car=Car()
# car.start()

# class Engine:
#     def start(self):
#         print('Engine.starts')
#
# class Car:
#     def __init__(self, engine):
#         self.engine = engine
#     def start(self):
#         self.engine.start()
#
# #creating an instance of the Engine class
# engine = Engine()
#
# #creating an instance of the Car class
# #and passing the engine object to it