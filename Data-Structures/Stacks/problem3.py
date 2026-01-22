class FreqStack:

    def __init__(self):
        #we created 2 dictionaries 
        # dict s to store values and their frequency
        # dict k to store stacks as values in which we will append values and key will be our frequency
        # and an integer maxf to store value of maximum frequency
        self.s = {}
        self.k = {}
        self.maxf = 0

    def push(self, val: int) -> None:
        # if our value is in our s dict then we will inc its frequency if not then we will set its value to 1 making our val the key
        # then we will  check if frequency of our val is > maxfreq or not if yes then we will assign this value to maxfreq
        # then we will check if we have a key with value f in dict k or not if not then wewill assign a list as value of that key and append our val in that list if not already

        if val in self.s:
            self.s[val]+=1
        else:
            self.s[val]= 1
        f = self.s[val]
        if self.maxf<f:
            self.maxf = f
        if f not in self.k:
            self.k[f] = []
        
        self.k[f].append(val)

        

    def pop(self) -> int:
        # we will now pop the last value in the list whose key is our maxfreq
        # and if our length of list of our key which is eqal to maxfreq is 0 we will update value of maxfreq to maxfreq -1 and at last we will return val which is our popped value 
        val = self.k[self.maxf].pop()
        self.s[val]-=1
        if len(self.k[self.maxf]) == 0:
            self.maxf -= 1

        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()