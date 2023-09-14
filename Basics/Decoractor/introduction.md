# Decorator in Python
## Objectives
    1. Simple introduce convience syntax -- decorator.
    2. Why does it invented?
    3. Symbol of decorator
    4. Give references for more advanced learning about decorator (shown in Ref section or Advanced Reading section)
## Prequisite
Before reading this article, you must be familiar with some basics about Python. Such as 

    1. function
    2. class 
    3. static method in class
    4. object

These are basic for any programming language. Therefore, I will discuss them in this article.

If you forget them or are not familiar with them, I high recommend you to visit python official docs before reading this article.

## Introduction to Decorator

For quick understanding, take a quick glance at the following first pair.
### Pair
#### Pair 1
##### Code 1
    class BaseClass:
        def BaseFunc1(
                self
        ):
            return "BaseFunc1"
    
    def GetInfo(
            obj
        ):
        return [obj,type(obj)]
    if __name__ == '__main__':
        
    print("-"*20)
        print(GetInfo(BaseClass().BaseFunc1()))
    
        inst = BaseClass()
        print("-"*20)
        print(GetInfo(inst.BaseFunc1()))
        
        print("-"*20)
        print(GetInfo(BaseClass().BaseFunc1))
        
        print("~"*20)
        print(GetInfo(BaseClass.BaseFunc1))
        
        staticMethod1 = staticmethod(BaseClass().BaseFunc1)   
        print("-"*20)
        print(GetInfo(staticMethod1))
        print(GetInfo(staticMethod1()))
        
        print("~"*20)
        print(GetInfo(BaseClass().BaseFunc1()))
        
        print()
        
        inst = BaseClass()
        print("-"*20)
        print(GetInfo(inst.BaseFunc1()))
        
        print("-"*20)
        print(GetInfo(BaseClass().BaseFunc1))
        
        print("-"*20)
        print(GetInfo(BaseClass.BaseFunc1))
##### Output

    --------------------
    ['BaseFunc1', <class 'str'>]
    --------------------
    ['BaseFunc1', <class 'str'>]
    --------------------
    [<bound method BaseClass.BaseFunc1 of <__main__.BaseClass object at 0x00000179E8201950>>, <class 'method'>]
    ~~~~~~~~~~~~~~~~~~~~
    [<function BaseClass.BaseFunc1 at 0x00000179E81C54E0>, <class 'function'>]
    --------------------
    [<staticmethod(<bound method BaseClass.BaseFunc1 of <__main__.BaseClass object at 0x00000179E8201C10>>)>, <class 'staticmethod'>]
    ['BaseFunc1', <class 'str'>]
    ~~~~~~~~~~~~~~~~~~~~
    ['BaseFunc1', <class 'str'>]
    
    --------------------
    ['BaseFunc1', <class 'str'>]
    --------------------
    [<bound method BaseClass.BaseFunc1 of <__main__.BaseClass object at 0x00000179E8201B50>>, <class 'method'>]
    --------------------
    [<function BaseClass.BaseFunc1 at 0x00000179E81C54E0>, <class 'function'>]
    
###### Explanation
In Pair 1, Code 1 section, we can easily know that BaseFunc1 is a non-static method in BaseClass.

Thus, we can and must instantiate an object with class BaseClass before calling the BaseFunc1.

However, we can make BaseFunc1 as a static method by the keyword staticmethod. 

Here we pass BaseClass().BaseFunc1 as argument in the keyword staticmethod to make BaseClass().BaseFunc1() as a static method and store it into the variable staticMethod1.

Therefore, staticMethod1 is a static method. But it will still get a non-static method on BaseClass().BaseFunc1 (even after I assign the statement). 
        
        staticMethod1 = staticmethod(BaseClass().BaseFunc1) 

The reason why it occurs is about the simple facts.

    The keyword staticmethod is NOT in-place in Python. That is, calling staticmethod in the above statement will NOT change the BaseClass().BaseFunc1 .


###### NOTICE
If we look it carefully, we will find that the address of staticmethod is NOT same as BaseClass.BaseFunc1. 

And the first call of BaseClass.BaseFunc1 (before making it static method) and second call of BaseClass.BaseFunc1 (after making it static method) have same address.

