# Helper Function -- help ()
## What are helper functions?
Helper functions are a kind of utilities to print message for help.

Here we call the message as "help message".
## How to call a help function?
In Python 3 above, type the statement.

help(<object-name>)
  
where <object-name> is the object for help.

The above statement prints the help message of <object-name> in the console.

## How to write help messages?(i.e.How to determine what help messages are displayed in the console?)
In the class definition or function definition, we simply add a double-quoted string at the beginning, making the string as help message.
  
If one wants to the help message is written in single line, one just have to add a double-quote before and after the help message.
 
If one wants to the help message is written in multiple line, one just have to add three double-quote before and after the help message.
  
The reason is about the multiple string representation.

Recall that the fact.

The string which is written in many line must be quotated with three double-quote.
 
Such as the following example code.
  
s="""
  
abc
  
def
  
"""
  
