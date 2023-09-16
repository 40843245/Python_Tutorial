# Assignment in Python
## Preface
It is very simple for me. Thus, I will simple to introduce it.
## Symbol
1. =

Note that it can NOT be used as an expression in lambda function. Otherwise, syntax error occurs. For example,

    lambda x : (
        print("Hello") , 
        y = x + 2 # Error
    )

will cause a syntax error. 

For the above example, use := instead.

    lambda x : (
        print("Hello") , 
        y := x + 2 # No Error for >= Python 3.8
    )
  
2. :=

Note that there can NOT be anything ( including whitespace or tab ) between : and = .

Also note that it is only supported >= Python 3.8 . 

Examples with syntax error.

    lambda x : (
        print("Hello") , 
        y : = x + 2 # Error
    )

Below Python 3.8 , the example will cause syntax error.

    lambda x : (
        print("Hello") , 
        y := x + 2 # Error for < Python 3.8
    )

For more details, see the link in Ref section.

## Ref

https://stackoverflow.com/questions/6282042/assignment-inside-lambda-expression-in-python
    
