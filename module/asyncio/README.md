# asyncio module
## FAQ
### How to check a function is a coroutine function (i.e. defined with async modifier)?
#### Answer
Two approaches.

    asyncio.iscoroutinefunction(func)

or 

    inspect.iscoroutinefunction(object)

I personally strongly recommend the 1th approach since it seems that it is more precise.

#### Ref
It can be found at stackoverflow.

https://stackoverflow.com/questions/36076619/test-if-function-or-method-is-normal-or-asynchronous

Very thankful to dirn and Sharad.

dirn provides 1th approach and Shared provides 2th.

#### Figure
For 1th approach,

![image](https://github.com/40843245/Python_Tutorial/assets/75050655/72254585-e346-4137-b2ba-100d5e20abbc)

For 2th approach,

![image](https://github.com/40843245/Python_Tutorial/assets/75050655/1445bdaf-8c80-46e0-a462-4d101fc10ee1)
