def linear_search(arr, target):
    for i in range(len(arr)):
        # if target is present, return it's location
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2

        if target == arr[middle]:
            return middle
        if target < arr[middle]:
            high = middle - 1
        else:
            low = middle + 1

    return -1  # not found
