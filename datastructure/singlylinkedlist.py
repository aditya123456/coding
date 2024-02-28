# operations
# PushFront(key) ---add to front
# key topFront() ---return front item
# PopFront()----- remove fron item
# PushBack(key) ----- add to back
# key TopBack() ----- return back items
# PopBack()------------- remove back item
# Boolean Find(key) ----is key in list
# Erase(key) -----remove key from list
# Boolean Empty() ---eompy list
# AddBefore(Node, key)------ add key before node



class Node:
    def __init__(self, key):
        self.key=key
        self.next = None



class SingleLnkedList:
    def __init__(self):
        self.head = None
        self.node = None
        self.tail = None


    def PushFront(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node


    def topFront(self):
        return self.head.key

    def PopFront(self):
        self.head = self.head.next


    def PushBack(self, key):
        new_node = Node(key)
        new_node.next = None
        self.tail.next = new_node
        self.tail = new_node

    def TopBack(self):
        pass

    def PopBack(self):
        if self.head == None:
            print("list is empty")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            p = self.head
            while p.next.next  != None:
                p = p.next
            p.next = None
            self.tail = p

    def find(self, key):
        pass

    def Erase(self, key):
        pass

    def empty(self):
        pass

    def addBefore(self, Node, key):
        pass



x = SingleLnkedList()
x.PushFront(10)
x.PushFront(20)
x.PushFront(30)

print(x.topFront())
x.PopFront()
print(x.topFront())