# Time complexity: O(N^2). Each step is O(N) compares&swaps
# Space complexity: O(1)
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i - 1
        while j >= 0:
            if array[i] < array[j]:
                tmp = array[i]
                array[i] = array[j]
                array[j] = tmp

            i -= 1
            j -= 1

    return array


array = [5, 2, 4, 6, 1, 3]
print(insertion_sort(array))
