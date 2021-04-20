def insertion_sort(arr):
    if len(arr)<=1:
        return arr
    for i in range(1,len(arr)):
        insertion_index=i
        while arr[insertion_index-1]>arr[insertion_index] and insertion_index>0:
            arr[insertion_index-1],arr[insertion_index]=arr[insertion_index],arr[insertion_index-1]
            insertion_index-=1
    return arr