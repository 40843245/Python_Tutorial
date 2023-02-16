# What is difference between Python 2 and Python 3?
## Ref:
https://docs.python.org/3/howto/pyporting.html

## Ans:
From the above website (website of python docs), I notice there are slightly BUT MORE differences between Python 2 and Python 3.

If you don't care about it, the slightly difference may cause unexpected result and make you crazy, discouraging you to develop with Python.

In this article, I will talk the main differences.

As for these details and the history of changes, see the above website. The above website gives detailed explanation. 

To save your time, I will list these main differences.

1) Division operator.

Before Python 2.7, 

    5/2 will be 2.
    
 BUT in Python 2.7 after Python 2.7,
 
    5/2 will be 2.5
    
 It has changed in Python 2.7 since 2002.
 
 Before performing the division operation between integers, these integer will be converted into float type (even though the numerator and denominator of the fraction 
 
 are both integer type). 
 
2) Text v.s. binary 

In Python 2, 

     you don't have to worried about the issue when using str for both text and binary data.
     
However, in Python 3. It may cause exceptions or unexpected results if 

    you mix these data (text and binary data).
    
For convenience, I really recommend you that you DON't handle both text and binary data at same project when design API.

3) Issues about package and modules compatibility.

Some packages can be used in Python 2 but can NOT be used in Python 3.

Similarly, some packages can be used in Python 3 but can NOT be used in Python 2.

For example,

    1) importlib2 v.s. importlib
    
    importlib2 is used for Python 2. While importlib is used for Python 3.
    
    2) urllib v.s. urllib3
    
    urllib is used for Python 2. While urllib3 is used for Python 3.
    
    
