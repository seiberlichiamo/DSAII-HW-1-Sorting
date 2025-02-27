##Selection sort Method. 
#@param – A is the inputted array.
#@return – A returned is the sorted array
def selectionSort(A, n):
        for i in range(0, n - 1):
                smallest = i
                for j in range(i+1, n):
                        if A[j] < A[smallest]:
                                smallest = j
                temp = A[i]
                A[i] = A[smallest]
                A[smallest] = temp
        return A

##Test code.
arr = [1,3,5,6,2]
selectionSort(arr, len(arr))
print(arr)	


import math

##Function meant to recursively sort an array using merge-sort.
##@param – A is the array being brought in
##@param – beginning is the first index of the array
##@param – last is the last index in the array/array segment
def mergeSort (A, first, last):
       if first < last:
                mid = (first + last)//2
                mergeSort(A, first, mid)
                mergeSort(A, mid + 1, last)
                merge(A, first, mid, last)

##Function meant to take two halves of an array and sort them  repeatedly.
##@param – A is the inputted array
##@param – first is the first index of the array.
##@param – mid is the midpoint of the array determined in mergeSort half of the algorithm
##param – last is the last index of the array
def merge(A, first , mid, last):
        ##Make length of left and right subarrays
        n1 = mid - first + 1
        n2 = last - mid

        ##Make temporary arrays for left and right
        Left = [0] * n1
        Right = [0] * n2

        ##Set index for Left and Right arrays.
        for i in range(n1):
                Left[i] = A[first + i]
        for j in range(n2):
                Right[j] = A[mid + 1 + j]

        ##Initial index for left and right arrays
        i = 0
        j = 0

        for k in range(first, last + 1):
                if i < n1 and (j >= n2 or Left[i] <= Right[j]):
                        A[k] = Left[i]
                        i += 1
                else:
                        A[k] = Right[j]
                        j += 1

##Testing Merge Sort          
sortPlease = [38, 27, 43, 3, 9, 82, 10]
mergeSort(sortPlease, 0, len(sortPlease) - 1)
print(sortPlease)
