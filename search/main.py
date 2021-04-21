from linear_sort import linear_sort
from binary_search import binary_search

if __name__=='__main__':

    arr=[3,5,2,4,1,6]
    target=4

    print(f'linea_search  : index={linear_sort(arr,target)}')

    sorted_arr=sorted(arr)
    print(f'binary_search : index={binary_search(sorted_arr,target)}')