# MRO
## What is mro in inheritence of object?

It is the abbreviation of Multiple Resolution Order.

In Python, it is allowed to inherit many different classes.

Additionally, it is allowed for multiple-level inheritence.

(i.e. to inherit a class that inherits to other class.)

For a class, the order of the class inherits to is called 
MRO (Multiple Resolution Order).

MRO decides the priority the compiler finds for a identifier when needed.

When the compiler finds for a identifier? 
When you use the identifier.

## How to get the MRO of a class?

In Python, you don't have to implement it

since there is a builit-in method and attribute in Python.

F.__mro__

and

F.mro()

To get a tuple type,

F.__mro__

To get a list type,

F.mro()

## Example
### Example 1
#### Example Code

class A:

	def rk(self):
  
		print(" In class A")
    
class B:

	def rk(self):
  
		print(" In class B")

# classes ordering

class C(A, B):

	def __init__(self):
  
		print("Constructor C")
        
class D(C):

    def __init__(self):
    
        print("Constructor D")
        
class E(B):

    def __init__(self):
    
        print("Constructor E")
        
class F(D,E):

    def __init__(self):
    
        print("Constructor F")
        
r = F()

# it prints the lookup order

print(F.__mro__) # return a list

print(F.mro())   # return a tuple

#### Example Output In Console
Constructor F

(<class '__main__.F'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.E'>, <class '__main__.B'>, <class 'object'>)

[<class '__main__.F'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.E'>, <class '__main__.B'>, <class 'object'>]

# Ref
https://www.geeksforgeeks.org/method-resolution-order-in-python-inheritance/

