# 삽입 정렬 (O(N^2))

def insertion_sort():
    unsorted_list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    for i in range(1,len(unsorted_list)):
        for j in range(i,0,-1):
            if unsorted_list[j-1]>unsorted_list[j]:
                unsorted_list[j-1], unsorted_list[j] = unsorted_list[j], unsorted_list[j-1]
            else:
                break
    return unsorted_list

print(insertion_sort())