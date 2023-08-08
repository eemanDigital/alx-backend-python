#!/usr/bin/env python3
'''Task 1's module: Async Comprehensions.
'''
import asyncio
from typing import List
from asyncio import run
from random import uniform
from async_generator import async_generator

async def async_comprehension() -> List[float]:
    result = [i async for i in async_generator()]
    return result

async def main():
    print(await async_comprehension())

run(main())
