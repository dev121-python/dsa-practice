class Solution:
    def buildArray(self, target, n: int):
        res = []
        j = 0  # pointer for target
        
        for i in range(1, n + 1):
            if j == len(target):
                break
            
            res.append("Push")
            
            if i == target[j]:
                j += 1
            else:
                res.append("Pop")
        
        return res
k = Solution.buildArray(self = None,target=[1,3],n=3)
print(k)

        