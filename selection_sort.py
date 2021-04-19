def search_min_index(arr):
    min_index=0
    for i in range(len(arr)):
        if arr[min_index]>arr[i]:
            min_index=i
    return min_index

def swap(i,j,arr):
    tmp=arr[i]
    arr[i]=arr[j]
    arr[j]=tmp

def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index=i+search_min_index(arr[i:])
        swap(i,min_index,arr)
