#!/usr/bin/env python3
'''Task 2's module:  Run time for four
parallel comprehensions.
'''
import asyncio
from asyncio import gather
from time import time
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of running
    async_comprehension four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time()  # Record the start time

    # Run async_comprehension four times in parallel using asyncio.gather
    await gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time()  # Record the end time
    total_runtime = end_time - start_time
    return total_runtime


if __name__ == "__main__":
    print(asyncio.run(measure_runtime()))
