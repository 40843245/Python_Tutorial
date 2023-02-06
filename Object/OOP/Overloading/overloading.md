# Overloading
## What is overloading in programming language?

Overloading refers something (functions,operators,even classes) with same name are used in many different situations.

### Function Overloading
Function Overloading refers two functions are declared with same name 

BUT these statements can NOT be all true.

1. Their number of arguments of functions.

2. Types of them are same for each corresponding arguments.

The constraints comes from prevention of ambiguity.

Functions declarations that causes ambiguity are NOT allowed in programming language.

When there exist functions declarations that causes ambiguity, we have the compiler-errors or run-time errors.

### Operator Overloading

Operator Overloading refers declare the behaviour to an existing operators for different use.

Such as

In C++, one can declare the behaviour of the operator + in the classes which have been declared.

But there are some details we have to care about.

Behaviour of operators may be changed when the behaviour of one or many other functions or operators is changed.

Some examples that behaviour of operators IS ALWAYS changed when the behaviour of one or many other functions or operators is changed.

1. In C/C++, arithmetic assigment operators.

About the arithmetic assignment operators in C/C++, we have that 

x <op> =y is equivalent to x=x <op> y 

  where <op> is one of arithmetic assignment operators +,-,*,/,%.
  
 If the operator <op> is overloaded , then the corresponding assigment operator <op>= will also be overloaded.
 
 For example, 
  
 We overload the operator + for class namely "classA".
 
 Then += for "classA" will be overloaded.
  
 The reason why is the C/C++ compiler consider the statement 
 
  x<op>=y 
 
 as 

  x = x <op> y
    
Some examples that behaviour of operators NEVER be changed when the behaviour of one or many other functions or operators is changed.
  
1. In C/C++, comparison operators.
  
 For all comparison operators <comp_op>,
  
 if the operator <comp_op> is overloaded , then the corresponding assigment operator <comp_op>= and its negation will NEVER be overloaded.
  
  For example, 
  
 We overload the operator == for class namely "classA".
 
 Then != for "classA" will be overloaded.
  
 The reason why is the C/C++ compiler consider 
  
  == 
  
 and
  
  !=
  
independently.

## Ref

For function overloading,
  
  https://www.geeksforgeeks.org/does-c-support-function-overloading/
  
For operator overloading,
  
  https://en.wikipedia.org/wiki/Operators_in_C_and_C%2B%2B

