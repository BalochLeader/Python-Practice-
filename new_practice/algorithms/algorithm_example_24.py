# Algorithm Example 24
# This program demonstrates a simple sorting algorithm (Bubble Sort).

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

my_array = [64, 34, 25, 12, 22, 11, 90]
print(f"Original array: {my_array}")
sorted_array = bubble_sort(my_array)
print(f"Sorted array: {sorted_array}")
