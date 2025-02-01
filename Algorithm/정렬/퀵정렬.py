def quick_sort(array):
    if len(array)<=1:
        return array
    pivot = array[0]
    small_list = []
    big_list = []
    for i in array[1:]:
        if i <=pivot:
            small_list.append(i)
        if i >pivot:
            big_list.append(i)
    
    return quick_sort(small_list) + [pivot] + quick_sort(big_list)









unsorted_array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort(unsorted_array))