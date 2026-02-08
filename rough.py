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

arr = [3, 1, 6 ,2, 8]

merge_sort(arr)

print(arr)