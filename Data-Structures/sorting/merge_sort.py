def merge(array1,array2):
    
    i = len(array1) -1
    j = len(array2)- 1
    array = [0]*(len(array1)+ len(array2))
    c = len(array)-1
    while i>=0 and j >=0:
        if array1[i] > array2[j]:
           
            array[c] = array1[i]
            i-=1
            c-=1
        else:
             array[c] = array2[j]
             j-=1
             c-=1
    while i>=0 :
        array[c] = array1[i]
        i-=1
        c-=1
    while j>=0 :
        array[c] = array2[j]
        j-=1
        c-=1
    return array
            
def merge_sort(array):
    if len(array)<=1:
        return array
    mid = len(array)//2
    k = merge_sort(array[:mid])
    j = merge_sort(array[mid:])

    return merge(k,j)
print(merge_sort([4, 2, 7, 1],0,3))
