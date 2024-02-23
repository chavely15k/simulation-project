from collections import *

class queue:
    def __init__(self) -> None:
        self.first = 0
        self.count = 0
    def push(self, item):
        if self.count == 0:
            self.first = item
        self.count = self.count + 1
    def pop(self):
        if self.count == 0: return None
        self.count = self.count - 1
        self.first = self.first + 1
        return self.first - 1
    def front(self):
        return self.first
    def empty(self):
        return self.count == 0


    