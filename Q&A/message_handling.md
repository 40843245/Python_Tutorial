# message handling in Python
## Q1: Ignore display warning at runtime.
## A1:
### Way 1: In Python code
In python, one can import warnings module.

    import warnings
    
Then one can simply filter the warnings.

    warnings.filterwarnings('ignore')

### Way 2: In terminal in Windows
In Windows 11, in terminal, one can use -W options. Such as

    python -W ignore foo.py

## Ref
https://stackoverflow.com/questions/14463277/how-to-disable-python-warnings



