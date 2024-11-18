## You're given an array of integer arr and integer k.
## Find the maximum element of each contiguous subarray of size k.


def maxElement(arr, k):
    """
    Arguments: arr-> array of elements, k->window of contiguous elements

    Return: Max element from the contiguous subarray.

    Exception: If the array is empty, return an empty array.
    """
    result=[]
    if len(arr) == 0:
        return []
    
    for i in range(len(arr)):
        if len(arr[i:i+k])==k:
            result.append(max(arr[i:i+k]))
        else:
            break
    
    return result

arr=[1,3,-1,-3,5,3,6,7]
k=3
op=maxElement(arr,k)
print(op)









