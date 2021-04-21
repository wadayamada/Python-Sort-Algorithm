def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    left=merge_sort(left)
    right=merge_sort(right)

    return merge(left,right)

def merge(left,right):
    
    left_index=0
    right_index=0

    merged_arr=[]

    while left_index<len(left) and right_index<len(right):
        if left[left_index]<right[right_index]:
            merged_arr.append(left[left_index])
            left_index+=1
        else:
            merged_arr.append(right[right_index])
            right_index+=1
    
    if left_index<len(left):
        merged_arr+=left[left_index:]
    if right_index<len(right):
        merged_arr+=right[right_index:]

    return merged_arr
            