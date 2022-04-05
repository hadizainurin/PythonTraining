# #So let start with a simple ideas on how you will swap an array
# arr = [0,1,2,3,4]
# arr[0], arr[1] = arr[1], arr[0] #arr = 1,0,2,3,4
# arr[1], arr[2] = arr[2], arr[1] #arr = 1,2,0,3,4
# arr[0], arr[1] = arr[1], arr[0] #arr = 2,1,0,3,4
# print(arr)

### END DEMONSTRATION ###

#Advance
#This is essentially a swapping problem which is solved using a swapping algorithm
#Say you want to swap an array to an even numbers then odd number
#Do this without allocating extra storage

#Question: How do we swap an array in ascending order when the values of array is even then it is sorted first.

def even_odd(arr):
    next_even, next_odd = 0, len(arr) - 1

    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even] #swapping algorithm
            next_odd -= 1
    return arr

# O(n) time with O(1) space complexity
#
#One common problem in building an array algorithm is that you must not used paranthesis () in place of bracket []

# def even_odd(arr):
#     next_even, next_odd = len(arr) - 1, 0 #swapping even or odd, A/B

#     while next_even > next_odd: #Execute as long as condition is true, <, >
#         if arr[next_even] % 2 == 0:
#                 next_even -= 1
#         else:
#             arr[next_odd], arr[next_even] = arr[next_even], arr[next_odd] #Does not really matter how you call the flag
#             next_odd += 1
#     return arr

arr = [1,2,3,4,5,6,7,8] #unclassified array
#even array, odd array
#initially even array and odd are empty
#But as we move the elemenets to the boundaris of the Even and Odd subarrays via swaps, thereby expanding Even an dOdd and shrinking unclassified
#print(len(arr)) this shows that list index out of range because we only have 7 arrays and not 8
print(even_odd(arr))