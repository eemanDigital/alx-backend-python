#!/usr/bin/env python3
'''Task 0's module.
'''
import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    '''Waits for a random number of seconds.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
