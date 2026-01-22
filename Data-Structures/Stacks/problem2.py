class MinStack:
    # time complexity is O(1)

    def __init__(self):
        self.s = []
        self.k = []
        self.p = None   
        # created  2 stacks s and k s is our stack of operation and k is the stack which will hold minimum values
        

    def push(self, val: int) -> None:
        # we will append value in ourmainstack s and if the min stack is empty or value at last of minstack is greater than the value to be appended then we will append the value in minstack
        self.s.append(val)
        if len(self.k) == 0 or val <= self.k[-1]:  
            self.k.append(val)
        return None
        

    def pop(self) -> None:
        #we will pop the value from mainstack and if the value at end of minstack k is equal to value we are popping then we will pop minstack k 
        if len(self.s) == 0:
            return None
        else:
            p = self.s.pop()
            if p == self.k[-1]:
                self.k.pop()

    def top(self) -> int:
        # we will return last element of stack s
        if len(self.s) == 0:
            return None
        else:
            return self.s[-1]

    def getMin(self) -> int:
        # we will return last element of min stack it is the minimum value in our mainstack
        if len(self.k) == 0:
            return None
        else:
            return self.k[-1]
