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

If you forget them or are not familiar with them, I high recommend you to visit python official docs before reading this article.

## Introduction to Decorator

For quick understanding, take a quick glance at the following two pairs first. (Each pair has two equivalent pieces of code.)
### Pair
#### Pair 1
##### Code 1
    class BaseClass:
        def BaseFunc1():
            return "BaseFunc1"
##### Code 2
    
