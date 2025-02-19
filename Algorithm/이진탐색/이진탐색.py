"""
내가 평소 이진탐색을 구현하던 방식은 리스트의 슬라이싱을 이용하는 방법이었다 이는 공간복잡도 측면에서 좋지 않으므로
인덱스를 넘겨 하는 방식으로 이진탐색을 구현하는 연습을 한다.
"""

recursive_def_count = 0


# 재귀 방식
def binary_search(start, end, target, array):
    global recursive_def_count
    if start > end:
        return "not found"
    recursive_def_count += 1
    mid = (start + end) // 2

    if target == array[mid]:
        print("탐색횟수", recursive_def_count)
        return array[mid]
    elif target > array[mid]:
        return binary_search(mid + 1, end, target, array)
    else:
        return binary_search(start, mid - 1, target, array)


# sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 3
# print(binary_search(0, len(sorted_array) - 1, target, sorted_array))


# 반복문 방식
def binary_search_while(start, end, target, array):
    while True:
        if start > end:
            return "not found"
        mid = (start + end) // 2

        if array[mid] == target:
            return array[mid]
        elif target > array[mid]:
            start = mid + 1
        else:
            end = mid - 1


sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 1
print(binary_search_while(0, len(sorted_array) - 1, target, sorted_array))
