#!/usr/bin/env python3
'''Task 1's module: Async Comprehensions.
'''
import asyncio
from typing import List
from asyncio import run
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async
    comprehension over async_generator.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    result = [i async for i in async_generator()]
    return result


async def main():
    print(await async_comprehension())

run(main())  # Execute the main coroutine
