import asyncio
from collections.abc import Callable
from typing import Any, TypeVar

import aiohttp
import async_timeout

T = TypeVar("T")

# This function allows you to run a synchronous function asynchronously using threads
# It helps improve the time and success rate for making multiple API requests concurrently by:
# 1. Running the specified synchronous function in a seperate thread to avoid blocking the event loop.
# 2. Implementing a retry mechanism to handle transient errors.
# 3. Setting a timeout to ensure that each attempt does not exceed a specified duration.
#
# Parameters:
# - fetch_function: Synchronous function to be executed.
# - *args: Arguments to pass the to the synchronous function.
# - max_retries: The maximum number of retry attempts if an error occurs.
#
# Returns:
# - The result of the synchronous function if successful within the retry attempts.
#
# Raises:
# - The last encountered exception if all retry attempts fail.


async def fetch_data_async(
    fetch_function: Callable[..., T], *args: Any, max_retries: int = 5
) -> T:
    for attempt in range(max_retries):
        try:
            async with async_timeout.timeout(10):
                result = await asyncio.to_thread(fetch_function, *args)
                return result
        except (asyncio.TimeoutError, aiohttp.ClientError) as e:
            print(f"Attempt {attempt + 1} for {args} failed: {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(2**attempt)
            else:
                print(f"Final attempt failed for {args[0]}")

    raise RuntimeError(f"Failed to fetch data fro {args} after {max_retries} attempts")
