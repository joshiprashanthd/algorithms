"""
Represents a priority queue
"""
from typing import List, Dict, TypeVar, Generic, Tuple

T = TypeVar('T')


class PriorityQueue(Generic[T]):

    def __init__(self, maxsize: int = 0, max_queue: bool = False, sort_index: int = 0, key=None):
        """
        Arguments:
            maxsize: Maximum number of elements, this queue is allowed to store\n
            max_queue: If True, pop() operation will pop the tuple corresponding to the index of element given by [sort_index]\n
            sort_index: Index of element, which is used as key in sorted() function\n
        """
        self.key = key
        self.size = maxsize
        self.max_queue = max_queue
        self.sort_index = sort_index
        self.pq: List[T] = []

    def contains(self, key: str) -> bool:
        return any([item[0] == key for item in self.pq])

    def update_key(self, key: T, new_value: float) -> None:
        assert self.contains(key), Exception("Key is not present in priority queue")
        key_index = 0
        for i in range(len(self.pq)):
            if self.pq[i][0] == key:
                key_index = i
                break
        self.pq.pop(key_index)
        self.insert((key, new_value))

    def insert(self, element: T) -> None:
        assert self.size > len(self.pq), Exception("Queue Overflow")
        self.pq.append(element)

    def pop(self) -> T:
        assert (len(self.pq) > 0), Exception("Queue Underflow")
        if self.key is None:
            self.pq = sorted(self.pq, key=lambda item: item[self.sort_index], reverse=self.max_queue)
        else:
            self.pq = sorted(self.pq, key=self.key, reverse=self.max_queue)
        return self.pq.pop(0)

    def is_empty(self) -> bool:
        return len(self.pq) == 0
