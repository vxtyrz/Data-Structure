array = [7,3,9,13,11,5,23,22]
def insertion_sort(array):
    n = len(array)
    for i in range (1,n):
        marcado = array[i]
        j = i - 1
        while j >= 0 and marcado < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array [j + 1] = marcado
    return array

array1 = insertion_sort(array)
print(array1)