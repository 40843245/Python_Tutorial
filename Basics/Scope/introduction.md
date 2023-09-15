# Scope in Python
## Objectives
In this article, I will discuss

    1. What is scope.
    2. Create a scope in Python.
    3. Nested scope.
    4. Notes about scope.

## What is scope?
Simply said, scope of the variable can determine when the variable can NOT be used anymore.

Variables can be used in this scope of definition of variable.

Scope of the variable is like to a lifecycle of the variable.

Look at the following example.

    glob = 3
    def func(x):
        y = x + glob
        def inner():
            return y + 1
        return inner, abs

In the above example. there are 3 different scopes -- one is at top-level whose lifecycle is the whole code.

While the other one is inside function definition of func whose lifecycle ends at the statement "return inner, abs".

Lastly, the innermost one is inside function definition of func whose lifecycle ends at the statement "return y + 1".

The tree of scope heirarchy looks like this.

    top-level 
    \- func
       \- inner
       
## How to create scope in Python?
Once define a class, a method in class and a function, or use a keyboard such as while, match - case, we create a scope.

## Nested scope
Nested scope refer a scope inside other scope.

## NOTES about scope in Python
Although we can use for loop in Python such as 

    for i in range(10):
        pass
    print(i)

However, it does NOT create a scope for the keyword for.

Instead, the lazy binding is used. (It is out of topic. I may write an article in the future.)

In the above code, we will see "i == 9 " is True.
## Ref
https://dboyliao.medium.com/%E8%81%8A%E8%81%8A-python-closure-ebd63ff0146f

