# callable(object) v.s. object.__call__
# callable(object)
As the Python docs says 

A callable is an object that can be called, possibly with a set of arguments (see argument).

A function, and by extension a method, is a callable. An instance of a class that implements the __call__() method is also a callable.

## NOTE 
By the article from geeksforgeeks, note that 

If it returns False, then it is NOT allowed to invoke the object as object()

That is object() will cause runtime error. 

If it returns True, then it may NOT be allowed to invoke the object as object().

It just takes a chance to be allowed.

As the following example.
  
    class Geek:
        def testFunc(self):
            print('Hello GeeksforGeeks')


    print(callable(Geek))
    print(Geek.__call__)
    GeekObject = Geek()

    GeekObject()


## Ref

https://www.geeksforgeeks.org/callable-in-python/

https://docs.python.org/3/glossary.html#term-callable
