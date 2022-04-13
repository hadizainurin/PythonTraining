# QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.
# There are many different version of quickSort that pick pivot in a different way

# 1. Always pick first element as pivot
# 2. Always pick last element as pivot
# 3. Pick a random element as pivot
# 4. Pick median as pivot

###PSEUDOCODE####
# /* low  --> Starting index,  high  --> Ending index */
# quickSort(arr[], low, high)
# {
#     if (low < high)
#     {
#         /* pi is partitioning index, arr[p] is now
#            at right place */
#         pi = partition(arr, low, high);

#         quickSort(arr, low, pi - 1);  // Before pi
#         quickSort(arr, pi + 1, high); // After pi
#     }
# }

# This funciton takes last element as pivot, places 
# the pivot elemtn at its correct position in sorted
# array, and place all smaller (smaller than pivot)
# to left of pivot and all greater elemetns to right
# of pivot

from os import sep

def partition (arr,low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low,high):
        if arr[j] >= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] #swapping
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1, high)

# Driver code to test above
arr = [10,7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i], sep=',', end=" ") # %d acts a placeholder for number. This associated values are passed in via a list using the % operator
    # To print without newline in Phyton used print(a[i], end =" "), print(sep='') will print in between
    