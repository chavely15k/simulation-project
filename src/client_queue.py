from collections import *

class client_queue:
    def __init__(self) -> None:
        self.queue = deque()
    def push(self, item):
        self.queue.append(item)
    def pop(self):
        self.queue.popleft()
    def front(self):
        return self.queue[0]
    def empty(self):
        return len(self.queue) == 0


    