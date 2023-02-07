# All issues about python-docx
## Q1: Is there any way to know how many pages are there in a .docx file?
At present, NO.

The reason why is

1. Different size will get different counts:

  There isn't a way to do it in python-docx. 

  Until the document is rendered for a certain page size, 

  there's no way to know where the page breaks are or how many pages there will be.  

  python-docx has no way to know if you're using A4 or US-Letter or legal size pages,

  which will produce different page counts. 

  I sometimes get different results with the same data depending on whether I'm on Windows of macOS.

https://codesti.com/issue/python-openxml/python-docx/1142#:~:text=There%20isn%27t%20a%20way%20to%20do%20it%20in,size%20pages%2C%20which%20will%20produce%20different%20page%20counts.

## Ref
