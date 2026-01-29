def insertion_sort(k):
    n = len(k)
    for i in range(1,n-1):
        key =  k[i]
        j =  i-1
        while j >= 0  and key < k[i]:
            k[j+1] = k[j]
            j-=1
        k[j+1] = key
    return k

k = [1,45,34,-4,667,23]
print("Unsorted array is:", k)
sorted_array = insertion_sort(k)
print("Sorted array is:", sorted_array)   