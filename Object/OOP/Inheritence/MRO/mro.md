# MRO
## What is mro in inheritence of object?

It is the abbreviation of Multiple Resolution Order.

In Python, it is allowed to inherit many different classes.

Additionally, it is allowed for multiple-level inheritence.

(i.e. to inherit a class that inherits to other class.)

For a class, the order of the class inherits to is called 
MRO (Multiple Resolution Order).

MRO decides the priority the compilers find for a identifier when needed.

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

