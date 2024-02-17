from math import inf
from heapq import *

class heap:
    def __init__(self) -> None:
        self.heap = []
    def empty(self):
        return len(self.heap) == 0
    def push(self, item):
        heappush(self.heap, item)
    def pop(self): 
        return heappop(self.heap)
    def top(self):
        if not self.empty(): return self.heap[0]
        else: return None
