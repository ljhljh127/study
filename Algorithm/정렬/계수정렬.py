
def count_sort():
    unsorted_list = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
    result = []
    array = [0 for _ in range(max(unsorted_list)+1)]
    for i in unsorted_list:
        array[i] +=1

    for i in range(len(array)):
        if array[i] != 0:
            result += [i]*array[i]
    
    return result

print(count_sort())

