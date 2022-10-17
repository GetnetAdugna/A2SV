class MyQueue:

    def __init__(self):
        self.stackOne = []
        self.stackTwo = []

    def push(self, x: int) -> None:
        self.stackOne.append(x)
        

    def pop(self) -> int:
        length = len(self.stackOne)
        for i in range(length):
            self.stackTwo.append(self.stackOne.pop())
        val = self.stackTwo.pop()
        length = len(self.stackTwo)
        for J in range(length):
            self.stackOne.append(self.stackTwo.pop())
        return val
        
        
        

    def peek(self) -> int:
        return self.stackOne[0]
        

    def empty(self) -> bool:
        return len(self.stackOne)  == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()