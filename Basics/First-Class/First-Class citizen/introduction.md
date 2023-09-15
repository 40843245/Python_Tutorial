# First-Class citizen in programming language
## Introduction
From the GeeksForGeeks, 

https://www.geeksforgeeks.org/what-is-first-class-citizen-in-javascript/

I summarize a sentence and 3 features.

A First-Class function is a function that can treat a function as an object.

It has these features.

    1. Ability to treat functions as values.

    2. Ability to pass a function as arguments.

    3. Ability to return a function from another function.

### Detailed explanations for features in Python.
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

## Alias -- First-Class Object
According to Wiki,

https://en.wiktionary.org/wiki/first-class_citizen

it says that first-class citizen is a symonym of the term First-Class object.

I will introduce what is First-Class object in next section.

## First-Class Object

From a question whose title is " What are "first-class" objects? " in statckoverflow,

https://stackoverflow.com/questions/245192/what-are-first-class-objects

An user replies that

    A first class object is an entity that can be dynamically created, destroyed, passed to a function, returned as a value, and have all the rights as other variables in the programming language have.

According to the above definition. This can imply:

        being expressible as an anonymous literal value
        being storable in variables
        being storable in data structures
        having an intrinsic identity (independent of any given name)
        being comparable for equality with other entities
        being passable as a parameter to a procedure/function
        being returnable as the result of a procedure/function
        being constructible at runtime
        being printable
        being readable
        being transmissible among distributed processes
        being storable outside running processes
## Ref
A simple introduction.

https://www.geeksforgeeks.org/what-is-first-class-citizen-in-javascript/

A detailed explanation to First-Class object.

https://stackoverflow.com/questions/245192/what-are-first-class-objects

## Advance Reading
https://en.wikipedia.org/wiki/First-class_citizen

https://stackoverflow.com/questions/5178068/what-is-a-first-class-citizen-function
