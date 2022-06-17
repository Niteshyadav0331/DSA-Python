def interpolation_search(arr, low, high, x):
    if (low <= high and x >= arr[low] and x <= arr[high]):
        pos = (low + ( x - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if (arr[pos] == x):
            return pos

        elif(arr[pos] > x):
            return interpolation_search(arr, low, pos - 1, x)

        else:
            return interpolation_search(arr, pos + 1, high, x)

    return -1

arr = [2, 5, 9, 11, 12, 14, 15]
n = len(arr)

result = interpolation_search(arr, 0, n - 1, 15)
if result != -1:
    print(f"Number found at index {result}")

else:
    print('Number not found in array')
