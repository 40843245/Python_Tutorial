# Coroutines in Python
## Declaration
To define a func as a coroutine, replace the keyword return to await and add the keyword async in front of the keyword def.
## Invocation
To invoke a coroutine, just place the whole function inside call in asyncio.run() . Such as
    
    import asyncio
    async def main():
        print('hello')
        await asyncio.sleep(1)
        print('world')
    
    asyncio.run(main())
    hello
    world
## Usage
It can be used for async (asynchronization) tasks.
## Module
It is defined in the built-in module.
asyncio 

## Ref
https://docs.python.org/3/library/asyncio-task.html
