def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot_index=len(arr)//2
    left=[]
    right=[]
    for i in range(len(arr)):
        if arr[i] <= arr[pivot_index] and i!=pivot_index:
            left.append(arr[i])
        if arr[i] > arr[pivot_index]:
            right.append(arr[i])
    left=quick_sort(left)
    right=quick_sort(right)
    return left+[arr[pivot_index]]+right