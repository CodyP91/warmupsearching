def find_max(arr):
    return max(arr)

def find_second_largest(arr):
    arr.sort()
    return arr[-2]

def find_kth_largest(arr, k):
    arr.sort(reverse=True)
    return arr[k-1]

# Testing find_max
numbers = [5, 2, 9, 1, 7]
print(find_max(numbers))  # Output: 9

numbers = [3, 8, 2, 4, 6]
print(find_max(numbers))  # Output: 8

numbers = [1, 1, 1, 1, 1]
print(find_max(numbers))  # Output: 1

# Testing find_second_largest
numbers = [5, 2, 9, 1, 7]
print(find_second_largest(numbers))  # Output: 7

numbers = [3, 8, 2, 4, 6]
print(find_second_largest(numbers))  # Output: 6

numbers = [1, 1, 1, 1, 1]
print(find_second_largest(numbers))  # Output: 1

# Testing find_kth_largest
numbers = [5, 2, 9, 1, 7]
k = 3
print(find_kth_largest(numbers, k))  # Output: 5

numbers = [3, 8, 2, 4, 6]
k = 2
print(find_kth_largest(numbers, k))  # Output: 6

numbers = [1, 1, 1, 1, 1]
k = 1
print(find_kth_largest(numbers, k))  # Output: 1

# Add more test cases...

