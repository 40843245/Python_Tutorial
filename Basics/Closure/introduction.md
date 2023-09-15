# Closure in Python
## Objectives
I will discuss these topics in this artcile.

    1. What is closure?
    2. Application about closure in Python.
    3. How to use closure in Python.

## Prequisite
    
    1. function (including default value in function)
    2. class
    3. object

## Code
### Code 1
    
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

### Explanation
We can easily know the fact that the attribute return_default can make a function to return default value when the func does NOT return value.

In the func call of x = at_least_10(3) .

The return statement does NOT be executed. Thus, it will return default value. Here, it will return 10.

Without return_default attribute marked, the default value for return is None.

In the func call of msg = greeting(None) .

The return statement does NOT be executed. Thus, it will return default value. Here, it will return "python".



## Ref

https://dboyliao.medium.com/%E8%81%8A%E8%81%8A-python-closure-ebd63ff0146f
