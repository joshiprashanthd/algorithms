from typing import List, TypeVar, Generic

T = TypeVar('T')

class Edge(Generic[T]):
    def __init__(self, from_: T, to: T, weight: float = 0):
        self.from_ = from_
        self.to = to
        self.weight = weight
        
    def __str__(self):
        return f"{self.from_}" + " -" + f"{self.weight}" + "-> " + f"{self.to}"
    