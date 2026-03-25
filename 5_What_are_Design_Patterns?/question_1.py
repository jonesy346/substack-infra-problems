"""
Question:

Implement the Singleton design pattern in Python. Your implementation should ensure that:
- Only one instance of the class can ever be created
- All calls to create a new instance return the same object
- The implementation is thread-safe

Answer:

The Singleton design pattern can be implemented using a class variable to hold the single instance and a class method to control access to that instance. To ensure thread safety, we can use a lock from the threading module.
We use a strategy known as "double-checked locking" to minimize the performance overhead of acquiring a lock every time the instance is accessed. The outer if not cls._instance avoids acquiring the lock on every call once the instance exists (which would be slow), and the inner check handles the race condition where two threads both pass the outer check simultaneously before either acquires the lock.
"""

import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:  # Double-checked locking
                    cls._instance = super().__new__(cls)
        return cls._instance

singleton_one = Singleton()
singleton_two = Singleton()
print(singleton_one is singleton_two)  # True
