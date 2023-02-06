# Data hidden
## What is data hidden in Python?
Generally, we have to declare attributes of the class in __init__() method.

But for more convenience of use, one can hide the attributes in the class.

The technique to hide the attributes in the class is called data hidden in class.

The concept is like that

we declare a global variable. Thus, we don't have to pass the variable as argument every time we call the function.

## NOTE
NOTE that 
1. There is a difference between declaration variables with data hidden and declaration global variables in the class.

Variables with data hidden are private which indicates we can NOT use it outside of the class.

Variables with the reserved word "global" are public so that we can use it outside of the class.



## Example
### Example Code
Consider the following code.

class MyClass:

	# Hidden member of MyClass
  
	__hiddenVariable = 0
	
	# A member method that changes
  
	# __hiddenVariable
  
	def add(self, increment):
  
		self.__hiddenVariable += increment
    
		print (self.__hiddenVariable)

# Driver code

myObject = MyClass()	

myObject.add(2)

myObject.add(5)

# This line causes error

print (myObject.__hiddenVariable)



