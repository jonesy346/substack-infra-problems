"""
Question: Write a Python program that attempts to perform a CPU-bound task using multiple threads. Observe how the GIL (Global Interpreter Lock) prevents true parallel execution.

Answer: We can create a simple numerical task, such as calculating the factorial of a large number, and then run this task in multiple threads. Due to the GIL, we will see that the threads do not execute in parallel, and the performance will not improve compared to running the task in a single thread.
"""

import time
from threading import Thread

COUNT = 500

def factorial(n):
    # base case
    if n == 0:
        return 1
    
    return n * factorial(n - 1)

def single_thread_factorial(count = COUNT):
    start = time.time()
    factorial(count)
    end = time.time()

    print('Time taken for single thread run in seconds -', end - start)

def multi_thread_factorial(count = COUNT):
    t1 = Thread(target=factorial, args=(count,))
    t2 = Thread(target=factorial, args=(count,))

    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()

    print('Time taken for multi thread run in seconds -', end - start)

single_thread_factorial()
multi_thread_factorial()
