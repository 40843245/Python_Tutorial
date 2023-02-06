# Decorator List in functions
In this article, I will list some commonly used decorators for functions and its meaning.

# List
1. accepts
2. returns
3. onexit

# Meaning
1. accepts:

  To determine which type of parameters can be accepted.

2. returns:

  To determine which type of returned value.

3. onexit:
 
 Indicate the function to be a callback function which be executed iff the program is ready to exit.
 
 i.e. Before the program exits, the function which is marked by @onexit will be executed.
 
## Ref
https://peps.python.org/pep-0318/#warningwarningwarning
