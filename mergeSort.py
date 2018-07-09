def mergeSort(A):
    #base case if the input array is one or zero just return.
    if len(A) > 1:
        #splitting input array
        print('splitting', A)
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]
        #recursive calls to mergeSort for left and right sub arrays
        mergeSort(left)
        mergeSort(right)

        #initializes pointers for left(i) right(j) sub arrays
        #and output array (k)
        i = j = k = 0

        #Traverse and merges the sorted arrays
        while i < len(left) and j < len(right):
            if(left[i] < right[j]):
                A[k] = left[i]
                i = i + 1
            else:
                #if right <= left assignment
                A[k] = right[j]
                j = j + 1

            k = k + 1

        while i < len(left):
            #Assignment operation
            A[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            A[k] = right[j]
            j = j + 1
            k = k + 1

        print('merging', A)
        return(A)

if __name__ == "__main__":
    mergeSort([356,97,846,215])
