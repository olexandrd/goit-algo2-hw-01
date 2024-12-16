def min_max_search(arr):
    def recursive_search(arr, low, high):
        if low == high:
            return arr[low], arr[low]
        elif high == low + 1:
            return (min(arr[low], arr[high]), max(arr[low], arr[high]))
        else:
            mid = (low + high) // 2
            min1, max1 = recursive_search(arr, low, mid)
            min2, max2 = recursive_search(arr, mid + 1, high)
            return min(min1, min2), max(max1, max2)

    if not arr:
        return None, None
    return recursive_search(arr, 0, len(arr) - 1)


print(min_max_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(min_max_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
