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

def exponential_search(arr, n, x):
    if arr[0] == x:
        return 0

    i = 1
    while i < n and arr[i] <= x:
        i = i * 2

    return binary_search(arr, i //2, min(i, n - 1), x)

arr = [2, 5, 9, 11, 12, 14, 15]
n = len(arr)

result = exponential_search(arr, n , 14)
if result != -1:
    print(f"Number found at index {result}")

else:
    print('Number not found in array')