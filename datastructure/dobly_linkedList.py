class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def display_backward(self):
        current = self.head
        while current and current.next:
            current = current.next

        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

# Example usage
if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()

    doubly_linked_list.append(1)
    doubly_linked_list.append(2)
    doubly_linked_list.append(3)

    print("Forward traversal:")
    doubly_linked_list.display_forward()

    print("Backward traversal:")
    doubly_linked_list.display_backward()
