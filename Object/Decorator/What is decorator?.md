# Decorator
## What is a decorator in Python?
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

## Syntax

  @<built-in identifiers>

is equivalent to
  
  <built-in identifiers>()
  
  where <built-in identifiers> is any built-in functions that used to mark something.
  
## NOTICE
  
  NOTE that the () is NOT needed and can NOT be used when decorator is used. 
  
  Except that a function with many ()s when NOT use decorators.
    
  When we call a function, we have to add () at the end of identifiers. 
  
  However, when we use the decorator, the () after identifiers has to be removed.
  
  
Example above.

## Ref:

1. Simply intro to decorators.

https://www.geeksforgeeks.org/decorators-in-python/


2. Search results by the keyword decorator in python.org .

https://www.python.org/search/?q=Decorator&submit=


