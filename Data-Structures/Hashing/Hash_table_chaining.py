import random
class Hash_table:
    def __init__(self,capacity=800):
        self.buckets = [[]for i in range (capacity)]
        self.capacity = capacity
        self.size = 0
        self.max_load = 0.75
        self.p = 2**56+1
        self.a = random.randrange(1,self.p)
        self.b = random.randrange(0,self.p)

    def _hash(self,key):
        return (((self.a*hash(key )+self.b)%self.p)%self.capacity)
    

    def put(self,key,value):
        if (self.size+1)/self.capacity > self.max_load:
            self.resize()

        index = self._hash(key)
        bucket = self.buckets[index]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                return
        
        self.buckets[index].append((key,value))
        self.size+=1


    def get(self,key):
        index = self._hash(key)
        if self.buckets[index]==[]:
            return None
        else :
            bucket = self.buckets[index]
            for k , v in bucket:
                if k == key:
                    return v
            return None
                
    def delete(self,key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size-=1
                return True
        
        return False
    def resize(self):
        old_buckets = self.buckets
        capacity = self.capacity*2
        self.buckets = [[]for i in range (capacity)]
        self.size = 0
        for bucket in old_buckets:
            for k,v in bucket:
                self.put(k,v)
    def _iter(self):
        for bucket in self.buckets:
            for k,v in bucket:
                yield k

    def __repr__(self):
        pairs = []
        for bucket in self.buckets:
            for k, v in bucket:
                pairs.append(f"{repr(k)}: {repr(v)}")
        return "{" + ", ".join(pairs) + "}"

        
ht = Hash_table()
ht.put(1, "a")
ht.put(2, "b")
ht.put("x", 10)

print(ht)