array = [7,3,9,13,11,5,23,22]
def bubble_sort(array):
    n = len(array)
    for i in range (n):
        for j in range(0, n-i-1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array

array1 = bubble_sort(array)
print(array1)