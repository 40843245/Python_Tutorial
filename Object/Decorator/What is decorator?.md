# Decorator
## Symbol
@

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

Although there are many ways to use decorator, 

I will introduce the most commonly used and must be accepted in any Python 3.x compiler at present.

@ way.

Just insert @ and its reserved function name and its argument before functions or methods or attributes or classes.

Other ways on the "Syntax form" section of the following link.

https://peps.python.org/pep-0318/#warningwarningwarning

### NOTE 
NOTE that I'm NOT sure other way than @ way can be accepted in Python compilers. 

I haven't tried them before, even if I haven't  heard them before.

## Equivalence syntax and its intro

They are equivalent.

  @<builtin_identifiers>

and
  
  <builtin_identifiers>()
  
  where <builtin_identifiers> is any built-in functions that used to mark something.
  
  

## Equivalence sample.

They are equivalent.

  @dec2
  @dec1
  
  def func(arg1, arg2, ...):
  
      pass
  
and 
  
  def func(arg1, arg2, ...):
  
    pass
    
  func = dec2(dec1(func))
  
They are equivalent.
  
  @decomaker(argA, argB, ...)
  
  def func(arg1, arg2, ...):
  
    pass
    
   func = decomaker(argA, argB, ...)(func)
   
## NOTICE
  
  NOTE that the () is NOT needed and can NOT be used when decorator is used.
  
  Except that a function with many ()s when NOT use decorators.
    
  When we call a function, we have to add () at the end of identifiers. 
  
  However, when we use the decorator, the () after identifiers has to be removed.
  
  
Example above.

## Desgining Goal:

See the "Design Goal section" of the following link.

https://peps.python.org/pep-0318/#warningwarningwarning

## Ref:

1. Simply intro to decorators.

https://www.geeksforgeeks.org/decorators-in-python/


2. Search results by the keyword decorator in python.org .

https://www.python.org/search/?q=Decorator&submit=


3. Intro to decorator.

https://peps.python.org/pep-0318/#warningwarningwarning

