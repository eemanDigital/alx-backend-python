#!/usr/bin/env python3
'''Task 1's module: Async Comprehensions.
'''
import asyncio
from typing import List


delay_random = __import__('0-basic_async_syntax').delay_random


async def wait_n(n: int, delay: int) -> List[float]:
    '''Executes wait_random n times.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: delay_random(delay), range(n)))
    )
    return sorted(wait_times)
