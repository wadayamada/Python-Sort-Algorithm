import copy
from quick_sort import quick_sort
from selection_sort import selection_sort
from merge_sort import merge_sort

if __name__=='__main__':

    arr=[3,5,2,4,1]

    arr_for_ss=copy.deepcopy(arr)
    selection_sort(arr_for_ss)
    print(f'selection_sort: {arr_for_ss}')

    arr_for_qs=copy.deepcopy(arr)
    arr_for_qs=quick_sort(arr_for_qs)
    print(f'quick_sort    : {arr_for_qs}')

    arr_for_ms=copy.deepcopy(arr)
    arr_for_ms=merge_sort(arr_for_ms)
    print(f'merge_sort    : {arr_for_ms}')