def binary_search(sorted_arr,target):
    start=0
    end=len(sorted_arr)-1

    while start<=end:
        middle=(end+start)//2
        if sorted_arr[middle]<target:
            start=middle+1
        elif sorted_arr[middle]>target:
            end=middle-1
        else:
            return middle
    return -1