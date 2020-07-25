#Time complexity: O(N log N)
#Space complexity: O(log N), the depth of recursion tree
def find_peak_2D(nums):
    return find_peak_2D_helper(nums, 0, len(nums[0]) - 1)

def find_peak_2D_helper(nums, l, r):
    current_column = (l + r) // 2 # mid
    current_row = find_current_row(nums, current_column)

    if nums[current_row][current_column] < nums[current_row][current_column - 1]:
        return find_peak_2D_helper(nums, l, current_column)
    elif nums[current_row][current_column] < nums[current_row][current_column + 1]:
        return find_peak_2D_helper(nums, current_column + 1, r)
    else:
        return (current_row, current_column)

def find_current_row(nums, current_column):
    current_row = 0
    max = 0; # local max (i, j)

    for row in range(len(nums)):
        if nums[row][current_column] > max:
            max = nums[row][current_column]
            current_row = row

    return current_row;


#Time complexity: O(log N)
#Space complexity: O(1)
def find_peak_1D_iteratively(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[mid + 1]:
            r = mid
        else:
            l = mid + 1

    return l

#Time complexity: O(log N)
#Space complexity: O(log N), the depth of recursion tree
def find_peak_1D_recursively(nums):
    return find_peak_1D_recursively_helper(nums, 0, len(nums) - 1)

def find_peak_1D_recursively_helper(nums, l, r):
    mid = (l + r) // 2

    if l == r:
        return l

    if nums[mid] > nums[mid + 1]:
        return find_peak_1D_recursively_helper(nums, l, mid)
    else:
        return find_peak_1D_recursively_helper(nums, mid + 1, r)

nums_1D = [0, 1, 2, 3, 2]
print(find_peak_1D_iteratively(nums_1D))
print(find_peak_1D_recursively(nums_1D))

nums_2D = [[5, 8, 5, 5], [14, 5, 9, 20], [10, 21, 7, 13], [12, 13, 8, 11]]
print(find_peak_2D(nums_2D))
