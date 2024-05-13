class Queue:
    def __init__(self):
        self.queue =[]
    def enqueue(self,val):
        self.queue.append(val)
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]
    def is_empty(self):
        return len(self.queue) ==0
class Stack:
    def __init__(self, capacity):
        self.numArray = [0] * capacity
        self.top = -1
        self.size = 0

    def size(self):
        return self.size

    def push(self, value):
        if not self.isFull():
            self.top += 1
            self.numArray[self.top] = value
            self.size += 1
        else:
            print("Full")

    def pop(self):
        if not self.isEmpty():
            data = self.numArray[self.top]
            self.top -= 1
            self.size -= 1
            return data
        return -1

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == len(self.numArray)

    def peek(self):
        if self.top >= 0:
            return self.numArray[self.top]
        return -1

numStack = Stack(5)
numStack.push(11)
numStack.push(22)
numStack.push(33)
numStack.push(44)

numStack.pop()
numStack.pop()
# for i in range(numStack.size):
#     print(numStack.numArray[i])
myque = Queue()
myque.enqueue(numStack)
print(myque.queue)