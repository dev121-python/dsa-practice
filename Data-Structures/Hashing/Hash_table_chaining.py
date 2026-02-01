class Hash_table:
    def __init__(self):
        self.buckets = [[]for i in range (10)]


    def put(self,key,value):
        index = key%len(self.buckets)
        bucket = self.buckets[index]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                return
        
        self.buckets[index].append((key,value))


    def get(self,key):
        index = key % len(self.buckets)
        if self.buckets[index]==[]:
            return "none"
        else :
            bucket = self.buckets[index]
            for k , v in bucket:
                if k == key:
                    return v
            return None
                
    def delete(self,key):
        index = key%len(self.buckets)
        bucket = self.buckets[index]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return True
        
        return False
        
        

hm  = Hash_table()

hm.put(1, 10)
hm.put(11, 110)   # collision with 1 if size = 10

print(hm.get(1))   # 10
print(hm.get(11))  # 110
print(hm.delete(1)) 
print(hm.get(1))  # none
print (hm)
