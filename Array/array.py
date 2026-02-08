# Content
#  How Arrays wors
#  1. quick sort
#  2. merge sort
#  3. Binary Search
#  4. Exercise

# An array is a data structure that can store a fixed number of values of the same type.
# THe elements in an array are stored in contiguous memory locations,
#   which allows for efficient access and manipulation of the elements using their index.
# Arrays can be one-dimensional (like a list) or multi-dimensional (like a matrix).
# Arrays are fundamental data structures in programming and are used to implement other data structures like lists, stacks, queues, etc.
# In python, we have a built-in list data structure that can be used as an array, but it is more flexible and can store elements of different types. 
#   However, for the purpose of understanding arrays, we will treat lists as arrays in this context.

# Time Complexity : 
#   O(1) for accessing an element by index, 
#   O(n) for searching an element, 
#   O(n) for inserting/deleting an element (if we need to shift elements)
#   O(n) for traversing the array
#   In daynamic arrays (like python lists), the time complexity for inserting an element at the end is O(1) on average,
#       but can be O(n) in worst case when the array needs to be resized.

# Space Complexity : O(n) for storing n elements in the array



# Common Algorithms
def quick_sort(array, low, hi):
# Quick Sort Algorithm
# 1. Choose a pivot element
#     first/last/random/median element can be chosen as the pivot element
# 2. Elements smaller than the pivot should be on the left side of the pivot and element 
#   larger than the pivot should be on the right side of the pivot.
# 3. Now the pivot is in the correct position, no need to touch the pivot again
# 4. Recursively apply the same process to the left and right side of the pivot(excluding the pivot)
# 5. If the array has one or zero elements return - base case
# Time Complexity : O(n log n) in Best and Average cases.
#                   O(n^2) in worst case - if the pivot element is always the smallest or largest, we can avoid this by randomized pivot selection or any other methods to select the pivot.
# Space Complexity : O(log n) in best/average case, O(n) in worst case
    if low < hi:
        pivot = array[hi]
        
        i = low - 1
        for j in range(low, hi):
            if array[j] <= pivot:
                i += 1
                #swap array[i] wth array[j] if i and j are not equal
                if i != j:
                    array[i], array[j] = array[j], array[i]
        i += 1 # This is our pivot index i.e the correct position of our pivot element
        # swap array[i] with array[hi]-> this is the pivot element
        array[i], array[hi] = array[hi], array[i]
        
        
        quick_sort(array, low , i-1)    # left side of the array - from start till pivot(excluding pivot)
        quick_sort(array, i+1 , hi)    # right side of the array - from pivot(excluded) till end.









def merge_sort(array):
# Merge Sort Algorithm
# 1. Divide the given array into two halves
#     find the mid point of the array and then make two separate arrays to store left and right halves
# 2. recursively repeat the 1st step until there is only 1 element left in the array - base case
# 3. Merge the left and right halves
#     iterate through both the arrays and sort them
# Time Complexity : O(n log n) in all cases
# Space Complexity : O(n) - to store the extra arrays in all cases
    
    if len(array) <= 1: # Base case
        return
    mid = len(array) // 2
    left_half = array[0:mid] # start till mid
    right_half = array[mid:len(array)] # mid till end
    merge_sort(left_half)
    merge_sort(right_half)
    
    # Merging
    i = 0 # to iterate through left_half
    j = 0 # to iterate through right_half
    k = 0 # to iterate through original array 
    
    while i < len(left_half) and j < len(right_half): #if any one of the array is iterated we will exit from the loop
        if left_half[i] <= right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1
    
    # if some elements are left in left/right half we will add them to the main array 
    while i < len(left_half):
        array[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        array[k] = right_half[j]
        j += 1
        k += 1       






def binary_search(array, target):
# Binary Search Algorithm
# 1. Requires sorted array as input
# 2. Two pointers - lo(for staritng index of array) and hi(for end-index of array )
# 3. Find mid index - if element at mid indext is equal to the target return the index, else
#     4a. If the element at the mid index is smaller than target, move the lo pointer to mid+1
#     4b. IF the element at the mid index is larget than target, move the hi pointer to mid -1
# 5. Repeat this until lo<=hi, if we get out of the loop before returning, the element does not exist in the array.
# Time Complexity : O(1) in Best Case, O(log n) in Average/Worst Case
# Space Complexity : O(1) in all cases  
    lo, hi = 0, len(array)-1
    while lo <= hi:
        mid = (lo+hi) // 2
        if array[mid] == target:
            return mid # Target found - return index of the target element
        elif array[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1 # Target does not exist in the array, return -1 which means element does not exist

# This is main
array = [3, 2, 4, 6,1, 9]
quick_sort(array, 0, len(array)-1)
# merge_sort(array)
print(array)
