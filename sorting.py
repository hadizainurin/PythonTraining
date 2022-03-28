def bubbleSort(arr):
    n = len(arr) # We need to know the length of array
    #Traverse through all array eleemnts
    for i in range(n-1):
        for j in range(0, n-i-1): #This is how you do nested loop
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j] #swap the element if one is greater

#Test Code
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end="")