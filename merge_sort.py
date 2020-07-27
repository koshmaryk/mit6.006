#Time complexity: O(N log N)
#Space complexity: O(lon N)
def merge_sort(array):
    if len(array) > 1:
        left = merge_sort(array[: len(array) // 2])
        right = merge_sort(array[len(array) // 2 :])

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k]  = right[j]
            j += 1
            k += 1

    return array

array = [5, 2, 4, 6, 1, 3]
print(merge_sort(array))
