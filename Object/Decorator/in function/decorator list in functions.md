# Decorator List in functions
In this article, I will list some commonly used decorators for functions and its meaning.

# List
1. accepts
2. returns
3. onexit

# NOTICE


# Meaning
1. accepts:

  To determine which type of parameters can be accepted.
  
  Example Code (from the link https://peps.python.org/pep-0318/#warningwarningwarning):
  
  def accepts(*types):
  
    def check_accepts(f):
    
        assert len(types) == f.func_code.co_argcount
        
        def new_f(*args, **kwds):
        
            for (a, t) in zip(args, types):
            
                assert isinstance(a, t), \
                
                       "arg %r does not match %s" % (a,t)
                       
            return f(*args, **kwds)
            
        new_f.func_name = f.func_name
        
        return new_f
        
    return check_accepts

def returns(rtype):

    def check_returns(f):
    
        def new_f(*args, **kwds):
        
            result = f(*args, **kwds)
            
            assert isinstance(result, rtype), \
            
                   "return value %r does not match %s" % (result,rtype)
            return result
        new_f.func_name = f.func_name
        return new_f
    return check_returns

@accepts(int, (int,float))

@returns((int,float))

def func(arg1, arg2):

    return arg1 * arg2

2. returns:

  To determine which type of returned value.
  
  Same example Code as above.

3. onexit:
 
 Indicate the function to be a callback function which be executed iff the program is ready to exit.
 
 i.e. Before the program exits, the function which is marked by @onexit will be executed.
 
 Example Code (from the link https://peps.python.org/pep-0318/#warningwarningwarning):
 
 def onexit(f):
 
    import atexit
    
    atexit.register(f)
    
    return f

@onexit

def func():

    ...
 
## Ref
https://peps.python.org/pep-0318/#warningwarningwarning
