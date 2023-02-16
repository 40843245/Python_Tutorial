# Some tools of Python version converter
## Ref
https://360techexplorer.com/tools/python-2-to-3-converter/

## Comment to this converter.
It's OK.

I will score it 60.

However, it is NOT easily to convert Python 2 code to Python 3 code.

Why I score it 60?

Since 
  
    1)The most important part is that it has NO identation. After clicking the "Convert" Button, the input and output will NOT idented.
    
    2)The API looks to ugly.


## Example
NOT identation!!!

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
import argparseparser = argparse.ArgumentParser(description='Command-line example.')# Add optional switchesparser.add_argument('-v', action='store_true', dest='is_verbose',                    help='produce verbose output')parser.add_argument('-o', action='store', dest='output',                    metavar='FILE',                    help='direct output to FILE instead of stdout')parser.add_argument('-C', action='store', type=int, dest='context',                    metavar='NUM', default=0,                    help='display NUM lines of added context')# Allow any number of additional arguments.parser.add_argument(nargs='*', action='store', dest='inputs',                    help='input filenames (default is stdin)')args = parser.parse_args()print args.__dict__
#### Example Output
import argparseparser = argparse.ArgumentParser(description='Command-line example.')# Add optional switchesparser.add_argument('-v', action='store_true', dest='is_verbose',                    help='produce verbose output')parser.add_argument('-o', action='store', dest='output',                    metavar='FILE',                    help='direct output to FILE instead of stdout')parser.add_argument('-C', action='store', type=int, dest='context',                    metavar='NUM', default=0,                    help='display NUM lines of added context')# Allow any number of additional arguments.parser.add_argument(nargs='*', action='store', dest='inputs',                    help='input filenames (default is stdin)')args = parser.parse_args()print(args.__dict__)
