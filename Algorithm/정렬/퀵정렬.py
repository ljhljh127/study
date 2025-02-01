# 삽입 정렬 (O(N^2))
from collections import deque

def quick_sort(array):
    left_array = []
    right_array = []
    pivot = 0
    maxindex_array = deque()
    minindex_array = deque()
    for i in range(1,len(array)):
        if array[i]>array[pivot]:
            maxindex_array.append(i)
        if array[-i]<array[pivot]:
            minindex_array.append(-i)
        if maxindex_array and minindex_array:
            max_index = maxindex_array.popleft()
            min_index = minindex_array.popleft()
            if max_index>-min_index:
                array[pivot],array[min_index] = array[min_index],array[pivot]
                answer = []
                answer.append(array[min_index])
                print(answer)
                left_array = array[:min_index]
                right_array = array[min_index+1:]
                break
            else:
                array[max_index],array[min_index] = array[min_index], array[max_index]

    quick_sort(left_array)
    quick_sort(right_array)
        
    return unsorted_array








unsorted_array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort(unsorted_array))