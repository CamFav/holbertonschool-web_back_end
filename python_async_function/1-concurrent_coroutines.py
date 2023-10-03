#!/usr/bin/env python3
""" Multiple coroutines at the same time with async"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Waits for a random delay between 0 and max_delay """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    sorted_delays = sorted(delays)
    return sorted_delays
