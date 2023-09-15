# Closure in Python
## Objectives
I will discuss these topics in this article.

    1. What is closure?
    2. Application about closure in Python.
    3. How to use closure in Python.
    4. Implementation of closure. "__closure__"
    5. Notes about  "__closure__".

## Prequisite
    
    1. function (including default value in function)
    2. class
    3. object
    
## Preface 
To quick understand about closure in Python, let's take a glance at several pieces of code and its explanation.

## Example
### Examples 1
#### Code
    def return_default(value):
        def deco(func):
            def wrapped(*args, **kwargs):
                ret = func(*args, **kwargs)
                if ret is None:
                    ret = value
                return ret
            return wrapped
        return deco
    
    @return_default(10)
    def at_least_10(x):
        if x >= 10:
            return x
    @return_default("python")
    def greeting(msg):
        return msg
    x = at_least_10(3) 
    print(x)
    msg = greeting(None)
    print(msg)
#### Output
    10
    python
### Example 2
#### Code
    def return_default(value):
        def deco(func):
            def wrapped(*args, **kwargs):
                ret = func(*args, **kwargs)
                if ret is None:
                    ret = value
                return ret
            return wrapped
        return deco
    
        @return_default(10)
        def at_least_10(x):
            if x >= 10:
                return x
    @return_default("python")
    def greeting(msg):
        return msg
    x = at_least_10(3) # 10
    msg = greeting(None) # "python"
    
    print(return_default(10).__closure__)
    
    print(return_default(10).__closure__[0].cell_contents)
    
    print(return_default("hello").__closure__[0].cell_contents)
#### Output
    (<cell at 0x00000210C8FB6950: int object at 0x00007FFF2E7E9448>,)
    10
    hello
### Explanation
We can easily know the fact that the attribute return_default can make a function to return default value when the func does NOT return value.

In the func call of x = at_least_10(3) .

The return statement does NOT be executed. Thus, it will return default value. Here, it will return 10.

Without return_default attribute marked, the default value for return is None.

In the func call of msg = greeting(None) .

The return statement does NOT be executed. Thus, it will return default value. Here, it will return "python".

In Code 2, we use the the following attribute to get the info of closure function in Python.
        
        __closure__ 

## Introduction to Closure
From wiki,

    a closure (also lexical closure or function closure) is a technique for implementing lexically scoped name binding in a language with first-class functions.

For most people, you will NOT understand the meaning of these terms. Let's give explanations of these terms.

### What is binding?
Roughly said, binding determines the value of variable when lookup (i.e.access). Such as when assignment 

    x = 3

and simple lookup value

    print(x)

### What is lexically binding?
According to EmacsWiki, each scope has one own variable lookup table. It is the feature of lexically binding.

### What is variable lookup table?
Variable lookup table is a table that stores the pair of variable and its value. 

Otherwise, how can we get the value of variable while accessing it? 

Without it, it is impossible. Isn't it? (I am NOT sure)

### LEGB
According to Python official docs (Python.org), in Python, when using a variable, it must follow the LEGB rule.

    L : Local
    E : Enclosing
    G : Global
    B : Builtin

Let's introduce L and G first.
    
    Local variable : Iff the variable is found in this scope when accessing , the variable is a local variable of this scope.

    Global variable : Otherwise, the variable is a gloabal variable of this scope.

Take the following code as example.

    glob = 3
    def func(x):
        y = x + glob
        def inner():
            return y + 1
        return inner, abs


In the scope inside "def func(x):", when accessing variable glob, the interpreter will try to find it out in this scope and NOT found. Thus, it will try to find it out in the outer scope (top-level scope) and is found. Hence, glob in the statement 
        
    y = x + glob
        
is a global variable of this scope.

In the scope inside "def func(x):", when accessing variable x, the interpreter will try to find it out in this scope and is found. It is declared as one agrument of definition of function -- func. Hence, x in the statement 
        
    y = x + glob

is a local variable of this scope.

In the scope inside "def inner():", when accessing variable y, the interpreter will try to find it out in this scope and NOT found. Thus, it will try to find it out in the outer scope ( scope inside definition of function -- func) and is found. Hence, y in the statement 
    
    return y + 1 

is a global variable of this scope.

Let's use the above example and introduce B.

In the above example. When accessing abs in the statement 

    return inner, abs

the interpreter will try to find it out in this scope and NOT found. Thus, it will try to find it out in the outer scope ( scope inside definition of function -- func) and NOT found. 

Next, it will try to find it out in top-level scope and NOT found.

Then it will try to find it out in built-in module and is found. 

Therefore, here, abs is a built-in function.

An important feature of built-in function is that 
    
    Before use it, we don't have to define it in this module or define it in other module then import it.

Lastly, let's introduce the C.

I copied and paste the wiki introduction again.

    a closure (also lexical closure or function closure) is a technique for implementing lexically scoped name binding in a language with first-class functions.

Simply said, 

    a function closure is a technique that implements a lexical binding in a scope. Such as use a function that is defined a inside a function which makes a nested funtion.

In above example, the statement 
        
        return inner, abs

returns two functions named inner and abs function. 

While function with name inner is user-defined in the func scope (inside a function definition with name func). 

When use inner variable, we DO use function closure.

## Application
### Why do we have to learn it?
One of reason is that for more convenience to write your own decorator. 
See Example 0 and Example 1.

## Implementation of closure in Python

    The attribute "__closure__".
    
    Data type of "__closure__" is a tuple. Thus, it is immutable. On the other hand, it is readonly.

## NOTES
I will ask several question.

    1. Does the attribute "__closure__" of the object is not None once it is defined as a non-local variable?

    NO!!! 
    
    It is created once nce it is accessed at first time. Before that, it is always None. 
    
    See Examples 3.

![image](https://github.com/40843245/Python_Tutorial/assets/75050655/9e8cdf2a-8926-43a7-a7df-b27d7fba9d9d)

    2. Is it true?
        
    When there are no free variable that explicitly defines in outer scope, __closure__ is always None?

    NO!!! Not necessary to be None.

    When inner scope uses a free variable, then it will implicitly define in outer scope.

    See Example 4.
    
## Examples
### Example 3
#### Code 
    def foo():
            a = 3
            def bar():
                print("bar")
            return bar
    y = foo()
    print(y.__closure__ is None)
#### Output
    True
### Example 4
#### Code 
    def foo():
        a = 3
        def bar():
            def hell():
                return a
            return hell
        return bar
    bar = foo()
    print(bar.__closure__ is None)
    print(bar.__closure__)
    print(bar().__closure__ == bar.__closure__)
    print(bar.__closure__[0].cell_contents)
#### Output
    False
    (<cell at 0x000001EC010B51E0: int object at 0x00007FFF2E7E9368>,)
    True
    3

![image](https://github.com/40843245/Python_Tutorial/assets/75050655/5178888c-237e-4b13-8490-d00f8b1b2e71)

## Ref

https://dboyliao.medium.com/%E8%81%8A%E8%81%8A-python-closure-ebd63ff0146f
