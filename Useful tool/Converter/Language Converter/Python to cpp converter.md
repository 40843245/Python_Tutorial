# Some tools of Python to cpp converter
## Ref
https://www.javainuse.com/py2cpp

## Comment to this converter.
It's good.

I will score it 80.

It is NOT easily to convert Python 2 code to Python 3 code.

It is pity that
  
    1)It takes several minute to convert the example 1.
    
    2)The code is NOT complete, in example 1 it only forgets to add comment for cpp result.


## Example
### Example 1
#### Example Input 

### Example 1
#### Example Input 
class Quote_ENUM():
    singleQuote="'"
    
    pairSingleQuote=[singleQuote,singleQuote]
    
    doubleQuote='"'
    
    pairDoubleQuote=[doubleQuote,doubleQuote]
    
    #pair=[pairSingleQuote,pairDoubleQuote]
    
    #pair=[singleQuote,doubleQuote]
    
    singleQuoteL=[singleQuote]
    
    doubleQuoteL=[doubleQuote]
    
    
    pair=[singleQuoteL,doubleQuoteL]

#### Example Output

(incomplete)
    
    enum Quote_ENUM{
        singleQuote='\'',
        pairSingleQuote=[singleQuote,singleQuote],
        doubleQuote='"',
        pairDoubleQuote=[doubleQuote,doubleQuote],
        singleQuoteL=[singleQuote],
        doubleQuoteL=[doubleQuote],
        pair=[singleQuoteL,doubleQuoteL]
    };


### Example 2
#### Example Input 
a_string = "the quick brown fox jumps over the lazy dog. the quick brown fox jumps over the lazy dog"

# Find all indices of 'the'
indices = [index for index in range(len(a_string)) if a_string.startswith('the', index)]

print(indices)

# Returns: [0, 31, 45, 76]
#### Example Output
a_string = "the quick brown fox jumps over the lazy dog. the quick brown fox jumps over the lazy dog"

# Find all indices of 'the'
indices = [index for index in range(len(a_string)) if a_string.startswith('the', index)]

print(indices)

# Returns: [0, 31, 45, 76]
