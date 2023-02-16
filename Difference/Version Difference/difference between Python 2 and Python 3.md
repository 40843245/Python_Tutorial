# What is difference between Python 2 and Python 3?
## Ref:
https://docs.python.org/3/howto/pyporting.html

## Ans:
From the above website (website of python docs), I notice there are slightly BUT MORE differences between Python 2 and Python 3.

If you don't care about it, the slightly difference may cause unexpected result and make you crazy, discouraging you to develop with Python.

In this article, I will talk the main differences.

1) Division operator.

Before Python 2.7, 

    5/2 will be 2.
    
 BUT in Python 2.7 after Python 2.7,
 
    5/2 will be 2.5
    
 It has changed in Python 2.7 since 2002.
 
 Before performing the division operation between integers, these integer will be converted into float type (even though the numerator and denominator of the fraction 
 
 are both integer type). 
 
