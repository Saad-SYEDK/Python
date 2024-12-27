# Quick Sort Algorithm
# 1. Choose a pivot element
#     first/last/random/median element can be chosen as the pivot element
# 2. Elements smaller than the pivot should be on the left side of the pivot and element 
#   larger than the pivot should be on the right side of the pivot.
# 3. Now the pivot is in the correct position, no need to touch the pivot again
# 4. Recursively apply the same process to the left and right side of the pivot(excluding the pivot)
# 5. If the array has one or zero elements return - base case
def quick_sort(array, low, hi):
    if low < hi:
        pivot = array[hi]
        
        i = low - 1
        for j in range(low, hi):
            if array[j] <= pivot:
                i += 1
                #swap array[i] wth array[j]
                temp = array[i] 
                array[i] = array[j]
                array[j] = temp
        i += 1 # This is our pivot index i.e the correct position of out pivot element
        # swap array[i] with array[hi]-> this is the pivot element
        temp = array[i]
        array[i] = array[hi]
        array[hi] = temp
        
        
        quick_sort(array, low , i-1)    # left side of the array - from start till pivot(excluding pivot)
        quick_sort(array, i+1 , hi)    # right side of the array - from pivot(excluded) till end.

array = [3, 2, 4, 6,1, 9]
quick_sort(array, 0, len(array)-1)
print(array)
