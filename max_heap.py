#           i >> 1
#          /
#         i
#      /    \
# i << 1    (i << 1) + 1
A = [0, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heap_size = len(A) - 1

def max_heapify(A: list, i: int):
    l = 2 * i
    r = 2 * i + 1
    if l <= heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def build_max_heap(A: list):
    n = len(A)
    for i in range(n // 2, 0, -1):
        max_heapify(A, i)


# Time complexity: O(N log N)
# Space complexity: O(1)
def heap_sort(A):
    n = len(A)
    build_max_heap(A)
    for i in range(n - 1, 1, -1):
        A[1], A[i] = A[i], A[1]
        global heap_size
        heap_size -= 1
        max_heapify(A, 1)

heap_sort(A)
print(A)