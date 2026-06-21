"""
Question:

Let’s imagine you have 1 million (actual number doesn’t matter, just that it’s large enough to justify using Kafka) cars emitting requests to a service consumer, which uploads the requests to Kafka topics. How would you assign which partition (a node on the topic) a request is routed to?

Answer:

A common partition strategy involves using a hash function (like murmur2, maps string to integer) to compute a hash of the key and then computing its modulus with the number of partitions to determine the target partition.
"""

import mmh3

def assign_partition(key, num_partitions):
    """
    Assign a partition for a given key using a hash function.

    :param key: The key to be hashed (e.g., car ID).
    :param num_partitions: The total number of partitions available.
    :return: The partition number to which the key is assigned.
    """
    seed = 42
    hash_value = mmh3.hash(key, seed)
    partition = abs(hash_value) % num_partitions # here we take absolute value of the hash_value since mmh3 can return negative values, and we want to ensure the partition number is non-negative
    return partition

num_partitions = 10
car_id = "car_1"
print(assign_partition(car_id, num_partitions))
car_id = "car_2"
print(assign_partition(car_id, num_partitions))
car_id = "car_3"
print(assign_partition(car_id, num_partitions))
