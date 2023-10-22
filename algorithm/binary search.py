def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1

# Test the algorithm with an example array and target element
arr = [10, 70,5]
x = 70
result = binary_search(arr, 0, len(arr), x)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
# x = 4
# arr = [1,2,3,4,5,6,7,8,9]
# print(arr[8])