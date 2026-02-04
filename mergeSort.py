def mergeSort(array):
    if len(array) > 1:
            
        mid = len(array) // 2
        
        rightHalf = array[:mid]
        leftHalf = array[mid:]
        
        mergeSort(rightHalf)    
        mergeSort(leftHalf)    
        i = j = k = 0
        
        while i < len(rightHalf) and j < len(leftHalf):
            if rightHalf[i] <= leftHalf[j]:
                array[k] = rightHalf[i]
                i+=1
                k+=1
            else:
                array[k] = leftHalf[j]
                j+=1
                k+=1
        while i < len(rightHalf):
            array[k] = rightHalf[i]
            i+=1
            k+=1
        while j < len(leftHalf):
            array[k] = leftHalf[j]
            j+=1
            k+=1

array = [12, 11, 13, 5, 6, 7]

mergeSort(array)

print(array)