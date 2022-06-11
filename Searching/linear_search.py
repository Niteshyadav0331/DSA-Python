def linear_search(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i

    return -1

arr = [2, 5, 9, 12, 11, 15]
n = len(arr)

result = linear_search(arr, n, 9)
if result != -1:
    print(f"Number found at index {result}")

else:
    print('Number not found in array')