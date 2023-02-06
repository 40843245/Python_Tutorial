# Decorator
## What is a decorator?
A decorator is a shorthand way to decorate and modify the functions, methods, attributes, or classes.

You can think of it is a shorthand to mark label with given built-in function word.

It saves lots of effort for development to decorate them.

Without decorator, we have to write a statement.

With decorator, we have to use the decorator symbol (i.e. @) and write the keyword for mark.

Such as 

class Operation:

  def add(x,y):
  
   return x+y
   
add=staticmethod(add)

is equivalent to

class Operation:

  @staticmethod
  
  def add(x,y):
  
   return x+y
   
add=staticmethod(add)

## Ref:

1. Simply intro to decorators.

https://www.geeksforgeeks.org/decorators-in-python/


2. Search results by the keyword decorator in python.org .

https://www.python.org/search/?q=Decorator&submit=


