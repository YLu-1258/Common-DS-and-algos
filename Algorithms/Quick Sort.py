arr1 = [13,153,243,17,28,57,26]

def partition(arr, lo, hi):                         # This is the partitioning function
    pivot = arr[hi]                                 # Establish our Pivot to be the last element. We will move all values less than pivot to the left of pivot, and all values greater to the right
    i = lo - 1                                      # This is our marker for marking values larger than the pivot for swapping
    for j in range(lo, hi):
        if arr[j] <= pivot:                         # marker will do nothing if the value is greater than the pivot
            i+=1                                    # marker will be shifted if value is lesser than pivot, to prevent shifting of two values smaller than pivot. This value is shifted until it is right before a value greater than the pivot. When the next value smaller than the pivot is found, i will be incremented to the index of that larger number
            arr[i], arr[j] = arr[j], arr[i]         # Swap the larger value with the smaller value
    arr[i+1], arr[hi] = arr[hi], arr[i+1]           # At the end of the loop, i+1 should be the index of where the pivot should be placed, because i is the number of total elements lesser than or equal to the pivot. 
    return i+1                                      # return partioning index for QSort to know where to split array.

def QuickSort(arr, lo, hi):
    if lo < hi:
        partition_index = partition(arr, lo, hi)

        QuickSort(arr, lo, partition_index-1)

        QuickSort(arr, partition_index+1, hi)

QuickSort(arr1, 0, 6)
print(arr1)
            