"""
Question:

Implement the Strategy design pattern for a sorting system, where each strategy represents a different sorting algorithm (e.g., bubblesort, mergesort). The system should allow switching strategies at runtime.

Answer:

The Strategy design pattern has the following components:
- Strategy Interface: This defines a common interface for all sorting algorithms.
- Concrete Strategies: These are the specific sorting algorithm implementations (e.g., BubbleSort, MergeSort).
- Context: This is the class that uses a Strategy to perform sorting. It maintains a reference to a Strategy object and can switch it at runtime.
"""

from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        n = len(data)

        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]

        return data

class MergeSort(SortStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data

        midpoint = len(data) // 2
        left_half = data[:midpoint]
        right_half = data[midpoint:]

        sorted_left = self.sort(left_half)
        sorted_right = self.sort(right_half)

        return self.merge(sorted_left, sorted_right)

    def merge(self, left, right):
        merged = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

class SortContext:
    def __init__(self, strategy: SortStrategy):
        self._sort_strategy = strategy

    def set_sort_strategy(self, strategy: SortStrategy):
        self._sort_strategy = strategy

    def sort(self, data):
        return self._sort_strategy.sort(data)
    
# Example usage
data = [64, 34, 25, 12, 22, 11, 90]
context = SortContext(BubbleSort())
print("Bubble Sort:", context.sort(data.copy()))

context.set_sort_strategy(MergeSort())
print("Merge Sort:", context.sort(data.copy()))
