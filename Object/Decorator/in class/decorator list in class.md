# Decorator List
I will list commonly used decorator and its meaning.

## List

1. staticmethod
2. property
3. classmethod
4. singleton
5. attrs
6. provides

## NOTICE

All these examples of the following link are possible today, though without syntactic support.

https://peps.python.org/pep-0318/#warningwarningwarning

## Meaning

1. staticmethod:

Make the method of the class is static.

A static method can NOT be used in instantianted object.

You can google it for more details.

2. property:

Mark the method readonly.

Readonly refers it can be read, it can NOT be written.

3. classmethod:

 Return a class method for the given function.

4. singleton:
 
 When the class is marked as @singleton, the class is a singleton class.
 
 Example Code (from the link https://peps.python.org/pep-0318/#warningwarningwarning):
 
 def singleton(cls):
 
    instances = {}
    
    def getinstance():
    
        if cls not in instances:
        
            instances[cls] = cls()
            
        return instances[cls]
        
    return getinstance

@singleton

class MyClass:
     ...

5. attrs:

  Add attributes to the function.
  
  (Based on an example posted by Anders Munch on python-dev.)
  
  Exmaple code (from the link https://peps.python.org/pep-0318/#warningwarningwarning):
  
  def attrs(**kwds):
  
    def decorate(f):
    
        for k in kwds:
        
            setattr(f, k, kwds[k])
            
        return f
        
    return decorate

@attrs(versionadded="2.2",

       author="Guido van Rossum")
       
def mymethod(f):

  ...
  
6. provides:
  
  
  Example Code (from the link https://peps.python.org/pep-0318/#warningwarningwarning):
  
  def provides(*interfaces):
  
     """
     
     An actual, working, implementation of provides for
     the current implementation of PyProtocols.  Not
     particularly important for the PEP text.
     
     """
     
     def provides(typ):
     
         declareImplementation(typ, instancesProvide=interfaces)
         
         return typ
         
     return provides
     

class IBar(Interface):

     """Declare something about IBar here"""

@provides(IBar)

class Foo(object):

        """Implement something here..."""
        

## Ref
0. For all:
https://docs.python.org/3/howto/descriptor.html#descriptorhowto

https://peps.python.org/pep-0318/#warningwarningwarning

3. For classmethod:
https://www.geeksforgeeks.org/classmethod-in-python/


