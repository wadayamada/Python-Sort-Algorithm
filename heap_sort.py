def heap_sort(arr):
    for i in reversed(range(len(arr)//2)):
        downheap(arr,i,len(arr)-1)    
    for i in reversed(range(len(arr))):
        arr[0],arr[i]=arr[i],arr[0]
        downheap(arr,0,i-1)
    return arr

def downheap(arr,parent_index,end_index):
    child0_index=parent_index*2+1
    child1_index=child0_index+1

    if child0_index>end_index and child1_index>end_index:
        return

    if child0_index>end_index:
        larger_child_index=child1_index
    elif child1_index>end_index:
        larger_child_index=child0_index
    else:
        if arr[child0_index]>arr[child1_index]:
            larger_child_index=child0_index
        else:
            larger_child_index=child1_index
        
    if arr[parent_index]<arr[larger_child_index]:
        arr[parent_index],arr[larger_child_index]=arr[larger_child_index],arr[parent_index]
        downheap(arr,larger_child_index,end_index)
    


