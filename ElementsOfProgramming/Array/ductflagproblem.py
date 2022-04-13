# Write a program that takes an array A and an index i into A, and rearranges the elements such
# that all elements less than A[r] (the "pivot") appear first, followed by elements equal to the pivot,
# followed by elements greater than the pivot.

RED, WHITE, BLUE = range(3) #Create a constant of three variables

def partition(pivot_index, A):
    pivot = A[pivot_index]
    #first pass: group elements smaller than pivot