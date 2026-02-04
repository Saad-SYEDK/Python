def quickSort(arr, lo, hi):
    if hi <= lo:
        return
    
    pivotElement = arr[hi]
    i = lo - 1
    j = lo
    while j < hi:
        if arr[j] < pivotElement:
            i+=1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        j+=1
    i+=1
    temp = arr[i]
    arr[i] = arr[hi]
    arr[hi] = temp
    
    pivotPosition = i
    
    quickSort(arr, lo, pivotPosition-1)
    quickSort(arr, pivotPosition+1, hi)


array = [12, 11, 13, 5, 6, 7]
quickSort(array,0 , len(array)-1)

print(array)