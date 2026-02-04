def binarySearch(arr, key):
    lo = 0
    hi = len(arr) -1
    
    while lo <= hi:
        mid = (lo+hi) // 2
        
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            lo = mid +1
        else:
            hi = mid -1
             
    return -1

array =[0,1,2,3,4,5]

print(binarySearch(array, 5))
            