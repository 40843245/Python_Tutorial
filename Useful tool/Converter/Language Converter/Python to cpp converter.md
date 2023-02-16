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
from collections import OrderedDictd = OrderedDict([('first', 1),   ('second', 2),       ('third', 3)])d.items()

#### Example Output

from collections import OrderedDictd = OrderedDict([('first', 1),   ('second', 2),       ('third', 3)])list(d.items())

### Example 2
#### Example Input 
import argparseparser = argparse.ArgumentParser(description='Command-line example.')# Add optional switchesparser.add_argument('-v', action='store_true', dest='is_verbose',                    help='produce verbose output')parser.add_argument('-o', action='store', dest='output',                    metavar='FILE',                    help='direct output to FILE instead of stdout')parser.add_argument('-C', action='store', type=int, dest='context',                    metavar='NUM', default=0,                    help='display NUM lines of added context')# Allow any number of additional arguments.parser.add_argument(nargs='*', action='store', dest='inputs',                    help='input filenames (default is stdin)')args = parser.parse_args()print args.__dict__
#### Example Output
import argparseparser = argparse.ArgumentParser(description='Command-line example.')# Add optional switchesparser.add_argument('-v', action='store_true', dest='is_verbose',                    help='produce verbose output')parser.add_argument('-o', action='store', dest='output',                    metavar='FILE',                    help='direct output to FILE instead of stdout')parser.add_argument('-C', action='store', type=int, dest='context',                    metavar='NUM', default=0,                    help='display NUM lines of added context')# Allow any number of additional arguments.parser.add_argument(nargs='*', action='store', dest='inputs',                    help='input filenames (default is stdin)')args = parser.parse_args()print(args.__dict__)
