def ternary_search(arr, low, high, x):
    if (low <= high):
        mid1 = low + (high - low) // 3
        mid2 = mid1 + (high - low) // 3

        if (arr[mid1] == x):
            return mid1

        elif(arr[mid2] == x):
            return mid2

        elif(arr[mid1] > x):
            return ternary_search(arr, low, mid1 - 1, x)

        elif(arr[mid2] < x):
            return ternary_search(arr, mid2 + 1, high, x)

        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, x)

    return  -1

arr = [2, 5, 9, 11, 12, 14, 15]
n = len(arr)

result = ternary_search(arr, 0, n - 1 , 14)
if result != -1:
    print(f"Number found at index {result}")

else:
    print('Number not found in array')