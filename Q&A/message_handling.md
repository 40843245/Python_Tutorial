# message handling in Python
## Q1: Exception handling.
## A1:
### Way 1:
With try-except block. Such as 

    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


## Ref
Visit Python docs.

https://docs.python.org/3/tutorial/errors.html

## Q2: Ignore display warning at runtime.
## A2:
### Way 1: In Python code
In python, one can import warnings module.

    import warnings
    
Then one can simply filter the warnings.

    warnings.filterwarnings('ignore')

### Way 2: In terminal in Windows
In Windows 11, in terminal, one can use -W options. Such as

    python -W ignore foo.py

## Ref
From stackoverflow,

https://stackoverflow.com/questions/14463277/how-to-disable-python-warnings

About warnings module, visit Python Docs,

https://docs.python.org/3/library/warnings.html


