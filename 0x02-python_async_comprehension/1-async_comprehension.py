#!/usr/bin/env python3
"""
Async_generator from the previous task and then write a coroutine called 
async_comprehension that takes no arguments.
"""
import asyncio

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension():
    """
    The coroutine will collect 10 random numbers using an async comprehensing
    Return: 10 random numbers.
    """
    result = [i async for i in async_generator()]
    return result
