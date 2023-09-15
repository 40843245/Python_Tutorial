# First-Class citizen in programming language
## Introduction
A First-Class function is a function that can treat a function as an object.

It has these features.

    1. Ability to treat functions as values.

    2. Ability to pass a function as arguments.

    3. Ability to return a function from another function.

## Detailed explanations for features in Python.
1. Ability to treat functions as values:

For example:

    lambdaFunc1 = lambda x : ( x + 5 )

2. Ability to pass a function as arguments:

For example:

    def Greet(msg):
      print(msg)
    def Message():
      return "Message"
    def Sentence():
      return "Sentence"

    Greet(Message)
    Greet(Sentence)
    
3. Ability to return a function from another function:

For example:

    def Func1():
        return "Func1"

    def Func2():
        return "Hello World" + " This is a function named: " + Func1() 
        
    Func2()

## Ref
A simple introduction.

https://www.geeksforgeeks.org/what-is-first-class-citizen-in-javascript/

## Advance Reading
https://en.wikipedia.org/wiki/First-class_citizen

https://stackoverflow.com/questions/5178068/what-is-a-first-class-citizen-function
