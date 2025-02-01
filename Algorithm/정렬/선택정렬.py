# 선택정렬
# O(N^2)
def selection_sort():
    unsorted_list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    for i in range(len(unsorted_list)):
        minindex = i
        for j in range(i+1,len(unsorted_list)):
            if unsorted_list[j]<unsorted_list[minindex]:
                minindex = j
        temp = unsorted_list[i]
        unsorted_list[i] = unsorted_list[minindex]
        unsorted_list[minindex] = temp
    return unsorted_list


print(selection_sort())