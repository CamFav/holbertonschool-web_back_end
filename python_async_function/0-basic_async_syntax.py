#!/usr/bin/env python3
""" Basic annotations - async generator """
import asyncio
import random


async def wait_random(max_delay: int = 0) -> float:
    """ Waits for a random delay between 0 and max_delay """
    random_delay = random.uniform(0, max_delay)

    await asyncio.sleep(random_delay)

    return random_delay
