

class Heap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self.heapify_up()

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down()
        return root

    def heapify_up(self):
        index = len(self.heap) - 1
        while index > 1:
            parent = (index - 1) // 2
            if self.heap[parent] > self.heap[index]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break


    def heapify_down(self):
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if (
                    left_child_index < len(self.heap)
                    and self.heap[left_child_index] < self.heap[smallest]
            ):
                smallest = left_child_index

            if (
                    right_child_index < len(self.heap)
                    and self.heap[right_child_index] < self.heap[smallest]
            ):
                smallest = right_child_index

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break


min_heap = Heap()
min_heap.push(4)
min_heap.push(1)
min_heap.push(7)
min_heap.push(3)

print(min_heap.pop())  # Output: 1
print(min_heap.pop())  # Output: 3
print(min_heap.pop())  # Output: 4
print(min_heap.pop())  # Output: 7