class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = []
        self.m = m

    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.m:
            self.queue.insert(0,value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.m:
            self.queue.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if len(self.queue) > 0:
            self.queue.remove(self.queue[0])
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if len(self.queue) > 0:
            self.queue.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return -1

    def getRear(self) -> int:
        if len(self.queue) >0:
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if len(self.queue) == self.m:
            return True
        else:
            return False
