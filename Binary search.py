Array = [12, 48, 1, 5, 23, 15, 46, 19]
Key = 23

def BubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


def BinarySearch(array, key, left, right):
    while left <= right:

        mid = left + (right - left) // 2

        if array[mid] == key:
            return mid
        elif array[mid] < key:
            left = mid - 1
        else:
            right = mid + 1

    return None

Array  = BubbleSort(Array)
print BinarySearch(Array, Key, 0, len(Array) - 1)