##### Code 2

    class BaseClass:
        def BaseFunc1(
        ):
            return "BaseFunc1"

    def GetInfo(
            obj
        ):
        return [obj,type(obj)]
    if __name__ == '__main__':
    
        print("-"*20)
        print(GetInfo(BaseClass().BaseFunc1) ) 
        
        staticMethod1 = staticmethod(BaseClass.BaseFunc1)
        print("~"*20)
        print(GetInfo(staticMethod1))
        print(GetInfo(staticMethod1()))
        
        print("~"*20)
        print(GetInfo(BaseClass().BaseFunc1) 

###### Output
    --------------------
    [<bound method BaseClass.BaseFunc1 of <__main__.BaseClass object at 0x000001BE641E1850>>, <class 'method'>]
    ~~~~~~~~~~~~~~~~~~~~
    [<staticmethod(<function BaseClass.BaseFunc1 at 0x000001BE641A54E0>)>, <class 'staticmethod'>]
    ['BaseFunc1', <class 'str'>]
    ~~~~~~~~~~~~~~~~~~~~
    [<bound method BaseClass.BaseFunc1 of <__main__.BaseClass object at 0x000001BE63F47690>>, <class 'method'>

##### Code 3

    class BaseClass:
        def BaseFunc1(
        ):
            return "BaseFunc1"

    def GetInfo(
            obj
        ):
        return [obj,type(obj)]
    if __name__ == '__main__':
    
        print("-"*20)
        print(GetInfo(BaseClass().BaseFunc1) ) 
        
        staticMethod1 = staticmethod(BaseClass.BaseFunc1)
        print("~"*20)
        print(GetInfo(staticMethod1))
        print(GetInfo(staticMethod1()))
        
        print("~"*20)
        print(GetInfo(BaseClass().BaseFunc1) ) 
        
        print("-"*20)
        print(GetInfo(BaseClass().BaseFunc1()) ) 


###### Output
A runtime error occurs.

    --------------------
    [<bound method BaseClass.BaseFunc1 of <__main__.BaseClass object at 0x00000201FD61D390>>, <class 'method'>]
    ~~~~~~~~~~~~~~~~~~~~
    [<staticmethod(<function BaseClass.BaseFunc1 at 0x00000201FD6214E0>)>, <class 'staticmethod'>]
    ['BaseFunc1', <class 'str'>]
    ~~~~~~~~~~~~~~~~~~~~
    [<bound method BaseClass.BaseFunc1 of <__main__.BaseClass object at 0x00000201FD61D5D0>>, <class 'method'>]
    --------------------
    Traceback (most recent call last):
    
      File C:\ProgramData\anaconda3\Lib\site-packages\spyder_kernels\py3compat.py:356 in compat_exec
        exec(code, globals, locals)
    
      File c:\users\40843\utility\classparser\untitled6.py:24
        print(GetInfo(BaseClass().BaseFunc1()) )
    
    TypeError: BaseClass.BaseFunc1() takes 0 positional arguments but 1 was given

###### Explanation
In Pair 1, Code 3 section, it throws a runtime error since for non-static method in BaseFunc1 it requires 1 arguments -- self 

(Don't ask me why. It's a feature of Python. I also want to know why (and I don't know why)). 

However, we just give 0 argument, causing a runtime error -- TypeError.

But, how about making BaseFunc1 as a static method?

Solved the issue. 

Since it is NOT a non-static method but a static method, we don't have an extra argument -- self .

However, to do that, we have to write 1 assignment. It is very troublesome, isn't it?

On the other hand, we always to use staticMethod1. We can NOT use BaseClass().BaseFunc1. (Even after making it as a static method through this approach. Why? I have already discussed it. I am lazy to do so.) For most people, one usually forget (or almost forget) the fact, doesn't one?

Fortunately, we can use decorator to avoid two defects.

For more details, see the next Code.

##### Code 4
        import types
            def GetInfo(
                    obj
                ):
                return [obj,type(obj)]
            
            class A:
                def f(self):
                    return 'this is f'
                @staticmethod
                def g():
                    return 'this is g'
        a = A()
        print(GetInfo(a.g))
        print(GetInfo(a.f))
        print(GetInfo(isinstance(a.g, types.FunctionType)))
        print(GetInfo(isinstance(a.f, types.FunctionType)))
        
###### Output

        [<function A.g at 0x0000020642091620>, <class 'function'>]
        [<bound method A.f of <__main__.A object at 0x000002064208EF90>>, <class 'method'>]
        [True, <class 'bool'>]
        [False, <class 'bool'>]
###### Explanation

By the output of Pair 1, Code 4, we can know the a method with attribute staticmethod will be a static method (If we don't mark it then it would be a non-static method).

A.f is a non-static method

A.g is a static method.

It is approaches better than the above approach in Pair 1, Code 3 section, isn't it?

### What is decorator?
Decorator is a symbol to mark the attribute to a method in class or function. 

As above codes in Pair 1, we don't have to write an extra statement, taking less work.

## Syntax
They are roughly equivalent.

    @f1(arg)
    @f2
    class Foo: pass

and 

    class Foo: pass
    Foo = f1(arg)(f2(Foo))

However, it is more restrictive before PEP 614
For more details about relaxing decorator in PEP 614, see 

https://peps.python.org/pep-0614/

## Symbol 
There are many ways to represent decorator. The most common way to do it is add a symbol at front of the keyword def. Shown in above codes.

In history, there are many different ways. However, due to historical reason ( really? really!!! ) and convenience, the other symbol than @ is deprecated.

I can NOT ensure that they will be removed in the future.

Thus, I high recommend to use symbol @.

## My Speech
I remember that I have posted an article about some common decorator in Python in the account. 

I will offer the link in this artcile in the future (if I have chance to do so).

It's in night. Good night, everyone. (In fact, I want to finish reading an article about enclosing in Python)

## Ref
Python Official Docs:

https://docs.python.org/3/glossary.html#term-decorator

https://docs.python.org/3/reference/compound_stmts.html#function

https://docs.python.org/3/reference/compound_stmts.html#class

https://peps.python.org/pep-0614/
