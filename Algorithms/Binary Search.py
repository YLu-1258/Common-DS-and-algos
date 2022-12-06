def BinarySearch(arr, target):
    hi = len(arr)-1
    lo = 0
    while lo <= hi:
        mid = (lo + hi)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1
    return -1

def BinarySearchRecursion(arr, target, lo, hi):
    if lo > hi:
        return -1
    mid = (lo+hi)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return BinarySearchRecursion(arr, target, lo, mid-1)
    elif arr[mid] < target:
        return BinarySearchRecursion(arr, target, mid+1, hi)
    

print(BinarySearch([1,2,3,4,7,90,1239],7))
print(BinarySearchRecursion([1,2,3,4,7,90,1239],7,0,6))

