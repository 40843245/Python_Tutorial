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

For quick understanding, take a quick glance at the following four pairs first. (Each pair has at least two equivalent pieces of code.)
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
    
