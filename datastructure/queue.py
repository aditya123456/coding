class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)

# Example usage
if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Queue:", queue.items)

    dequeued_item = queue.dequeue()
    print("Dequeued item:", dequeued_item)
    print("Queue after dequeue:", queue.items)

    front_item = queue.front()
    print("Front item:", front_item)

    print("Queue size:", queue.size())




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return removed_item
        else:
            print("Queue is empty")

    def front_item(self):
        if not self.is_empty():
            return self.front.data
        else:
            print("Queue is empty")

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

# Example usage
if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Queue size:", queue.size())
    print("Front item:", queue.front_item())

    dequeued_item = queue.dequeue()
    print("Dequeued item:", dequeued_item)
    print("Queue size after dequeue:", queue.size())
