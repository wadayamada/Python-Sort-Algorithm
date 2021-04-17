import copy

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

if __name__=='__main__':

    arr=[3,5,2,4,1]

    arr_for_ss=copy.deepcopy(arr)
    selection_sort(arr_for_ss)
    print(f'selection_sort: {arr_for_ss}')

    arr_for_qs=copy.deepcopy(arr)
    arr_for_qs=quick_sort(arr_for_qs)
    print(f'quick_sort    : {arr_for_qs}')