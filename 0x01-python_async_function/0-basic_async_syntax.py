#!/usr/bin/env python3
"""
`wait_random` function is an asynchronous coroutine function
that waits `max_delay` for a random delayed number.
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """wait_random function is an asynchronous coroutine function
    that wait for max_delay for a random delayed number.

    Args:
        max_delay (int, optional): Number for delayed time. Defaults to 10.

    Returns:
        Time (s): The time it took for the function to run.
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
