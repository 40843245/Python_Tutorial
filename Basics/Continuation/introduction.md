# Continuation in programming language
## Introduction
Continuation is a technique that can make something to start from the last point of previous execution.

One kind of this is a coroutine. For coroutines in Python, the keyword yield will store the current state (called state1) of the function then ends the function, 

once it is called again, the previous state (here is state1) will be loaded and starts from the statement where previous state (state1) ends up with.
