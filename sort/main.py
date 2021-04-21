import copy
from quick_sort import quick_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from bubble_sort import bubble_sort
from heap_sort import heap_sort
from insertion_sort import insertion_sort

if __name__=='__main__':

    arr=[3,5,2,4,1,6]

    arr_for_ss=copy.deepcopy(arr)
    selection_sort(arr_for_ss)
    print(f'selection_sort: {arr_for_ss}')

    arr_for_qs=copy.deepcopy(arr)
    arr_for_qs=quick_sort(arr_for_qs)
    print(f'quick_sort    : {arr_for_qs}')

    arr_for_ms=copy.deepcopy(arr)
    arr_for_ms=merge_sort(arr_for_ms)
    print(f'merge_sort    : {arr_for_ms}')

    arr_for_bs=copy.deepcopy(arr)
    arr_for_bs=bubble_sort(arr_for_bs)
    print(f'bubble_sort   : {arr_for_bs}')

    arr_for_hs=copy.deepcopy(arr)
    arr_for_hs=heap_sort(arr_for_hs)
    print(f'heap_sort     : {arr_for_hs}')

    arr_for_is=copy.deepcopy(arr)
    arr_for_is=insertion_sort(arr_for_is)
    print(f'insertion_sort: {arr_for_is}')