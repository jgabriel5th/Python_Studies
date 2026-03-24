'''
Object-Oriented Programming:
It is one of the paradigms or patterns in programming, paradigms define how to write and structure the code.
Each paradigm has different functionalities and behaviors.

Examples of programming patterns:
- Structural programming
- Procedural programming
- Object-oriented programming
- Functional programming
- And there are more...
'''
# Python is an object-oriented programming language, and here's an example with type() function:
name = "João"
print(type(name)) # it returns <class 'str'>

'''
Classes and Objects:
- OOP is a paradigm that provides a means for structuring programs so that properties and behaviors are bundled into indivual objects.
- The two main concepts about OOP are Classes and Objects, in other words the variable 'name' is the object of the class 'string' at the most basic level.
- It allows developers to develop applications using the OOPs approach with a major focus on code reusability.
- Object-oriented programming is an approach for modeling concrete, real-world things, and relations between those things.
- OOP models real-world entities as programming objects that have some data associated with them and can perform certain functions.

The 4 Pillars of OOP:
Abstraction - It means to abstract only the details/data which might concern the user. The developer let the user abstract only the details that are required, the rest is hidden.
Encapsulation - It tries to encapsulate all the data as a single entity. Similarly a black box, where an input is passed, the box processes it and gives the result as an output
from the other end, therefore what happens in the black box is totally hidden. Encapsulation also hides the data.
Inheritance - A class can inherit various characteristics and capabilities from another class. It supports the concept of reusability, when a new a feature includes part from an
existing code, it can be derived from the existing one instead of developing from scratch.
Polymorphism - This word means "having many forms", so polymorphism is the ability of something to have more than one form. In programming, an operation may exhibit different behaviors
in different instances, these behaviors will depend upon the types of data used in the operation.

Building Blocks of OOP:
- Classes and Objects are the building blocks of the object-oriented system.
- Abstraction, Encapsulation, Inheritance, Polymorphism combined with Classes and Objects make an object-oriented program.

Classes:
- Like lists, tuples, dictionaries... Classes are advanced data structures to store, manipulate, and structure the data.
- Differently from lists, tuples, dictionaries and others data structures that can store only a few attributes, Classes is a type of user-defined structure that can store various attributes,
(Data - both primitive and user-defined) along with their functionalities, all together as a single unit.
- These attributes and their functionalities(behaviors) can be accessed via Objects.

Definition of a Class in OOP: "Blueprint to create objects."
- It's a user-defined prototype for an object that defines the set of attributes that characterize any object of the class.
- It's just like a prototype depending on which the real-world objects are created.
- An analogy: when a building is being planned to be created, the first to do is to create a blueprint of how the building would be. Depending upon that blueprint, real-world building structures
would be created that would be that same but with different attributes and functionalites such as colors, windows, interior, etc. At the most basic level, the base structure would be the same as
defined in the blueprint.

Objects:
- They are called as an instance of the class.
- An object contains two trings: Attributes(Data variables of the class) and Behaviors(Functions defined in the class).

Example:
- If the building is a class, therefore color, floors, flats, entrance, etc, would be the attributes, and isFinished(), isBusy(), flatAvailable(), etc would be its be behaviors that are the methods.
Each building would have all these data and behaviors and unique to themselves.

Defining a Class: Syntax
class className:
    #body of the class
- 'class' is the keyword used to define a class in Python.
- className is the name given to the class. It's similar to giving a name to a variable or a function, so it's important to choose a meaningful name.
- It's terminated with a semicolon.
- Inside the class, the attributes, the functions and the body of the class must be defined and indented.
'''

# Creating an Employee Class
class Employee:
    pass
 
 # The "pass" is just like a temporary placeholder until we add the required functionalities. The pass statement will be ignored by the Python interpreter and can be seen as a null statement.
 # Nothing will be returned in the output since at the moment the class is empty.

class Employee:
    empName = 'John'
    age = 30
    designation = 'Manager'

# It won't return any output considering that a class is just the description.
# It's necessary to create an object to access the attributes

'''
Declaring an Object: Syntax
objName = className()
- After it, it's possible to access the attributes and methods using the following syntax:
objName.attributeName
objName.methodName()
'''

# Creating an object of Employee Class
empOne = Employee()
print(empOne.empName, empOne.age, empOne.designation)

empTwo = Employee()
print(empTwo.empName, empTwo.age, empTwo.designation)

'''
Each object is a unique instance of the class and has its own attributes and behaviors, however the example above doesn't confirm it, because the attributes of the class Employee are quite rigid
so they return the same attributes and data for all the objects.
''' 