def merge(arr, l, m, r):
    L = arr[l:m+1]
    R = arr[m+1:r+1]

    i, j = 0, 0
    k = l

    while (i < len(L) and j < len(R)):
        if (L[i] < R[j]):
            arr[k] = L[i]
            i += 1

        else:
            arr[k] = R[j]
            j += 1

        k += 1

    while(i < len(L)):
        arr[k] = L[i]
        i += 1
        k += 1

    while(j < len(R)):
        arr[k] = R[j]
        j += 1
        k += 1

    return arr

def mergesort(arr, l, r):
    if (l < r):
        m = l + (r - l) // 2

        mergesort(arr, l, m)
        mergesort(arr, m + 1, r)
        merge(arr, l, m, r)

arr = [18, 20, 5, 19, 5, 3, 10]
result = mergesort(arr, 0, len(arr))

print(result)