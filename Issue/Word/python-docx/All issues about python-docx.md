# All issues about python-docx
## Q1: Is there any way to know how many pages are there in a .docx file?
At present, NO.

1. One says:

  There isn't a way to do it in python-docx. 

  Until the document is rendered for a certain page size, 

  there's no way to know where the page breaks are or how many pages there will be.  

  python-docx has no way to know if you're using A4 or US-Letter or legal size pages,

  which will produce different page counts. 

  I sometimes get different results with the same data depending on whether I'm on Windows of macOS.

(from the link https://codesti.com/issue/python-openxml/python-docx/1142#:~:text=There%20isn%27t%20a%20way%20to%20do%20it%20in,size%20pages%2C%20which%20will%20produce%20different%20page%20counts.)

2. While other one says:

  A .docx file contains no concept of a "page". 
  
  The content of the document is divided into pages by the renderer, 
  
  maybe the Word application or Google Docs or whatever, 
  
  based on the printer capabilities and available fonts. 
  
  So there is no general-case method to discover the number of "pages" in a document file.
 
(from the link https://stackoverflow.com/questions/70660132/how-to-fetch-total-no-of-pages-count-in-python-docx.)
