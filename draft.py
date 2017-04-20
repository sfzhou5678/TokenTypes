
class Stack:
    """模拟栈"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items)==0

    def push(self, item):
        # print("push")
        self.items.append(item)

    def pop(self):
        # print("pop")

        if not self.isEmpty():
            return self.items.pop()
        else:
            print('NULL')

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s=Stack()
a=("asdf",1)
b=("bbbb",2)
s.push(a)
s.push(b)
print(s.pop()[0])