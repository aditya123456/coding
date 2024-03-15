import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        # Priority is negated to create a min-heap
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        if not self.is_empty():
            # Return the item with the highest priority
            return heapq.heappop(self.heap)[1]
        else:
            raise IndexError("pop from an empty priority queue")

    def is_empty(self):
        return len(self.heap) == 0

# Example usage:
priority_queue = PriorityQueue()
priority_queue.push("Task1", 3)
priority_queue.push("Task2", 1)
priority_queue.push("Task3", 2)

while not priority_queue.is_empty():
    print(priority_queue.pop())
