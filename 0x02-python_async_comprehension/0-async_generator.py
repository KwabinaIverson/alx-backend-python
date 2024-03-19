#!/usr/bin/env python3
"""A coroutine called async_generator that takes no arguments."""
import asyncio
import random


async def async_generator():
"""
An asynchronous generator that yields random numbers
10 times with 1 second delay.
"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
