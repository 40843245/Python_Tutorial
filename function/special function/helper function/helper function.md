# Helper Function in Python -- help ()
## What are helper functions?
Helper functions are a kind of utilities to print message for help.

Here we call the message as "help message".
## How to call a help function?
In Python 3 above, type the statement.

help(<object-name>)
  
where <object-name> is the object for help.

The above statement prints the help message of <object-name> in the console.

## How to write help messages?(i.e.How to determine what help messages are displayed in the console?)
In the class definition or function definition, we simply add a double-quoted string at the beginning, making the string as help message.
  
If one wants to the help message is written in single line, one just have to add a double-quote before and after the help message.
 
If one wants to the help message is written in multiple line, one just have to add three double-quote before and after the help message.
  
The reason is about the multiple string representation.

Recall that the fact.

The string which is written in many line must be quotated with three double-quote.
 
Such as the following example code.
  
s="""
  
abc
  
def
  
"""
  
## NOTICE
 1. The help() displays the help message instead of returning a string object, 
  
  so we don't have to use the print statement to display the help message.
 
 2. The help() returns a NonType object insteas of a string object, 
  
  so if we use the print statement as the following statement, None will be displayed in console.
  
  And the type of the returning object is NoneType.
  
  More details on the following example.
  
  x=help(<object-name>)
  
  print(x) # Output: None
  
  print(type(x)) # Output: <class 'NoneType'>
  
  
  
  
## Example
NOTE that I run the Python code in Spyder of Anaconda Navigator.

### Example 1
#### Example Code
  
def find_name_in_mro(cls, name, default):
  
    ## message in help function
  
    "Emulate _PyType_Lookup() in Objects/typeobject.c"
  
    for base in cls.__mro__:
  
        if name in vars(base):
  
            return vars(base)[name]
  
    return default

def object_getattribute(obj, name):
  
    ## message in help function
  
    "Emulate PyObject_GenericGetAttr() in Objects/object.c"
  
    null = object()
  
    objtype = type(obj)
  
    cls_var = find_name_in_mro(objtype, name, null)
  
    descr_get = getattr(type(cls_var), '__get__', null)
  
    if descr_get is not null:
  
        if (hasattr(type(cls_var), '__set__') or hasattr(type(cls_var), '__delete__')):
  
            return descr_get(cls_var, obj, objtype)     # data descriptor
  
    if hasattr(obj, '__dict__') and name in vars(obj):
  
        return vars(obj)[name]                          # instance variable
  
    if descr_get is not null:
  
        return descr_get(cls_var, obj, objtype)         # non-data descriptor
  
    if cls_var is not null:
  
        return cls_var                                  # class variable
  
    raise AttributeError(name)
    
class DirtyWord:
  
  def __init__(self,l=None):
  
    self.dirty_word=l if l!= None else []
    
  def Is_DirtyWord(self,word):
  
    tf=True if word in self.dirty_word else False
    
    print(tf)
        
o=DirtyWord()
  
result=object_getattribute(o,"Is_DirtyWord")
  
print(result)
  
x=help(object_getattribute)
  
print(x)
  
print(type(x))
  
#### Example Output In Console

<bound method DirtyWord.Is_DirtyWord of <__main__.DirtyWord object at 0x00000291CA5700A0>>
  
Help on function object_getattribute in module __main__:

object_getattribute(obj, name)
  
    Emulate PyObject_GenericGetAttr() in Objects/object.c

None
  
<class 'NoneType'>

##Example 2
### Example Code
  

def object_getattribute(obj, name):
    
    ## message in help function
    
    """
    
    Emulate PyObject_GenericGetAttr() in Objects/object.c
    
    1111111111111111111111111111
    
    aaaaaaaaaaaaaaaaaaaaaaaaaaaa
    
    """
    
    null = object()
    
    objtype = type(obj)
    
    cls_var = find_name_in_mro(objtype, name, null)
    
class DirtyWord:

  def __init__(self,l=None):
  
    self.dirty_word=l if l!= None else []
  
  def Is_DirtyWord(self,word):
  
    tf=True if word in self.dirty_word else False
    
    print(tf)
        
o=DirtyWord()
  
result=object_getattribute(o,"Is_DirtyWord")
  
print(result)
  
x=help(object_getattribute)
  
print(x)
  
print(type(x))

### Example Output In Console
<bound method DirtyWord.Is_DirtyWord of <__main__.DirtyWord object at 0x00000291C909C100>>

Help on function object_getattribute in module __main__:

object_getattribute(obj, name)

    Emulate PyObject_GenericGetAttr() in Objects/object.c
    
    1111111111111111111111111111
    
    aaaaaaaaaaaaaaaaaaaaaaaaaaaa

None
  
<class 'NoneType'>

## Example 3
### Example Code
  def object_getattribute(obj, name):
    
    ## message in help function

    null = object()
    
    objtype = type(obj)
    
    """
    
    Emulate PyObject_GenericGetAttr() in Objects/object.c
    
    """
    
  
x=help(object_getattribute)
  
print(x)
  
print(type(x))
  
## Example Output In Console

None
  
Help on function object_getattribute in module __main__:

object_getattribute(obj, name)

None
  
<class 'NoneType'>
