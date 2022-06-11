def binary_search(arr, low, high, x):

    mid = low + (high - low) // 2

    if (low <= high):
        if arr[mid] == x:
            return mid

        elif(arr[mid] > x):
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)

    return -1

arr = [2, 5, 9, 11, 12, 14, 15]
n = len(arr)

result = binary_search(arr, 0, n - 1, 12)
if result != -1:
    print(f"Number found at index {result}")

else:
    print('Number not found in array')