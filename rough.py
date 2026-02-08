def merge_sort(arr):
    if len(arr) <= 1:
        return
    
    
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:len(arr)]
    
    merge_sort(left)
    merge_sort(right)
    
    
    # Logic for merge
    i = j = k = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left [i]
            i += 1
        else:
            arr[k] = right[j]
            j+=1
        k+=1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]    
        j += 1
        k += 1 


def quicksort(arr, lo, hi):
    if lo >= hi :
        return
    
    pivot = arr[hi]
    
    
    i = lo-1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i +=1 
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
    
    i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    
    quicksort(arr, lo, i-1)
    quicksort(arr, i+1, hi)
    
    
        

arr = [3, 1, 6 ,2, 8]

quicksort(arr, 0, len(arr) - 1)

print(arr)