

class Stack:
    def __init__(self):
        self.stack= []


    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            self.stack.pop()

    def isEmpty(self):
        return len(self.stack)==0


parentthesis = "((((([[[[[[[]]]]]]]))))))"
s = Stack()
flag = True
for i in parentthesis:
    if i in ['[','(']:
        s.push(i)
    else:
        if s.isEmpty():
            flag = False
        top = s.pop()
        if top in  ['[','('] and i not in  ['[','(']:
            flag = False
if s.isEmpty() and flag== True:
    print("parenthesis is balanced")
