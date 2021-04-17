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

if __name__=='__main__':

    arr=[3,5,2,4,1]

    arr_for_ss=copy.deepcopy(arr)
    selection_sort(arr_for_ss)
    print(f'selection_sort: {arr_for_ss}')